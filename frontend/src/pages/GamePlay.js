import React, { useEffect, useState } from "react";
import Board from "../chessboard/Board";
import { useAuth0 } from "@auth0/auth0-react";
import { Button } from "@material-ui/core";
import { useHistory } from "react-router-dom";

const pieceLookup = {
  p: "Pawn",
  b: "Bishop",
  k: "Knight",
  K: "King",
  q: "Queen",
  r: "Rook",
  v: "Vanguard",
};

const GamePlay = ({ gameID }) => {
  const history = useHistory();
  const [size, setSize] = useState(8);
  const [color, setColor] = useState("");
  const [pieces, setPieces] = useState([]);

  const [IDArray, setIDArray] = useState([]);

  const { user } = useAuth0();
  const { email } = user;

  const getImageSource = (name) => {
    const colour = name[0] === "b" ? "Black" : "White";
    const type = pieceLookup[name[1]];
    return `${colour}_${type}`;
  };

  const setState = async () => {
    const response = await fetch("game/currentstate", {
      method: "POST",
      headers: {
        Accept: "application/json, text/plain, */*",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ gameID: gameID, email: email }),
    });
    if (!response.ok) {
      throw new Error("bad network response");
    }
    const { board } = await response.json();

    let piecesCopy = pieces.slice();
    let IDArrayCopy = IDArray.slice();
    const insertPiece = ({ location, name, pieceID }) => {
      piecesCopy[location[0]][location[1]] = getImageSource(name);
      IDArrayCopy[location[0]][location[1]] = pieceID;
    };
    board.myPieces.forEach(insertPiece);
    board.oppPieces.forEach(insertPiece);
  };

  const makeMove = async (ID, location) => {
    const response = await fetch("game/makemove", {
      method: "POST",
      headers: {
        Accept: "application/json, text/plain, */*",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        gameID: gameID,
        email: email,
        pieceID: ID,
        location: location,
      }),
    });
    const { move, reason } = await response.json();
    if (!move) {
      alert(reason);
    } else {
      await setState();
    }
  };

  useEffect(() => {
    const setup = async () => {
      const response = await fetch("game/currentstate", {
        method: "POST",
        headers: {
          Accept: "application/json, text/plain, */*",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ gameID: gameID, email: email }),
      });
      if (!response.ok) {
        throw new Error("bad network response");
      }
      const { board } = await response.json();
      setSize(board.size);
      setColor(board.myColor);
      let newPiecesArray = [];
      let newBoardArray = [];
      for (let i = 0; i < size; i++) {
        let piecesRow = [];
        let boardRow = [];
        for (let j = 0; j < size; j++) {
          piecesRow.push("");
          boardRow.push(-1);
        }
        newPiecesArray.push(piecesRow);
        newBoardArray.push(boardRow);
      }
      setPieces(newPiecesArray);
      setIDArray(newBoardArray);
    };
    setup();
    setState();
  }, []);

  const handleResign = () => {
    fetch("game/resign", {
      method: "POST",
      headers: {
        Accept: "application/json, text/plain, */*",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ gameID: gameID, email: email }),
    })
      .then((response) => response.json())
      .then(({ success }) => {
        if (success) {
          history.push("/");
        }
      });
  };

  return (
    <div>
      <Board
        size={size}
        pieces={pieces}
        IDArray={IDArray}
        makeMove={makeMove()}
      />
      <Button variant="contained" onClick={handleResign}>
        Resign
      </Button>
    </div>
  );
};

export default GamePlay;
