import "./App.css";
import React, { useState, useEffect, useContext } from "react";
import Header from "./components/Header";
import { CartProvider, CartContext } from "./components/CartContext";
import Card from './components/Card.jsx';

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

  return (
    <>
      <CartProvider>
        <Header />
        <div className="products">
          <ul className="product-list">
            {data.map((product) => (
              <li key={product.id} className="product-item">
                <Card>
                {/* renders from media file; file is created from the updload_to path in models.py */}
                <img
                  className="product-images"
                  src={`http://localhost:8000/media/${product.image}`}
                  alt={product.title}
                />
                <div>
                <h2>{product.title}</h2>
                <p>${product.price}</p>
                <CartContext.Consumer>
                  {({ addToCart }) => (
                    <button className="add-to-cart-button" onClick={() => addToCart(product.id)}>Add To Cart</button>
                  )}
                </CartContext.Consumer>
              </div>
              </Card>
              </li>
            ))}
          </ul>
        </div>
      </CartProvider>
    </>
  );
}

export default App;
