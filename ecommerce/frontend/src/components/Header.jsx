import "./Header.css";
import "./CartIcon.jsx";
import CartButton from "./CartButton.jsx";

const Header = () => {
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
          <CartButton />
        </span>
      </div>
    </>
  );
};

export default Header;
