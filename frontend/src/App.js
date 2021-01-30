import React, { useEffect } from "react";
import Form from "./components/Form";
import TopMenuBar from "./components/TopMenuBar";
import FileUpload from "./components/FileUpload";
import PageNotFound from "./components/PageNotFound";
import Home from "./components/Home";
import FileDownload from "./components/FileDownload";
import DataVisualization from "./components/DataVisualization";
import { Switch, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <TopMenuBar />
      <Switch>
        <Route path="/form" component={Form} />
        <Route path="/file" component={FileUpload} />
        <Route path="/download" component={FileDownload} />
        <Route path="/data" component={DataVisualization} />
        <Route path="/" component={Home} exact />
        <Route component={PageNotFound} />
      </Switch>
    </div>
  );
}

export default App;
