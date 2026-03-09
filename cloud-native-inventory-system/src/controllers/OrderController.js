const { Order, User, OrderItem, Product } = require("../models");

// ===============================
// Read Order by ID (WITH JOIN)
// ===============================
exports.getOrderById = async (req, res) => {
  try {
    const orderId = req.params.id;

    const order = await Order.findByPk(orderId, {
      include: [
        {
          model: User,
          attributes: ["id", "name", "email"],
        },
        {
          model: OrderItem,
          include: [
            {
              model: Product,
              attributes: ["id", "name", "price"],
            },
          ],
        },
      ],
    });

    if (!order) {
      return res.status(404).json({ message: "Order not found" });
    }

    res.json(order);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Server error" });
  }
};