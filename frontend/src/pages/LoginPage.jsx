import React, { useState } from "react";
import { useAuth } from '../components/AuthContext.js';
import "../assets/css/Login.css";
import { FaUserAlt, FaEyeSlash, FaEye } from "react-icons/fa";
import Navbar from "../components/Navbar.jsx";
import RedirectIfAuthenticated from "../components/RedirectIfAuthenticated.jsx";
import LoadingScreen from "../components/LoadingScreen.jsx";
import { useNavigate, Link } from "react-router-dom";

function LoginPage() {
    const { isAuthenticated, login, loading } = useAuth();
    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);
    const navigate = useNavigate();


    const togglePassword = () => {
        setShowPassword(prevState => !prevState);
    };


    const toggleConfirmPassword = () => {
        setShowConfirmPassword(prevState => !prevState);
    };

    const [formData, setFormData] = useState({
        username: "",
        password: "",
        rememberMe: false
    });

    const updateErrors = (errors) => {
        setFormErrors(errors);
        console.log(formErrors);
    };

    const [formErrors, setFormErrors] = useState({
        error: "",
    });


    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData({
            ...formData,
            [name]: type === "checkbox" ? checked : value,
        });

    };




    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await login(formData.username, formData.password, formData.rememberMe);

            if (!response.ok) {
                const errors = await response.json();
                updateErrors(errors);
            }

            if (response.ok) {
                navigate("/");
            }

        } catch (error) {
            console.error("Error:", error);
        }
    };

    if (loading) {
        return <LoadingScreen />;
    }


    return (
        <div>
            <Navbar full={false} /><RedirectIfAuthenticated>
            <div className="login-container">
        
                    <form onSubmit={handleSubmit}>
                        <div className="wrapper-login">
                            <div className="sign-up">Login</div>
                            <div className="username">`<input type="text" name="username" placeholder="Username" value={formData.username} onChange={handleChange} required />`</div>
                            <div className="password">
                                <input
                                    type={showPassword ? "text" : "password"} name="password"
                                    placeholder="Password" value={formData.password} onChange={handleChange} required
                                />
                                {!showPassword && <FaEyeSlash
                                    className="icon"
                                    onClick={togglePassword}
                                    style={{ cursor: "pointer" }}
                                />}
                                {showPassword && <FaEye onClick={togglePassword} className="icon" />}
                                <div className="error">{formErrors.error}</div>
                            </div>
                            <div className="submit"><button type="submit">Login</button></div>
                            <div className="remember-me">
                                <div>
                                    <input
                                        type="checkbox"
                                        id="remember"
                                        name="rememberMe"
                                        className="checkbox"
                                        checked={formData.rememberMe}
                                        onChange={handleChange}
                                    /><label htmlFor="remember">Remember me</label>
                                </div>
                            </div>
                        </div>
                    </form>
                    <div className="login-redirect">
                        <p>Don't have an account? <Link to="/signup" className="a">Sign up</Link></p>
                    </div>
                
            </div>
            </RedirectIfAuthenticated>
        </div>
    );
}



export default LoginPage;
