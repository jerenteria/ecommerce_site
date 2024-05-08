import "./App.css";
import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([]);
    useEffect(() => {
      fetch("http://localhost:8000/api/data")
        .then((response) => response.json())
        .then((data) => setData(data));
    }, []);

  return (
    <div>
      <h1>Homepage</h1>
      <ul>
        {data.map((product) => (
          <li key={product.id}>{product.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
