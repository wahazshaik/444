export let MASTER_DATA_SERVER = {
    PROTOCOL: process.env.REACT_APP_SERVER_PROTOCOL,
    SERVER_URL: process.env.REACT_APP_SERVER_URL, // REST API IP HOST
    PORT: process.env.REACT_APP_SERVER_PORT, // REST API IP PORT
    API_PREFIX: process.env.REACT_APP_API_PREFIX,
    MASTER_ROUTE: process.env.REACT_APP_API_MASTER_ROUTE,
};
 
export let MASTER_URL = `http://${MASTER_DATA_SERVER.SERVER_URL}:${MASTER_DATA_SERVER.PORT}/`;
export let RBAC_DATA_SERVER = MASTER_URL + "rbac/";
 
/* App name details */
export let APP_NAME = {
    MASTER: process.env.REACT_APP_API_NAME,
};
 
/* App title name */
export let settings = {
    appTitle: window.innerWidth>500
    ? process.env.REACT_APP_PROJECT_NAME
    : process.env.REACT_APP_PROJECT_SHORT_NAME,
    quickForm: process.env.REACT_APP_ENABLE_QUICK_FORM
};
 
/* Route URL */
export let route_url = {"url": process.env.REACT_APP_PROJECT_ROUTE==="/null"?"":process.env.REACT_APP_PROJECT_ROUTE};
 
/* Grid view config */
export let gridViewConfig = {
    paginationPageSize: process.env.REACT_APP_DEFAULT_PAGINATION_SIZE
};
 
/* Api call details */
export const apiCall = {
    screenRootOptionCall: "?set=appmeta",
    login: "login/",
};
export const ColumnFilter = "view_columnfilter";
 
/* Screen root notification details */
export let screenRootNotificationData = {
    messageType: "error",
    messageTitle: "API",
    message: "Cannot Make API connection"
};
 
/* Local storage variable name */
export let localStorageVariableName = {
    authToken: `${process.env.REACT_APP_TOKEN_PREFIX}-auth-token`,
    guestAuthToken: "guest-auth-token",
    userName: `${process.env.REACT_APP_TOKEN_PREFIX}-user-name`,
    pendingSave : 'user_inputs_save_pending',
    isLoggedIn : 'isLoggedIn',
    isStaff : 'is_staff',
    showNotificationDrawer: 'show_notification_drawer',
};
 
/* Navlink Active Style details */
export let navlinkActivteStyle = {
    background: "#DB4040",
    color: "white"
};
 
export let restrictFields = {
    created_by: 'created_by',
    created_date: 'created_date',
    last_updated_by: 'last_updated_by',
    last_updated_date: 'last_updated_date',
};