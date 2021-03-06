import React, { useState } from "react";
import { MenuItem, InputLabel } from "@material-ui/core";
import Select from "@material-ui/core/Select";
import { useHistory } from "react-router-dom";
import { useAuth0 } from "@auth0/auth0-react";
import AvailableGamesSelector from "../components/AvailableGamesSelector";

const DashBoard = ({ setGameID }) => {
  let history = useHistory();

  const [newGameID, setNewGameID] = useState(0);

  const { user } = useAuth0();
  const { email } = user;

  const [response, setResponse] = useState("");
  const [openGames, setOpenGames] = useState([]);
  const [screenName, setScreenName] = useState("");
  const [metrics, setMetrics] = useState({});

  const getGames = (event) => {
    event.preventDefault();

    fetch("dashboard", {
      method: "POST",
      headers: {
        Accept: "application/json, text/plain, */*",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email: email }),
    })
      .then((res) => res.json())
      .then(({ openGames, message }) => {
        console.log(openGames);
        setOpenGames(openGames);
      });
  };

  const joinGame = (event) => {
    event.preventDefault();
    fetch("game/join", {
      method: "POST",
      headers: {
        Accept: "application/json, text/plain, */*",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email: email, gameID: newGameID }),
    })
      .then((res) => res.json())
      .then(({ success, message }) => {
        if (success) {
          setGameID(newGameID);
          history.push("/gameplay");
        } else {
          alert(message);
        }
      });
  };

  const CreateNewGame = (event) => {
    event.preventDefault();
    history.push("/creategame");
  };

  return (
    <form>
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
      <input
        id="gameID"
        name="gameID"
        type="text"
        onChange={(event) => {
          setNewGameID(parseInt(event.target.value));
        }}
      />

      <button onClick={joinGame}>Request to join game</button>
      <p></p>

      <InputLabel id="label">Available Games for you!</InputLabel>
      <AvailableGamesSelector
        openGames={openGames}
        getGames={getGames}
        setNewGameID={setNewGameID}
        joinGame={joinGame}
      />

      <h1> Your Metrics</h1>
      <p>{response}</p>
    </form>
  );
};

export default DashBoard;
