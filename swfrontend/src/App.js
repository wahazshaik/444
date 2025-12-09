import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import MDMApp from 'swfrontend/MDMApp';
import { localStorageVariableName } from 'swfrontend/AppConfigs';
import LoginPage from 'swfrontend/LOGIN/LoginPage';
import ScreenRouters from './ScreenRouters';
import './App.css';

const App = () => {
  const authToken = localStorage.getItem(localStorageVariableName.authToken);

  return (
    authToken == null ? (
      <LoginPage />
    ) : (
      <BrowserRouter>
        <MDMApp routes={ScreenRouters} />
      </BrowserRouter>
    )
  );
};

export default App;