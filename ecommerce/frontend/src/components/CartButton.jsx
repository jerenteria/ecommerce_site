import CartIcon from "./CartIcon.jsx";
import "./CartButton.css";
import React from "react";

const CartButton = ({ onClick }) => {
  return (
    <>
      {/* uses the onClick function from the CartButton in Header.jsx */}
      <button id="cart-button" onClick={onClick}>
        <CartIcon />
      </button>
    </>
  );
};

export default CartButton;
