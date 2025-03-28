import React, { useState } from "react";
import { useAuth } from '../components/AuthContext.js';
import "../assets/css/Signup.css";
import { FaUserAlt, FaEyeSlash, FaEye } from "react-icons/fa";
import Navbar from "../components/Navbar.jsx";
import { useNavigate, Link } from "react-router-dom";
import LoadingScreen from "../components/LoadingScreen.jsx";
import RedirectIfAuthenticated from "../components/RedirectIfAuthenticated.jsx";

function SignupPage() {
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
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        confirmPassword: "",
        rememberMe: false
    });

    const [formErrors, setFormErrors] = useState({
        username: "",
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        confirmPassword: "",
    });

    const updateErrors = (errors) => {
        setFormErrors(errors);
        console.log(formErrors);
    };

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData({
            ...formData,
            [name]: type === "checkbox" ? checked : value,
        });

    };

    const form_validation = () => {
        if (formData.password !== formData.confirmPassword) {
            setFormErrors({ ...formErrors, confirmPassword: "Passwords do not match" });
        }
    }


    const handleSubmit = async (e) => {
        e.preventDefault();
        //form_validation(); Implement also a frontend form validation ??
        try {
            const response = await fetch(`${process.env.REACT_APP_BASE_API_URL}signup`, {
                method: "POST",
                headers: { "Content-Type": "application/json", },
                body: JSON.stringify(formData),
                credentials: "include"
            });

            if (!response.ok) {
                const errors = await response.json();
                updateErrors(errors.error);
            }

            const data = await response.json();

            if (response.ok) {
                login(formData.username, formData.password, formData.rememberMe);
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
            <Navbar full={false} />
            <RedirectIfAuthenticated>
            <div className="signup-container">
                
                    <form onSubmit={handleSubmit}>
                        <div className="wrapper-signup">
                            <div className="sign-up">Sign Up</div>
                            <div className="username error-border">
                                <input type="text" name="username" placeholder="Username" value={formData.username} onChange={handleChange} required />
                                <div className="error">{formErrors.username}</div>
                            </div>
                            <div className="first-name error-border">
                                <input type="text" name="firstName" placeholder="First name" value={formData.firstName} onChange={handleChange} required />
                                <div className="error">{formErrors.firstName}</div>
                            </div>
                            <div className="last-name error-border">
                                <input type="text" name="lastName" placeholder="Last name" value={formData.lastName} onChange={handleChange} required />
                                <div className="error">{formErrors.lastName}</div>
                            </div>
                            <div className="email error-border">
                                <input type="text" name="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
                                <div className="error">{formErrors.email}</div>
                            </div>
                            <div className="password error-border">
                                <input
                                    type={showPassword ? "text" : "password"}
                                    name="password"
                                    placeholder="Password"
                                    value={formData.password}
                                    onChange={handleChange}
                                    required
                                />
                                {!showPassword ? (
                                    <FaEyeSlash className="icon" onClick={togglePassword} style={{ cursor: "pointer" }} />
                                ) : (
                                    <FaEye onClick={togglePassword} className="icon" />
                                )}
                                <div className="error">{formErrors.password}</div>
                            </div>
                            <div className="confirm-password error-border">
                                <input
                                    type={showConfirmPassword ? "text" : "password"}
                                    name="confirmPassword"
                                    placeholder="Confirm password"
                                    value={formData.confirmPassword}
                                    onChange={handleChange}
                                    required
                                />
                                {!showConfirmPassword ? (
                                    <FaEyeSlash className="icon" onClick={toggleConfirmPassword} style={{ cursor: "pointer" }} />
                                ) : (
                                    <FaEye onClick={toggleConfirmPassword} className="icon" />
                                )}
                                <div className="error">{formErrors.confirmPassword}</div>
                            </div>
                            <div className="submit">
                                <button type="submit">Sign up</button>
                            </div>
                            <div className="remember-me">
                                <div>
                                    <input
                                        type="checkbox"
                                        id="remember"
                                        name="rememberMe"
                                        className="checkbox"
                                        checked={formData.rememberMe}
                                        onChange={handleChange}
                                    />
                                    <label htmlFor="remember">Remember me</label>
                                </div>
                            </div>
                        </div>
                    </form>
                    <div className="login-redirect">
                        <p>Already have an account? <Link to="/login" className="a">Login</Link></p>
                    </div>
               
            </div>
            </RedirectIfAuthenticated>
        </div>
    );

}



export default SignupPage;
