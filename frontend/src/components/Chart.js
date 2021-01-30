import React from "react";
import {
  VictoryChart,
  VictoryTheme,
  VictoryScatter,
  VictoryLabel,
} from "victory";

const Chart = ({ data }) => {
  return (
    <VictoryChart
      theme={VictoryTheme.material}
      domainPadding={10}
      animate={{ duration: 100 }}
    >
      <VictoryScatter
        data={data.map((datum, i) => ({ ...datum, number: i + 1 }))}
        maxBubbleSize={20}
        minBubbleSize={10}
        labels={(datum) => datum.number}
        labelComponent={<VictoryLabel dy={8} />}
        style={{ labels: { fill: "white", fontSize: 18 } }}
        animate={{
          onExit: {
            duration: 500,
            before: () => ({ fill: "orange", _x: 0, _y: 0 }),
          },
          onEnter: {
            duration: 500,
          },
        }}
      />
    </VictoryChart>
  );
};

export default Chart;
