import React, { useState } from "react";
import { MenuItem, InputLabel } from "@material-ui/core";
import Select from "@material-ui/core/Select";
import { useHistory } from "react-router-dom";
import {useAuth0} from "@auth0/auth0-react";


const DashBoard = () => {
  let history = useHistory();


  const { user } = useAuth0();
  const { email } = user;

  const [response, setResponse] = useState("");
  const [gameID, setgameID] = useState( "")

  const getGames = (event) => {
    event.preventDefault();
    const data = new FormData(event.target);

    fetch("Get User Dashboard", {
      method: "POST",
      body: {email : email}
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setResponse(JSON.stringify(data));
      });
  };

  const handleSubmit = (event) => {
    const data = new FormData(event.target);

    fetch("Join", {
      method: "POST",
      body: {email : email, gameID: gameID}
    })
        .then((res) => res.json())
        .then((data) => {
        console.log(data);
        setResponse(JSON.stringify(data));
      });

  };


  const CreateNewGame = () =>{

    history.push('/creategame');

  }


    return (
    <form onSubmit={handleSubmit}>
      <header>
        <h1> Game Dashboard</h1>
        <p>
          Create a game, enter the ID for games you would like to join, or
          select a game from the menu!
        </p>
      </header>

      <button onClick={CreateNewGame}> Create new Game! </button>
      <p></p>

      <label htmlFor="gameID">Game ID for game you would like to join: </label>
      <input id="gameID" name="gameID" type="text" />

      <button onClick = {handleSubmit}>Request to join game</button>
      <p></p>

      <InputLabel id="label">Available Games for you!</InputLabel>
      <Select labelId="label" id="select" value="20"></Select>

      <h1> Your Metrics</h1>
      <p>{response}</p>
    </form>
  );
};

export default DashBoard;
