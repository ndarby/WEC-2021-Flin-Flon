import React, { useState } from "react";
import DashBoard from "./pages/DashBoard";
import TopMenuBar from "./components/TopMenuBar";
import PageNotFound from "./pages/PageNotFound";
import Home from "./pages/Home";
import { Switch, Route } from "react-router-dom";
import { useAuth0 } from "@auth0/auth0-react";
import GamePlay from "./pages/GamePlay";
import ProtectedRoute from "./auth/protected-route";
import CreateGame from "./pages/CreateGame";

function App() {
  const { isAuthenticated } = useAuth0();
  const [gameID, setGameID] = useState(-1);

  return (
    <div className="App">
      <TopMenuBar />
      <Switch>
        <Route path="/" component={isAuthenticated ? DashBoard : Home} exact />
        <ProtectedRoute
          path="/gameplay"
          render={(props) => <GamePlay {...props} gameID={gameID} />}
        />
        <ProtectedRoute
          path="/gameplay"
          component={GamePlay}
          render={(props) => <GamePlay {...props} setGameID={setGameID} />}
        />
        <ProtectedRoute
          path="/creategame"
          render={(props) => <CreateGame {...props} setGameID={setGameID} />}
        />
        <Route component={PageNotFound} />
      </Switch>
    </div>
  );
}

export default App;
