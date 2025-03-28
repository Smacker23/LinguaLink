import "../assets/css/Home.css";
import React, { useState } from "react";
import { useAuth } from '../components/AuthContext.js';
import { fetchData, postData } from "../components/Api.js";
function HomePage() {
  const {get_user, login, logout, user} = useAuth();
  const get_user_button = async (e) => {
    await get_user();
  };

  const logout_button = async (e) => {
    await logout();
  };

  const login_button = async (e) => {
    const password = "!Teste123123";
    const username = "Teste";
    await login(username, password);
  };



  const [formData, setFormData] = useState({
    username: "",
});

  const handleChange = (e) => {
    setFormData({
        ...formData,
        [e.target.name]: e.target.value,
    })
}

  const add_follower = async (e) => {
    console.log(`${process.env.REACT_APP_BASE_API_URL}add-follower`)
    const data = await postData("add-follower", formData);
    console.log(data.data)
  }

  return (
    <div>
       <h1>{user ? `Welcome, ${user.username}` : "HEY Welcome Guest"}</h1> 
      <button
        style={{ width: "100px", height: "100px", backgroundColor: "#4CAF50", color: "white", border: "none", borderRadius: "8px" }}
        onClick={get_user_button}
      >
        GET USER
      </button>
      <button
        style={{ width: "100px", height: "100px", backgroundColor: "#4CAF50", color: "white", border: "none", borderRadius: "8px" }}
        onClick={logout_button}
      >
        LOGOUT
      </button>
      <button
        style={{ width: "100px", height: "100px", backgroundColor: "#4CAF50", color: "white", border: "none", borderRadius: "8px" }}
        onClick={login_button}
      >
        Login
      </button>
      <button
        style={{ width: "100px", height: "100px", backgroundColor: "#4CAF50", color: "white", border: "none", borderRadius: "8px" }}
        onClick={login_button}
      >
        Logout
      </button>
      <button
        style={{ width: "100px", height: "100px", backgroundColor: "#4CAF50", color: "white", border: "none", borderRadius: "8px" }}
        onClick={add_follower}
      >
        Add follower
      </button>
      <input type="text" name="username" placeholder="Username" value={formData.username} onChange={handleChange} />
    </div>
  );
}

export default HomePage;
