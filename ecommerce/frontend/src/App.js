import "./App.css";
import React, { useState, useEffect, useContext } from "react";
import Header from "./components/Header";
import { CartProvider, CartContext } from "./components/CartContext";

function App() {
  const [data, setData] = useState([]);
  const { addToCart } = useContext(CartContext);

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


  return (
    <>
      <CartProvider>
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
      </CartProvider>
    </>
  );
}

export default App;
