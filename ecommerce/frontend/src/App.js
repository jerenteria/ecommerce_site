import "./App.css";
import React, { useState, useEffect } from "react";
import Header from "./components/Header";

function App() {
  const [data, setData] = useState([]);
  const [cart, setCart] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8000/api");
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const jsonData = await response.json();
        setData(jsonData);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  const fetchCart = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/get_cart_items");
      const cartData = await response.json();
      setCart(cartData);
    } catch (error) {
      console.error("Error fetching cart data:", error);
    }
  };

  // async function that calls API endpoint from backend to handle the adding items to cart
  // in the backend but handling adding item to cart button in front end
  const addToCart = async (productId) => {
    try {
      const csrftoken = getCookie("csrftoken");
      const response = await fetch("http://localhost:8000/api/add_to_cart", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({ product_id: productId, quantity: 1 }),
      });
      const result = await response.json();
      if (result.status === "success") {
        alert(result.message);
        fetchCart(); // Update the cart data after adding an item
      } else {
        alert("Error adding item to cart");
      }
    } catch (error) {
      console.error("Error adding to cart:", error);
    }
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

  useEffect(() => {
    fetchCart();
  }, []);

  return (
    <>
      <Header />
      <div className="products">
        <ul className="product-list">
          {data.map((product) => (
            <li key={product.id} className="product-item">
              {/* renders from media file; file is created from the updload_to path in models.py */}
              <img
                className="product-images"
                src={`http://localhost:8000/media/${product.image}`}
                alt={product.title}
              />
              <div>
                <h2>{product.title}</h2>
                <p>${product.price}</p>
                <button onClick={() => addToCart(product.id)}>
                  Add To Cart
                </button>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
}

export default App;
