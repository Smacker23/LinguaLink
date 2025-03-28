import { React, useState } from "react";
import "../assets/css/Home.css";
import { useAuth, login } from '../components/AuthContext.js';
import Navbar from "../components/Navbar.jsx";
import { useNavigate, Link } from "react-router-dom";
import LoadingScreen from "../components/LoadingScreen.jsx";
import { fetchData, postData, deleteData } from "../components/Api.js";
function HomePage() {
  const { loading } = useAuth();
  const navigate = useNavigate();
  const [decks, setDecks] = useState([]);
  const new_deck = async (e) => {
    const quiz = {
      quiz: {
        name: "New Deck911231",
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
      }
    }
    const response = await postData('own-deck', quiz)
    if (response.status === 401) {
      navigate("/login");
    }
  }

  const get_deck = async (e) => {
    const quiz = 'New Deck911'
    const response = await fetchData(`own-deck`);
    if (response.status === 401) {
      navigate("/login");
    }
    console.log(response.data);
    setDecks(response.data.quizzes);
    console.log(decks);
  }

  const delete_deck = async (e, name) => {
    console.log(name);
    const quiz = {quiz: name}
    await deleteData('own-deck', quiz);
    await get_deck();
  }

  const get_profile = async (e) => {
    const quiz = 'New Deck911'
    const url = `${process.env.REACT_APP_BASE_API_URL}profile`;
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
    <div className="home content-container">
      <Navbar />
      <div className="color">
        <button
          style={{ width: "100px", height: "100px", backgroundColor: "#4CAF50", color: "white", border: "none", borderRadius: "8px", position: "absolute", top: "50%", left: "50%", transform: "translate(-50%, -50%)" }}
          onClick={new_deck}
        >
          POST
        </button>
        <button
          style={{ width: "100px", height: "100px", backgroundColor: "#4CAF50", color: "white", border: "none", borderRadius: "8px", position: "absolute", top: "50%", left: "60%", transform: "translate(-50%, -50%)" }}
          onClick={get_deck}
        >
          GET
        </button>
        {decks.map((deck, index) => (
          <>
            <div key={index} className="deck-wrapper">
              <button className="delete_deck" onClick={(e) => delete_deck(e, deck.name)}>X</button>
              <p>{deck.name}</p>
            </div>
          </>
        ))}
      </div>
    </div>
  );
}

export default HomePage;
