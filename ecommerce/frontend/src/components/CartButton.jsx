import CartIcon from "./CartIcon.jsx";
import "./CartButton.css";
import { React, useContext } from "react";
import { CartContext } from "./CartContext.jsx";

const CartButton = ({ onClick }) => {
  const { cart } = useContext(CartContext);

  const numberOfCartItems = cart && Array.isArray(cart) // check that cart exists(not null or undefined) & is an array
  ? cart.reduce((currentNumber, item) => { // if cart exists and is an array use reduce(iterate through the whole array and sum up the total number of items in cart)
      return currentNumber + (item.quantity || 0); // return currentNumber + quantity of evert item or 0 if there is nothing in cart
    }, 0)
  : 0;
  return (
    <>
      {/* uses the onClick function from the CartButton in Header.jsx */}
      <button id="cart-button" onClick={onClick}>
        <CartIcon />
        <span id="number-of-cart-items">{numberOfCartItems}</span>
      </button>
    </>
  );
};

export default CartButton;
