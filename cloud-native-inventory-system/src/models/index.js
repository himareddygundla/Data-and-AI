const sequelize = require("../config/db");

const User = require("./User");
const Product = require("./Product");
const Order = require("./Order");
const OrderItem = require("./OrderItem");
const Inventory = require("./Inventory");

// =========================
// Relationships
// =========================

// User → Orders
User.hasMany(Order, { foreignKey: "user_id" });
Order.belongsTo(User, { foreignKey: "user_id" });

// Order → OrderItems
Order.hasMany(OrderItem, { foreignKey: "order_id" });
OrderItem.belongsTo(Order, { foreignKey: "order_id" });

// Product → OrderItems
Product.hasMany(OrderItem, { foreignKey: "product_id" });
OrderItem.belongsTo(Product, { foreignKey: "product_id" });

// Product → Inventory (one-to-one)
Product.hasOne(Inventory, { foreignKey: "product_id" });
Inventory.belongsTo(Product, { foreignKey: "product_id" });

module.exports = {
  sequelize,
  User,
  Product,
  Order,
  OrderItem,
  Inventory,
};