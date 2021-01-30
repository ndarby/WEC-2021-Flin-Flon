import React, { useState } from "react";
import { MenuItem, InputLabel } from "@material-ui/core";
import Select from "@material-ui/core/Select";

const DashBoard = () => {
  const [response, setResponse] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.target);

    fetch("available_games", {
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
      <header>
        <h1> Game Dashboard</h1>
        <p>
          Create a game, enter the ID for games you would like to join, or
          select a game from the menu!
        </p>
      </header>

      <button>Create new Game!</button>
      <p></p>

      <label htmlFor="gameID">Game ID for game you would like to join: </label>
      <input id="gameID" name="gameID" type="text" />

      <button>Request to join game</button>
      <p></p>

      <InputLabel id="label">Available Games for you!</InputLabel>
      <Select labelId="label" id="select" value="20"></Select>

      <h1> Your Metrics</h1>
      <p>{response}</p>
    </form>
  );
};

export default DashBoard;
