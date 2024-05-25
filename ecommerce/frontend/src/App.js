import "./App.css";
import React, { useState, useEffect } from "react";
import Header from "./components/Header";

function App() {
  const [data, setData] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8000/api");
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const jsonData = await response.json();
        setData(jsonData);
        console.log(jsonData);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  return (
    <>
      <Header />
      <div className="products">
        <ul className="product-list">
          {data.map((product) => (
            <li key={product.id} className="product-item">
              {/* renders from media file; file is created from the updload_to path in models.py */}
              <img className="product-images"
                src={`http://localhost:8000/media/${product.image}`}
                alt={product.title}
              />
              <div>
                <h2>{product.title}</h2>
                <p>${product.price}</p>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
}

export default App;
