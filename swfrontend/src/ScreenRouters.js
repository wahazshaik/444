import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import SCREENS from './screens/constants';
import BankMaster from './screens/BankMaster';
import PartyMaster from './screens/PartyMaster';
import PlantMaster from './screens/PlantMaster';
import LCDocumentType from './screens/LCDocumentTypeMaster';
import { route_url } from './AppConfigs';

const baseRoute = route_url.url === '/null' ? '' : route_url.url;
const withBaseRoute = (path) => `${baseRoute}${path.startsWith('/') ? '' : '/'}${path}`;

const modulePaths = (screen) => ({
  primary: withBaseRoute(screen.path),
  fallback: withBaseRoute(`/${screen.module}`),
});

const buildRoutes = (screen, Component, options = {}) => {
  const paths = modulePaths(screen);

  const baseRoutes = [
    <Route exact path={paths.primary} component={Component} key={paths.primary} />, 
    <Route exact path={paths.fallback} component={Component} key={paths.fallback} />, 
  ];

  if (options.redirectFromRoot) {
    baseRoutes.unshift(
      <Redirect
        exact
        from={baseRoute || '/'}
        to={paths.fallback}
        key="root-redirect"
      />,
    );
  }

  return baseRoutes;
};

const ScreenRouters = () => ({
  [SCREENS.BANK_MASTER.module]: {
    routers: buildRoutes(SCREENS.BANK_MASTER, BankMaster, { redirectFromRoot: true }),
  },
  [SCREENS.PARTY_MASTER.module]: {
    routers: buildRoutes(SCREENS.PARTY_MASTER, PartyMaster),
  },
  [SCREENS.PLANT_MASTER.module]: {
    routers: buildRoutes(SCREENS.PLANT_MASTER, PlantMaster),
  },
  [SCREENS.LC_DOCUMENT_TYPE.module]: {
    routers: buildRoutes(SCREENS.LC_DOCUMENT_TYPE, LCDocumentType),
  },
});

export default ScreenRouters;