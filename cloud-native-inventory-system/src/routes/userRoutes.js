const router = require("express").Router();
const User = require("../models/User");

// Create user
router.post("/", async (req, res) => {
  const user = await User.create(req.body);
  res.json(user);
});

// Read user
router.get("/:id", async (req, res) => {
  const user = await User.findByPk(req.params.id);
  res.json(user);
});

module.exports = router;