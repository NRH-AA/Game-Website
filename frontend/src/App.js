import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import './App.css';

import CreateAccountComponent from './components/users/CreateAccount';
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
      <Route path='/create'>
          <CreateAccountComponent />
        </Route>
        
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
