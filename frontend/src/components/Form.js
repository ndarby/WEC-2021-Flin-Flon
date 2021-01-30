import React, { useState } from "react";

const Form = () => {
  const [response, setResponse] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.target);

    fetch("requests", {
      method: "POST",
      body: data,
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setResponse(JSON.stringify(data));
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="username">Enter username </label>
      <input id="username" name="username" type="text" />

      <label htmlFor="email">Enter your email </label>
      <input id="email" name="email" type="email" />

      <button>Send data</button>
      <h1>Response</h1>
      <p>{response}</p>
    </form>
  );
};

export default Form;
