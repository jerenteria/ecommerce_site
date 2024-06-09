import React, { useContext } from "react";
import "./CartContext.jsx";
import { CartContext } from "./CartContext.jsx";

export default Cart = ({ product }) => {
  const checkout = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/checkout/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
      });
      const result = await response.json();
      if (result.url) {
        window.location.href = result.url; // Redirect to Stripe checkout
      } else {
        alert("Error during checkout");
      }
    } catch (error) {
      console.error("Error during checkout:", error);
    }
  };

  const cartCtx = useContext(CartContext);
  const totalAmount = `$${cartCtx.totalAmount.toFixed(2)}`;
  const hasItems = cartCtx.items.length > 0;

  const cartItems = (
    <ul>
      {cartCtx.items.map((product) => (
        <li>{product.name}</li>
      ))}
      ;
    </ul>
  );

  return (
    <>
      <div className="cart-total">
        <span>Total:</span>
        <span>{totalAmount}</span>
      </div>
      <div className="actions">
        <button>Close</button>
        {hasItems && <button id="order-button" onClick={checkout}>Order</button>}
      </div>
    </>
  );
};
