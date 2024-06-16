import React, { createContext, useState, useEffect } from 'react';

// The Context API allows you to manage global state easily. This is useful for a cart where you need to access and update the cart items from multiple components 
// (e.g., from the header, product listing, etc.).

export const CartContext = createContext();

export const CartProvider = ({ children }) => {
  const [cart, setCart] = useState([]);

  const fetchCart = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/get_cart_items/");
      const cartData = await response.json();
      setCart(cartData);
    } catch (error) {
      console.error("Error fetching cart data:", error);
    }
  };


  const addToCart = async (productId) => {
    try {
      const response = await fetch('http://localhost:8000/api/add_to_cart/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ product_id: productId, quantity: 1 }),
      });
      const result = await response.json();
      if (result.status === 'success') {
        console.log('Added to cart');
        fetchCart();
      } else {
        alert('Error adding item to cart');
      }
    } catch (error) {
      console.error('Error adding to cart:', error);
    }
  };

  useEffect(() => {
    fetchCart();
  }, []);


  const removeFromCart = (productId) => {
    setCart((prevCart) => prevCart.filter((item) => item.id !== productId));
  };

  return (
    <CartContext.Provider value={{ cart, addToCart, removeFromCart, fetchCart }}>
      {children}
    </CartContext.Provider>
  );
};