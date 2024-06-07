import React, { createContext, useState } from 'react';

// The Context API allows you to manage global state easily. This is useful for a cart where you need to access and update the cart items from multiple components 
// (e.g., from the header, product listing, etc.).

// CartContext will hold the cart state that will be shared with other components and provide functions to add/remove items from cart 
export const CartContext = createContext();

// children is taken in as a prop and is any nested component within CartProvider
export const CartProvider = ({ children }) => {
    const [cart, setCart] = useState([]);
  
    // takes in the product being added
    const addToCart = (product) => {
    // create a new array using the spread operator(...) with all the items already in the cart plus the new product added then
    // update the cart state with the new array
      setCart([...cart, product]);
    };
  
    // remove product from cart
    const removeFromCart = (productId) => {
      // get the cart and check if the productId is !== productId being selected(trying to be deleted), if the productId !== the productId of the product being deleted 
      // then that product stays, if the productId of the product selected does === productId of product selected then delete it because that means that is the product that the user wants to delete     
      setCart(cart.filter(item => item.id !== productId));
    };
  
    return (
        // 'value' prop of the 'Provider' is set to an object containing the current cart state and the function addToCart and removeFromCart. 
        // Any component that consumes this Context will have access to these values
      <CartContext.Provider value={{ cart, addToCart, removeFromCart }}>
        {children}
      </CartContext.Provider>
    );
  };