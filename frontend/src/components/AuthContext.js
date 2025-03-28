import React, { createContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true); // Default to true while checking auth

    useEffect(() => {
        get_user();
    }, []);

    const get_user = async () => {
        console.log("Checking user authentication...");
        setLoading(true);
        try {
            const response = await fetch(`${process.env.REACT_APP_BASE_API_URL}get_user`, {
                method: "GET",
                credentials: "include",
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const data = await response.json();
            if (data.isAuthenticated) {
                setIsAuthenticated(true);
                setUser(data.user);
            } else {
                setIsAuthenticated(false);
                setUser(null);
            }
        } catch (error) {
            console.error("Error fetching user:", error);
            setIsAuthenticated(false);
            setUser(null);
        } finally {
            setLoading(false); // Ensure loading is disabled no matter what
        }
    };

    const login = async (username, password, rememberMe = false) => {
        console.log("Logging in...");
        setLoading(true);
        try {
            const response = await fetch(`${process.env.REACT_APP_BASE_API_URL}login`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password, rememberMe }),
                credentials: "include",
            });

            if (response.ok) {
                const data = await response.json();
                setIsAuthenticated(true);
                setUser(data.user);
                await get_user(); // Refresh user data
            }

            return response;
        } catch (error) {
            console.error("Error during login:", error);
        } finally {
            setLoading(false);
        }
    };

    const logout = async () => {
        console.log("Logging out...");
        setLoading(true);
        try {
            const response = await fetch(`${process.env.REACT_APP_BASE_API_URL}logout`, {
                method: "GET",
                credentials: "include",
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const data = await response.json();
            if (!data.isAuthenticated) {
                setIsAuthenticated(false);
                setUser(null);
            }
        } catch (error) {
            console.error("Error during logout:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <AuthContext.Provider value={{ isAuthenticated, user, loading, get_user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => React.useContext(AuthContext);
