export const fetchData = async (endpoint) => {
  try {
    const response = await fetch(`${process.env.REACT_APP_BASE_API_URL}${endpoint}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
    });

    const data = await response.json();
    return {data, status: response.status};
  } catch (error) {
    console.error("Error:", error);
  }
};

export const postData = async (endpoint, payload) => {
  try {
    const response = await fetch(`${process.env.REACT_APP_BASE_API_URL}${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
      credentials: "include",
    });
    const data = await response.json();
    return {data, status: response.status};
  } catch (error) {
    console.error("Error posting data:", error);
    throw error;
  }
};


export const deleteData = async (endpoint, payload) => {
  try {
    const response = await fetch(`${process.env.REACT_APP_BASE_API_URL}${endpoint}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
      credentials: "include",
    });

    const data = await response.json();
    return {data, status: response.status};
  } catch (error) {
    console.error("Error:", error);
  }
};