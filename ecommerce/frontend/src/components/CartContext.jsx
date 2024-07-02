import React, { createContext, useState, useEffect } from "react";

// The Context API allows you to manage global state easily. This is useful for a cart where you need to access and update the cart items from multiple components
// (e.g., from the header, product listing, etc.).

export const CartContext = createContext();

export const CartProvider = ({ children }) => {
  const [cart, setCart] = useState([]);

  const addToCart = async (productId) => {
    try {
      const response = await fetch("http://localhost:8000/api/add_to_cart/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ product_id: productId, quantity: 1 }),
      });
      const result = await response.json();
      console.log("Add to cart response", result);
      if (result.status === "success") {
        console.log(`Product ${productId} added to cart`);
        setCart(result.cart); // Update the cart with the data returned from the backend
      } else {
        alert("Error adding item to cart");
      }
    } catch (error) {
      console.error("Error adding to cart:", error);
    }
  };

  const fetchCart = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/get_cart_items/");
      const cartData = await response.json();
      console.log("Fetched cart data:", cartData);
      setCart(cartData);
    } catch (error) {
      console.error("Error fetching cart data:", error);
    }
  };

  useEffect(() => {
    fetchCart();
  }, []);

  const removeFromCart = (productId) => {
    setCart((prevCart) => prevCart.filter((item) => item.id !== productId));
  };

  return (
    <CartContext.Provider value={{ cart, addToCart }}>
      {children}
    </CartContext.Provider>
  );
};
