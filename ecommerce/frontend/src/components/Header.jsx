import "./Header.css";
import "./CartIcon.jsx";
import CartButton from "./CartButton.jsx";
import React, { useState, useContext } from "react";
import { CartContext } from "./CartContext";
import Cart from "./Cart";

const Header = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const { cart } = useContext(CartContext);

  const toggleModal = () => {
    setIsModalOpen(!isModalOpen);
  };

  return (
    <>
      <div className="header">
        <h1 className="header-text">ModernMonarch</h1>
        <p id="quote">
          "Fashion fades, but style is eternal." – Yves Saint Laurent
        </p>
      </div>
      <div className="cart-button">
        <span>
          <CartButton onClick={toggleModal} />
        </span>
      </div>
      {isModalOpen && (
        <div className="cart-modal">
          <h2>Shopping Cart</h2>
          <Cart />
          <button onClick={toggleModal}>Close</button>
        </div>
      )}
    </>
  );
};

export default Header;
