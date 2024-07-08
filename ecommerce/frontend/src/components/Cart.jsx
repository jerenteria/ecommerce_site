import React, { useContext } from "react";
import "./CartContext.jsx";
import { CartContext } from "./CartContext.jsx";
import "./Cart.css";
import DeleteItems from "./DeleteItems.jsx";

const Cart = () => {
  const { cart, removeFromCart } = useContext(CartContext);

  const checkout = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/checkout/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ cart }),
        credentials: "include", // This is important for sending cookies
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      if (result.url) {
        window.location.href = result.url; // Redirect to Stripe checkout
      } else if (result.error) {
        alert(`Checkout error: ${result.error}`);
      } else {
        alert("Unexpected response from server");
      }
    } catch (error) {
      console.error("Error during checkout:", error);
      alert(`Checkout failed: ${error.message}`);
    }
  };

  const totalAmount = cart.reduce(
    (total, item) => total + item.price * item.quantity,
    0
  );

  

  return (
    <>
      <div className="cart-total">
        <ul className="item-list">
          {cart.map((item) => (
            <li key={item.product_id}>
              {item.title} - ${item.price} x {item.quantity}
              <button className="remove-items-btn" onClick={() => removeFromCart(item.product_id)}>
                <DeleteItems />
              </button>
            </li>
          ))}
        </ul>
        <span>Total:</span>
        <span>${totalAmount.toFixed(2)}</span>
      </div>
      <div id="actions">
        {cart.length > 0 && (
          <button id="order-button" onClick={checkout}>
            Order
          </button>
        )}
      </div>
    </>
  );
};

export default Cart;
