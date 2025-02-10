import React, { useEffect, useState } from 'react';
import { AuthProvider } from './components/AuthContext.js';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage.jsx";
import DebugPage from "./pages/DebugPage.jsx";
import SignupPage from "./pages/SignupPage.jsx";
import LoginPage from "./pages/LoginPage.jsx";
import ProfilePage from "./pages/ProfilePage.jsx"
import NotFoundPage from './pages/NotFoundPage.jsx';
import './App.css';

function App() {
  return (
    <AuthProvider>
    <Router>
      <Routes>
        <Route path="" element={<HomePage />} /> 
        <Route path="/home" element={<HomePage />} /> 
        <Route path="/debug" element={<DebugPage />} /> 
        <Route path="/signup" element={<SignupPage />} /> 
        <Route path="/login" element={<LoginPage />} />    
        <Route path="/profile/:username" element={<ProfilePage />} />
        <Route path="*" element={<NotFoundPage />} /> {/* Global 404 */}
      </Routes>
    </Router>
    </AuthProvider>
  );
}

export default App;
