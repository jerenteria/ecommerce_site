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
        credentials: 'include', // tells the browser to include cookies which often contains session information(crucial for maintaining session state between frontend and backend)
      });
      const result = await response.json();
      console.log("Add to cart response", result);
      if (result.status === "success") {
        console.log(`Product ${productId} added to cart`);
        console.log("New Cart state:", result.cart)
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
      const response = await fetch("http://localhost:8000/api/get_cart_items/", {
        credentials: "include", // tells the browser to include cookies which often contains session information(crucial for maintaining session state between frontend and backend)
      });
      const cartData = await response.json();
      console.log("Fetched cart data:", cartData);
      setCart(cartData);
    } catch (error) {
      console.error("Error fetching cart data:", error);
    }
  };

  // fetchCart is called inside useEffect() so that we only fetch the cart once we dont need to keep fetching the cart data
  useEffect(() => {
    fetchCart();
  }, []);

  const removeFromCart = async (productId, quantity = 1) => {
    try {
      const response = await fetch("http://localhost:8000/api/remove_from_cart/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ product_id: productId, quantity: quantity }),
        credentials: 'include',
      });
      const result = await response.json();
      console.log("Remove from cart response", result);
      if (result.status === "success") {
        console.log(`Product ${productId} removed from cart`);
        console.log("New Cart state:", result.cart)
        setCart(result.cart); // Update the cart with the data returned from the backend
      } else {
        alert("Error removing item from cart");
      }
    } catch (error) {
      console.error("Error removing from cart:", error);
    }
  };
  return (
    <CartContext.Provider value={{ cart, addToCart, removeFromCart }}>
      {children}
    </CartContext.Provider>
  );
};
