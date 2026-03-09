const API = "/products";

// ✅ Load products on page load
window.onload = fetchProducts;

// ================= CREATE =================
async function createProduct() {
  const name = document.getElementById("name").value;
  const price = document.getElementById("price").value;
  const quantity = document.getElementById("quantity").value;

  await fetch(API, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, price, quantity }),
  });

  fetchProducts();
}

// ================= READ =================
async function fetchProducts() {
  const res = await fetch(API);
  const data = await res.json();

  const table = document.getElementById("productTable");
  table.innerHTML = "";

  data.forEach((p) => {
    table.innerHTML += `
      <tr>
        <td>${p.name}</td>
        <td>${p.price}</td>
        <td>${p.quantity}</td>
        <td>
          <button class="update-btn" onclick="updatePrice(${p.id})">Update</button>
          <button class="delete-btn" onclick="deleteProduct(${p.id})">Delete</button>
        </td>
      </tr>
    `;
  });
}

// ================= UPDATE =================
async function updatePrice(id) {
  const newPrice = prompt("Enter new price:");

  if (!newPrice) return;

  await fetch(`${API}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ price: newPrice }),
  });

  fetchProducts();
}

// ================= DELETE =================
async function deleteProduct(id) {
  await fetch(`${API}/${id}`, {
    method: "DELETE",
  });

  fetchProducts();
}