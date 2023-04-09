import React, { useState } from "react";
import "./App.css";

function App() {
  const [inputString, setInputString] = useState("");
  const [inputNumber, setInputNumber] = useState(0);
  const [outputString, setOutputString] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!inputString) {
      alert("Please enter a string.");
      return;
    }
    if (!inputNumber || isNaN(inputNumber)) {
      alert("Please enter a valid number.");
      return;
    }

    const output = Array(inputNumber).fill(inputString);

    setOutputString(output);
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <div>
          <label title="inputString">String:</label>
          <input
            type="text"
            id="inputString"
            value={inputString}
            onChange={(event) => setInputString(event.target.value)}
          />
        </div>
        <div>
          <label title="inputNumber">Number:</label>
          <input
            type="number"
            id="inputNumber"
            value={inputNumber}
            onChange={(event) => setInputNumber(parseInt(event.target.value))}
          />
        </div>
        <button type="submit">Submit</button>
        {outputString &&
          outputString.map((val, index) => <p>{`${index + 1}.${val}`}</p>)}
      </form>
    </div>
  );
}

export default App;
