import { useEffect, useState } from "react";
import { useAuth } from "./AuthContext";
import { useNavigate } from "react-router-dom";
import "../assets/css/Home.css";
function RedirectIfAuthenticated({ children }) {
    const { isAuthenticated } = useAuth();
    const [message, setMessage] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        if (isAuthenticated) {
            setMessage("You are already logged in. Redirecting...");
            setTimeout(() => {
                navigate("/");
            }, 3000);
        }
    }, [isAuthenticated, navigate]);

    // If user is authenticated, only show the message
    if (isAuthenticated) {
        return <div className="logged-in-message">{message}
        
        <img src="./loading_spinner.svg" alt="" /></div>;
    }

    // Otherwise, render children (login/signup form)
    return children;
}

export default RedirectIfAuthenticated;
