import React from "react";
import "./chessboard.css";

const Board = ({ size }) => {
  let range = [];
  for (let i = 0; i < size; i++) {
    range.push(i);
  }

  return (
    <table>
      {range.map((i) => (
        <tr>
          {range.map((j) => (
            <td />
          ))}
        </tr>
      ))}
    </table>
  );
};

export default Board;
