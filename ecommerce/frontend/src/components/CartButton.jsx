import CartIcon from "./CartIcon.jsx";
import "./CartButton.css";
import { useContext } from "react";
import { CartContext } from "./CartContext.jsx";

const CartButton = ({product}) => {

  return (
    <>
      <button id="cart-button">
        <CartIcon />
      </button>
    </>
  );
};

export default CartButton;
