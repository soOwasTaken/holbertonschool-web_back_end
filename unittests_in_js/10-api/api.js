const express = require("express");
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// Root endpoint
app.get("/", (req, res) => {
  res.send("Welcome to the payment system");
});

// Endpoint for cart with number validation
app.get("/cart/:id(\\d+)", (req, res) => {
  const id = req.params.id;
  res.send(`Payment methods for cart ${id}`);
});

// New endpoint for available_payments
app.get("/available_payments", (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  });
});

// New endpoint for POST /login
app.post("/login", (req, res) => {
  res.send(`Welcome ${req.body.userName}`);
});

// Define the port and start listening
const PORT = 7865;
app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

// Export the app for testing
module.exports = app;
