import React, { useContext } from "react";
import "./CartContext.jsx";
import { CartContext } from "./CartContext.jsx";

const Cart = () => {
  const { cart } = useContext(CartContext);

  const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === `${name}=`) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };

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

  const totalAmount = cart.reduce(
    (total, item) => total + item.price * item.quantity,
    0
  );

  return (
    <>
      <div className="cart-total">
        <ul>
          {cart.map((item) => (
            <li key={item.id}>
              {item.title} - ${item.price}
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
