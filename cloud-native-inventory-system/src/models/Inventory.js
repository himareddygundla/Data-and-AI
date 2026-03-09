const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const Inventory = sequelize.define(
  "Inventory",
  {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true
    },
    product_id: {
      type: DataTypes.INTEGER,
      unique: true
    },
    stock: {
      type: DataTypes.INTEGER,
      allowNull: false
    }
  },
  {
    tableName: "inventory",
    timestamps: false
  }
);

module.exports = Inventory;