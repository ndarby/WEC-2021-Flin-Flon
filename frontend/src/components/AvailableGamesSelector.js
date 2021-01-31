import React from "react";
import { MenuItem, Select } from "@material-ui/core";

const AvailableGamesSelector = ({
  openGames,
  getGames,
  joinGame,
  setNewGameID,
}) => {
  return (
    <Select labelId="label" id="select" value="20" onClick={getGames}>
      {openGames.map((gameID) => (
        <MenuItem
          key={gameID}
          value={gameID}
          onClick={(event) => {
            event.preventDefault();
            setNewGameID(event.target.value);
            joinGame();
          }}
        >
          {gameID}
        </MenuItem>
      ))}
    </Select>
  );
};

export default AvailableGamesSelector;
