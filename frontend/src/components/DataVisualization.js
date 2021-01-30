import React, { useEffect, useState } from "react";
import { Grid, Paper } from "@material-ui/core";
import Chart from "./Chart";

const DataVisualization = () => {
  const getNewDatum = async () => {
    const response = await fetch(
      "https://random-data-api.com/api/number/random_number"
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const number = await response.json();
    return { x: number.decimal, y: number.normal, z: number.digit + 1 };
  };

  const [data, setData] = useState([]);

  useEffect(() => {
    const initialize = async () => {
      setData([await getNewDatum(), await getNewDatum(), await getNewDatum()]);
    };
    initialize().catch(() => {});
  }, []);

  const getMoreData = async () => {
    setData([...data.slice(-19), await getNewDatum()]);
  };

  return (
    <Grid
      container
      direction="column"
      justify="center"
      alignItems="center"
      spacing={3}
    >
      <Grid item xs={2} />
      <Grid
        container
        item
        direction="row"
        justify="center"
        alignItems="center"
        spacing={3}
        xs={8}
      >
        <Grid item xs={1} s={2} />
        <Grid item xs={10} s={8}>
          <Paper>
            <Chart data={data} />
          </Paper>
        </Grid>
        <Grid item xs={1} s={2} />
      </Grid>

      <Grid item xs={2}>
        <button onClick={getMoreData}>Get more data</button>
      </Grid>
    </Grid>
  );
};

export default DataVisualization;
