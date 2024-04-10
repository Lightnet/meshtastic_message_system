/*
  Project Name:
  License: MIT
  Created By Lightnet
  Type: Javascript Module
*/

//import van from 'vanjs-core';
//import van from 'van';
import { Router
  //, Link, getRouterParams, navigate 
} from "vanjs-routing";

import HomePage from './pages/home.js';
import AboutPage from "./pages/about.js";
import { SignInPage, SignOutPage, SignUpPage } from "./pages/auth.js";

function App() {
  return Router({
    //basename: "", // Optional base name (All links are now prefixed with '/vanjs-routing')
    routes: [
      { path: "/", component: HomePage },
      { path: "/about", component: AboutPage },
      //AUTH
      { path: "/signup", component: SignUpPage },
      { path: "/signin", component: SignInPage },
      { path: "/signout", component: SignOutPage },
      //{ path: "/forgot", component: ElForgot },
      //account
      //{ path: "/account", component: AccountPage },
    ]
  });
}

export default App;