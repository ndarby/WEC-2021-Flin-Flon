import React from "react";
import { MenuItem, Select } from "@material-ui/core";

const AvailableGamesSelector = ({
  openGames,
  getGames,
  joinGame,
  setNewGameID,
}) => {
  return (
    <Select
      labelId="label"
      id="select"
      value="20"
      onClick={getGames}
      onChange={(event) => {
        setNewGameID(event.target.value);
        joinGame();
      }}
    >
      {openGames.map((gameID) => (
        <MenuItem key={gameID} value={gameID}>
          {gameID}
        </MenuItem>
      ))}
    </Select>
  );
};

export default AvailableGamesSelector;
