import { useState } from "react";
import "../assets/css/Navbar.css";
import { useAuth } from "./AuthContext.js";
import { useNavigate } from "react-router-dom";
const Navbar = ({ full = true }) => {
  const { isAuthenticated, user, logout } = useAuth();
  const navigate = useNavigate();




  return (
    <nav className="navbar">
      <a href="/"><h1 className="navbar-brand">LinguaLink</h1></a>
      {full && (
        <>
          <h1 onClick={() => navigate("/my-decks")} className="link">My decks</h1>
          <h1>Community decks</h1>
          <h1>Profile</h1>
          <h1>{user ? `Welcome, ${user.username}` : "HEY SHORTY"}</h1>
          {isAuthenticated && <h1 onClick={logout} className="link">Logout</h1>}
          {!isAuthenticated &&
            <>
              <h1 onClick={() => navigate("/login")} className="link">Login</h1>
              <h1 onClick={() => navigate("/signup")} className="link">Register</h1>
            </>}
        </>)}
    </nav>
  );
};

export default Navbar;
