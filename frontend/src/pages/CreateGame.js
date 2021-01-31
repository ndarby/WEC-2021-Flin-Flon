import React, { useState } from "react";
import Switch from "@material-ui/core/Switch";
import { useAuth0 } from "@auth0/auth0-react";
import { useHistory } from "react-router-dom";

const CreateGame = ({ setGameID }) => {
  const history = useHistory();

  const { user } = useAuth0();
  const { email } = user;

  const [size, setSize] = React.useState(8);

  const [state, setState] = React.useState({
    checked: true,
  });

  const handleChange = (event) => {
    setState({ ...state, [event.target.name]: event.target.checked });
  };

  const handleSubmit = (event) => {
    fetch("game/create", {
      method: "POST",
      headers: {
        Accept: "application/json, text/plain, */*",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: email,
        color: state.checked ? "White" : "Black",
        size: size,
      }),
    })
      .then((res) => res.json())
      .then(({ gameID, success, message }) => {
        if (success) {
          setGameID(gameID);
          history.push("/gameplay");
        } else {
          alert(message);
        }
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <header>
        <h1> Create Game</h1>
        <p>Enter the ID of the friend to play with and size of the board</p>
      </header>

      <label> On for White, off for Black</label>
      <Switch
        checked={state.checked}
        onChange={handleChange}
        name="checkedA"
        inputProps={{ "aria-label": "secondary checkbox" }}
      />

      <label htmlFor="size"> size for the board!: </label>
      <input
        id="size"
        name="size"
        type="text"
        onChange={(event) => setSize(parseInt(event.target.value))}
      />

      <button onClick={handleSubmit}> Create new Game! </button>
      <p></p>
    </form>
  );
};

export default CreateGame;
