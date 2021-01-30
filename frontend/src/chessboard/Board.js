import React, { useState } from "react";
import "./chessboard.css";

const Board = ({ size, pieces, IDArray, makeMove }) => {
  let range = [];
  for (let i = 0; i < size; i++) {
    range.push(i);
  }

  const [selectedPiece, setSelectedPiece] = useState({
    position: [-1, -1],
    ID: -1,
  });

  const handleClick = async (position, ID) => {
    if (selectedPiece.ID === -1 && ID !== -1) {
      setSelectedPiece({ position: position, ID: ID });
    } else if (selectedPiece.ID !== -1 && ID === -1) {
      await makeMove(ID, position);
    }
  };

  return (
    <table>
      {range.map((i) => (
        <tr>
          {range.map((j) => (
            <td>
              <div onClick={() => handleClick([i][j], IDArray[i][j])}>
                {pieces[i][j] && (
                  <img
                    src={`/chess_pieces/${pieces[i][j]}.svg`}
                    alt="image source cannot be found"
                  />
                )}
              </div>
            </td>
          ))}
        </tr>
      ))}
    </table>
  );
};

export default Board;
