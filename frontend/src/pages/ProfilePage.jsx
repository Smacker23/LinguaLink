import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { fetchData } from "../components/Api";
import LoadingScreen from "../components/LoadingScreen.jsx";
import NotFoundPage from "./NotFoundPage.jsx";
import { useAuth } from "../components/AuthContext.js";
import "../assets/css/Profile.css";
function ProfilePage() {
    const { user } = useAuth();
    const { username } = useParams();
    const [profile, setprofile] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const getProfile = async () => {
            try {
                const data = await fetchData(`profile/${username}`);
                console.log(data)
                if (data.status == 200) {
                    setprofile(data.data);
                }
                console.log("user logged", user)
            } catch (error) {
                console.error("Error fetching profile:", error);
            } finally {
                setLoading(false);
            }
        };

        getProfile();
    }, [username]);

    if (loading) {
        return <LoadingScreen />;
    }

    if (profile == null) {
        <NotFoundPage />
    }

    if (profile == null) {
        return <NotFoundPage />
    }
    console.log(profile)
    return (
        <div>
            <h1>Profile Page</h1>
            <p> {profile.profilename}</p>
            <p> {profile.firstName} {profile.lastName}</p>
            <p>followers: {profile.followers} following {profile.following}</p>
            {profile.owner && <>
            
            <div className="box"></div>
            </>}
        </div>
    );
}

export default ProfilePage;
