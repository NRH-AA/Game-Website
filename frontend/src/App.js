import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import './App.css';

import AllPlayersComponent from './components/players';

const ErrorPage = () => {
  return (
    <React.Fragment>
      <h2>Failed to load resource.</h2>
    </React.Fragment>
  );
};

const App = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route path='/players'>
          <AllPlayersComponent />
        </Route>
        
        <Route path='/'>
          <ErrorPage />
        </Route>
        
      </Switch>
    </BrowserRouter>
  );
}

export default App;
