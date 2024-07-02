import React, { useContext } from "react";
import "./CartContext.jsx";
import { CartContext } from "./CartContext.jsx";


const Cart = () => {
    const { cart } = useContext(CartContext);
  
    const checkout = async () => {
      try {
        const response = await fetch("http://localhost:8000/api/checkout/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
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
  
    const totalAmount = cart.reduce(
      (total, item) => total + item.price * item.quantity,
      0
    );
  
    return (
      <>
        <div className="cart-total">
        <ul>
          {cart.map((item) => (
            <li key={item.product_id}>
              {item.title} - ${item.price} x {item.quantity}
            </li>
          ))}
        </ul>
          <span>Total:</span>
          <span>${totalAmount.toFixed(2)}</span>
        </div>
        <div className="actions">
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


