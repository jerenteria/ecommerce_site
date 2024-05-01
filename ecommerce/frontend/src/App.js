import logo from "./logo.svg";
import "./App.css";

function App() {
  async function getBackendData() {
    const response = await fetch("http://localhost:8000/");
    const responseInJson = await response.json();
    console.log(responseInJson);
  }
}

export default App;
