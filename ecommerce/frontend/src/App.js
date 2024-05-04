import "./App.css";
import React, { useState, useEffect } from "react";

function App() {
  function getBackendData() {
    const [data, setData] = useState([]);

    useEffect(() => {
      fetch("http://localhost:8000/")
        .then((response) => response.json())
        .then((data) => setData(data));
    }, []);
  }

  return (
    <div>
      <h1>Homepage</h1>
      <ul>
        {data.map(item => (
          <li key={product.id}>{product.title}</li>
        ))}
      </ul>
    </div>
  )
}

export default App;
