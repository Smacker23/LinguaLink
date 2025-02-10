import React from "react";
import "../assets/css/Home.css";
import { useAuth, login } from '../components/AuthContext.js';
import Navbar from "../components/Navbar.jsx";
import { useNavigate, Link } from "react-router-dom";
import LoadingScreen from "../components/LoadingScreen.jsx";
function HomePage() {
  const { loading } = useAuth();
  const navigate = useNavigate();
  const new_deck = async (e) => {
    const quiz = { quiz:{
      name: "New Deck911",
      difficulty: "easy",
      tags: ["General Knowledge", "Fun"],
      public: false,
      original_language: "en",
      translated_language: "en",
      questions: [{
        question: "Question 1",
        answer: "Answer 1",
        difficulty: "easy",
        tags: ["General Knowledge", "Fun"],
      },
      {
        question: "Question 3",
        answer: "Answer 1",
        difficulty: "easy",
        tags: ["General Knowledge", "Fun"],
      },
      {
        question: "Question 11",
        answer: "Answer 1",
        difficulty: "easy",
        tags: ["General Knowledge", "Fun"],
      }]
    }}
    try {
      const response = await fetch("http://127.0.0.1:8000/api/own-deck", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(quiz),
        credentials: "include"
      });

      if (response.status === 401) {
        navigate("/login");
      }

    } catch (error) {
      console.error("Error:", error);
    }
  }

  const get_deck = async (e) => {
    const quiz ='New Deck911'
    const url = `http://127.0.0.1:8000/api/own-deck?name=${quiz}`;
    try {
      const response = await fetch(url, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include"
      });

      if (response.status === 401) {
        navigate("/login");
      }
      const data = await response.json();
      console.log(data)

    } catch (error) {
      console.error("Error:", error);
    }
  }

  const get_profile = async (e) => {
    const quiz ='New Deck911'
    const url = `http://127.0.0.1:8000/api/profile`;
    try {
      const response = await fetch(url, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include"
      });

      if (response.status === 401) {
        navigate("/login");
      }
      const data = await response.json();
      console.log(data)

    } catch (error) {
      console.error("Error:", error);
    }
  }

  if (loading) {
    return <LoadingScreen />;
  }

  return (
    <div className="home">
      <Navbar />
      <div className="color">
        <button
          style={{ width: "100px", height: "100px", backgroundColor: "#4CAF50", color: "white", border: "none", borderRadius: "8px", position: "absolute", top: "50%", left: "50%", transform: "translate(-50%, -50%)" }}
          onClick={get_profile}
        >
          POST
        </button>
        <button
          style={{ width: "100px", height: "100px", backgroundColor: "#4CAF50", color: "white", border: "none", borderRadius: "8px", position: "absolute", top: "50%", left: "60%", transform: "translate(-50%, -50%)" }}
          onClick={get_deck}
        >
          GET
        </button>
      </div>
    </div>
  );
}

export default HomePage;
