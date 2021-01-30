import React from "react";
import "./chessboard.css";

const Board = ({ size, pieces }) => {
  let range = [];
  for (let i = 0; i < size; i++) {
    range.push(i);
  }

  return (
    <table>
      {range.map((i) => (
        <tr>
          {range.map((j) => (
            <td>
              {pieces[i][j] && (
                <img
                  src={`/chess_pieces/${pieces[i][j]}.svg`}
                  alt="image source cannot be found"
                />
              )}
            </td>
          ))}
        </tr>
      ))}
    </table>
  );
};

export default Board;
