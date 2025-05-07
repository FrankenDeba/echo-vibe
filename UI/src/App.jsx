import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import RegistrationForm from "./components/registration";
import Home from "./components/Home";
import ThreeT from "./components/3T";
import BusinessDescription from "./components/BusinessDesc";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<RegistrationForm />} />
          <Route path="/home" element={<Home />} />
          <Route path="/3t" element={<ThreeT />} />
          <Route path="/business_desc" element={<BusinessDescription />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
