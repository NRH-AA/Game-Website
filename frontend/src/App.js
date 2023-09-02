import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from "react-redux";
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import './App.css';

import CreateAccountComponent from './components/users/CreateAccount';
import AllPlayersComponent from './components/players';
import HomeComponent from './components/home';

const ErrorPage = () => {
  return (
    <React.Fragment>
      <h2>Failed to load resource.</h2>
    </React.Fragment>
  );
};

const App = () => {
  const dispatch = useDispatch();
  const sessionUser = useSelector(state => state.session.user);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    if (!loaded) dispatch(authenticate()).then(() => setLoaded(true));
  }, [loaded, sessionUser])

  return (
    <BrowserRouter>
      <Switch>
        <Route path='/create'>
          <CreateAccountComponent />
        </Route>
        
        <Route path='/players'>
          <AllPlayersComponent />
        </Route>

        <Route exact path='/'>
          <HomeComponent />
        </Route>
        
        <Route path='/'>
          <ErrorPage />
        </Route>
        
      </Switch>
    </BrowserRouter>
  );
}

export default App;
