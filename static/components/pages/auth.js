
import van from 'vanjs-core';
import SignIn from "../auth/signin.js";
import SignOut from "../auth/signout.js";
import SignUp from "../auth/signup.js";
import { NavMenu } from "../navmenu.js";
const {div, button } = van.tags;

function SignInPage(){
  return div(
    NavMenu(),
    SignIn()
  )
}

function SignOutPage(){
  return div(
    NavMenu(),
    SignOut()
  )
}

function SignUpPage(){
  return div(
    NavMenu(),
    SignUp()
  )
}

export {
  SignInPage,
  SignOutPage,
  SignUpPage,
}