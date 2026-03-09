const express = require("express");
const path = require("path");

const app = express();

app.use(express.json());

// ⭐ THIS LINE SERVES FRONTEND
app.use(express.static(path.join(__dirname, "../public")));

// routes
const productRoutes = require("./routes/productRoutes");
app.use("/products", productRoutes);

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});