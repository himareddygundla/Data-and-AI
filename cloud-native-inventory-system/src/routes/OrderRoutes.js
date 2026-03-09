const router = require("express").Router();
const orderController = require("../controllers/orderController");

// Read order with JOIN
router.get("/:id", orderController.getOrderById);

module.exports = router;