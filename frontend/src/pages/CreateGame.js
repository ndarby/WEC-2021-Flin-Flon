import React, { useState } from "react";
import {InputLabel} from "@material-ui/core";
import Select from "@material-ui/core/Select";
import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import Switch from '@material-ui/core/Switch';
import {useAuth0} from "@auth0/auth0-react";

const CreateGame = () => {

    function setResponse(s) {
        
    }

    const { user } = useAuth0();
    const { email } = user;


  const [size, setSize] = React.useState(8);

  const [state, setState] = React.useState({
    checked: true
  });

  const handleChange = (event) => {
    setState({ ...state, [event.target.name]: event.target.checked });
  };

  const handleSubmit = (event) =>
  {
      fetch("create", {
      method: "POST",
      body: {email : email, color : state.checked ? "White" : "Black", size : size}
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setResponse(JSON.stringify(data));
      });
  }


  return(

  <form onSubmit={handleSubmit}>
      <header>
        <h1> Create Game</h1>
        <p>
          Enter the ID of the friend to play with and Size of the board
        </p>
      </header>

      <label> On for White, off for Black</label>
      <Switch
        checked={state.checked}
        onChange={handleChange}
        name="checkedA"
        inputProps={{ 'aria-label': 'secondary checkbox' }}
      />

      <label htmlFor="size"> size for the board!: </label>
      <input id="size" name="size" type="text" onChange={ (event) => setSize(event.target.value)} />

      <button onClick={handleSubmit}> Create new Game! </button>
      <p></p>

    </form>

 );
};



export default CreateGame;