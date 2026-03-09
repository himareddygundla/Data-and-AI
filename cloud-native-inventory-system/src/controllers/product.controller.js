const Product = require("../models/product.model");


// ✅ Create Product
exports.createProduct = async (req, res) => {
  try {
    const { name, description, price } = req.body;

    const product = await Product.create({
      name,
      description,
      price,
    });

    res.status(201).json(product);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};


// ✅ Get Product List (with pagination)
exports.getProducts = async (req, res) => {
  try {
    const page = parseInt(req.query.page) || 1;
    const limit = parseInt(req.query.limit) || 10;
    const offset = (page - 1) * limit;

    const products = await Product.findAndCountAll({
      limit,
      offset,
      order: [["createdAt", "DESC"]],
    });

    res.json({
      total: products.count,
      page,
      data: products.rows,
    });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};


// ✅ Update Product Price
exports.updatePrice = async (req, res) => {
  try {
    const { id } = req.params;
    const { price } = req.body;

    const product = await Product.findByPk(id);

    if (!product) {
      return res.status(404).json({ message: "Product not found" });
    }

    product.price = price;
    await product.save();

    res.json(product);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};


// ✅ Delete Product
exports.deleteProduct = async (req, res) => {
  try {
    const { id } = req.params;

    const deleted = await Product.destroy({
      where: { id },
    });

    if (!deleted) {
      return res.status(404).json({ message: "Product not found" });
    }

    res.json({ message: "Product deleted successfully" });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};