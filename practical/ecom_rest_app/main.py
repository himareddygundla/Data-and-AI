from fastapi import FastAPI, Request, UploadFile, File, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict, List
import os
import uuid

app = FastAPI(title="E-commerce REST API + Web App")

templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# --------------------------
# Pydantic Models
# --------------------------
class ItemCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    category: Optional[str] = Field(default=None, max_length=50)

    model_config = ConfigDict(extra="forbid")


class ItemUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    price: Optional[float] = Field(default=None, gt=0)
    stock: Optional[int] = Field(default=None, ge=0)
    category: Optional[str] = Field(default=None, max_length=50)

    model_config = ConfigDict(extra="forbid")


class ItemOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float
    stock: int
    category: Optional[str] = None


class CartAdd(BaseModel):
    item_id: int
    quantity: int = Field(..., gt=0)

    model_config = ConfigDict(extra="forbid")


class CartItemOut(BaseModel):
    item_id: int
    title: str
    price: float
    quantity: int
    line_total: float


class CartOut(BaseModel):
    items: List[CartItemOut]
    subtotal: float


class CheckoutRequest(BaseModel):
    # super simplified checkout model
    name: str = Field(..., min_length=1, max_length=60)
    address: str = Field(..., min_length=5, max_length=200)
    payment_method: str = Field(..., pattern="^(COD|CARD|UPI)$")  # example

    model_config = ConfigDict(extra="forbid")


class PaymentRequest(BaseModel):
    order_id: str
    method: str = Field(..., pattern="^(CARD|UPI)$")
    amount: float = Field(..., gt=0)

    model_config = ConfigDict(extra="forbid")


# --------------------------
# In-memory "DB"
# --------------------------
items_db: Dict[int, Dict] = {}
next_item_id = 1

cart_db: Dict[int, int] = {}  # item_id -> quantity
orders_db: Dict[str, Dict] = {}  # order_id -> order details


# --------------------------
# Helpers
# --------------------------
def _get_item_or_404(item_id: int) -> Dict:
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


def _compute_cart() -> CartOut:
    out_items: List[CartItemOut] = []
    subtotal = 0.0

    for item_id, qty in cart_db.items():
        item = items_db.get(item_id)
        if not item:
            # if item removed from db, skip it
            continue
        line_total = float(item["price"]) * qty
        subtotal += line_total
        out_items.append(
            CartItemOut(
                item_id=item_id,
                title=item["title"],
                price=float(item["price"]),
                quantity=qty,
                line_total=line_total,
            )
        )

    return CartOut(items=out_items, subtotal=subtotal)


# --------------------------
# Error handling (clean JSON)
# --------------------------
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return fastapi_json_error(exc.status_code, exc.detail)


def fastapi_json_error(status_code: int, detail: str):
    from fastapi.responses import JSONResponse

    return JSONResponse(
        status_code=status_code,
        content={"error": {"code": status_code, "message": detail}},
    )


# ======================================================
# WEB APP PAGES (templates + upload + results)
# ======================================================
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # show sample list of items + cart subtotal
    cart = _compute_cart()
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "items": [ItemOut(**v).model_dump() for v in items_db.values()],
            "cart": cart.model_dump(),
        },
    )


@app.get("/upload", response_class=HTMLResponse)
def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request, "error": None})


@app.post("/upload", response_class=HTMLResponse)
async def upload_file(
    request: Request,
    title: str = Form(...),
    file: UploadFile = File(...),
):
    title = title.strip()

    if not title:
        return templates.TemplateResponse(
            "upload.html",
            {"request": request, "error": "Title is required."},
            status_code=400,
        )

    if not file.filename:
        return templates.TemplateResponse(
            "upload.html",
            {"request": request, "error": "Please choose a file."},
            status_code=400,
        )

    allowed = (".png", ".jpg", ".jpeg", ".pdf", ".txt")
    fname_lower = file.filename.lower()
    if not fname_lower.endswith(allowed):
        return templates.TemplateResponse(
            "upload.html",
            {"request": request, "error": f"Invalid file type. Allowed: {', '.join(allowed)}"},
            status_code=400,
        )

    safe_name = f"{uuid.uuid4().hex}_{os.path.basename(file.filename)}"
    save_path = os.path.join(UPLOAD_DIR, safe_name)

    content = await file.read()
    with open(save_path, "wb") as f:
        f.write(content)

    # send to results page
    return templates.TemplateResponse(
        "results.html",
        {
            "request": request,
            "title": title,
            "filename": file.filename,
            "saved_as": safe_name,
            "size": len(content),
        },
    )


# ======================================================
# REST API: ITEMS (Required)
# ======================================================
@app.get("/items", response_model=List[ItemOut])
def get_items(
    q: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
):
    # filters (e-commerce style)
    results = list(items_db.values())

    if q:
        ql = q.lower()
        results = [x for x in results if ql in x["title"].lower() or (x.get("description") or "").lower().find(ql) >= 0]

    if category:
        cl = category.lower()
        results = [x for x in results if (x.get("category") or "").lower() == cl]

    if min_price is not None:
        results = [x for x in results if float(x["price"]) >= float(min_price)]

    if max_price is not None:
        results = [x for x in results if float(x["price"]) <= float(max_price)]

    return [ItemOut(**x) for x in results]


@app.post("/items", response_model=ItemOut, status_code=201)
def create_item(payload: ItemCreate):
    global next_item_id

    item_id = next_item_id
    next_item_id += 1

    item = {
        "id": item_id,
        "title": payload.title,
        "description": payload.description,
        "price": float(payload.price),
        "stock": int(payload.stock),
        "category": payload.category,
    }
    items_db[item_id] = item
    return ItemOut(**item)


@app.put("/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int, payload: ItemUpdate):
    item = _get_item_or_404(item_id)

    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        item[k] = v

    items_db[item_id] = item
    return ItemOut(**item)


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    _get_item_or_404(item_id)
    del items_db[item_id]

    # also remove from cart if present
    if item_id in cart_db:
        del cart_db[item_id]

    return {"message": "Item deleted"}


# ======================================================
# CART: add/remove (Requested)
# ======================================================
@app.post("/cart/add")
def add_to_cart(payload: CartAdd):
    item = _get_item_or_404(payload.item_id)

    if item["stock"] <= 0:
        raise HTTPException(status_code=400, detail="Out of stock")

    current_qty = cart_db.get(payload.item_id, 0)
    new_qty = current_qty + payload.quantity

    if new_qty > item["stock"]:
        raise HTTPException(status_code=400, detail="Quantity exceeds available stock")

    cart_db[payload.item_id] = new_qty
    return {"message": "Added to cart", "cart": _compute_cart().model_dump()}


@app.post("/cart/remove")
def remove_from_cart(item_id: int, quantity: int = 1):
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="quantity must be > 0")

    if item_id not in cart_db:
        raise HTTPException(status_code=404, detail="Item not in cart")

    cart_db[item_id] -= quantity
    if cart_db[item_id] <= 0:
        del cart_db[item_id]

    return {"message": "Removed from cart", "cart": _compute_cart().model_dump()}


@app.get("/cart", response_model=CartOut)
def view_cart():
    return _compute_cart()


# ======================================================
# CHECKOUT + PAYMENT (Requested)
# ======================================================
@app.post("/checkout")
def checkout(payload: CheckoutRequest):
    cart = _compute_cart()
    if not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    # reduce stock
    for ci in cart.items:
        item = _get_item_or_404(ci.item_id)
        if ci.quantity > item["stock"]:
            raise HTTPException(status_code=400, detail=f"Not enough stock for item_id={ci.item_id}")
        item["stock"] -= ci.quantity
        items_db[ci.item_id] = item

    order_id = f"ORD-{uuid.uuid4().hex[:10].upper()}"
    order = {
        "order_id": order_id,
        "customer": {"name": payload.name, "address": payload.address},
        "payment_method": payload.payment_method,
        "subtotal": cart.subtotal,
        "status": "PENDING_PAYMENT" if payload.payment_method in ("CARD", "UPI") else "CONFIRMED",
        "items": [ci.model_dump() for ci in cart.items],
    }
    orders_db[order_id] = order

    # clear cart after checkout
    cart_db.clear()

    return {"message": "Checkout successful", "order": order}


@app.post("/payment")
def payment(payload: PaymentRequest):
    order = orders_db.get(payload.order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order["status"] == "CONFIRMED":
        raise HTTPException(status_code=400, detail="Order already confirmed")

    if float(payload.amount) != float(order["subtotal"]):
        raise HTTPException(status_code=400, detail="Amount mismatch")

    order["status"] = "CONFIRMED"
    order["paid_via"] = payload.method
    orders_db[payload.order_id] = order

    return {"message": "Payment successful", "order": order}


# ======================================================
# AUTHENTICATION + AUTHORIZATION (Simple demo)
# ======================================================
# NOTE: For real projects use OAuth2/JWT. This is minimal for learning.
FAKE_USERS = {
    "admin-token": {"username": "admin", "role": "admin"},
    "user-token": {"username": "user", "role": "user"},
}


def require_auth(request: Request) -> Dict:
    token = request.headers.get("X-API-KEY")
    if not token or token not in FAKE_USERS:
        raise HTTPException(status_code=401, detail="Unauthorized (missing/invalid X-API-KEY)")
    return FAKE_USERS[token]


def require_admin(user: Dict):
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Forbidden (admin only)")


@app.get("/me")
def me(request: Request):
    user = require_auth(request)
    return {"user": user}


@app.delete("/admin/orders/{order_id}")
def admin_delete_order(order_id: str, request: Request):
    user = require_auth(request)
    require_admin(user)

    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")

    del orders_db[order_id]
    return {"message": "Order deleted (admin)", "order_id": order_id}