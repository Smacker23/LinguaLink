import React, { useState, useEffect } from "react";

const FlashcardApp = () => {
  const [characters, setCharacters] = useState([]); // Store fetched data
  const [currentIndex, setCurrentIndex] = useState(0); // Track current character

  useEffect(() => {
    // Fetch data from API
    fetch("http://127.0.0.1:8000/api/get-by-tag/Hiragana") // Replace with your API URL
      .then((response) => response.json())
      .then((data) => setCharacters(data.data)) // Extract "data" array from response
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  // Function to move to the next character
  const nextCharacter = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex < characters.length - 1 ? prevIndex + 1 : 0
    ); // Loops back to first character when reaching the end
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      {characters.length > 0 ? (
        <div className="p-6 bg-white rounded-lg shadow-lg text-center">
          <h1 className="text-5xl font-bold mb-4">
            {characters[currentIndex].word}
          </h1>
          <p className="text-xl text-gray-600">
            {characters[currentIndex].translated}
          </p>
          <button
            onClick={nextCharacter}
            className="mt-4 px-6 py-3 bg-blue-500 text-white text-lg font-semibold rounded-lg hover:bg-blue-600 transition"
          >
            Next Character
          </button>
        </div>
      ) : (
        <p className="text-xl text-gray-500">Loading...</p>
      )}
    </div>
  );
};

export default FlashcardApp;
