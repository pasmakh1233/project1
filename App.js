import "./styles.css";
import React from "react";
import Capture from "./Capture.JPG";

function App() {
  return (
    <div
      style={{
        backgroundImage: "url(/img/Capture.JPG)",
        backgroundSize: "cover",
        height: "100vh",
        backgroundRepeat: "no-repeat",
        fontSize: "30px"
      }}
    >
      <h4>Please enter your ID and Password</h4>
      Your ID <input type="text" /> <br />
      <br />
      Password <input type="text" /> <br />
      <br />
      <button> Sign In</button> <button> Cancel</button>
    </div>
  );
}
export default App;
