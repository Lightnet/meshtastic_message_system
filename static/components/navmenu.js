
import van from 'vanjs-core';
import { Router, Link, getRouterParams, navigate } from "vanjs-routing";

const {div, button } = van.tags;

function NavMenu(){

  return div(
    button({onclick:()=>navigate("/")},' Home '),
    button({onclick:()=>navigate("/about",{replace:true})},' About '),
    button({onclick:()=>navigate("/signin",{replace:true})},' Sign In '),
    button({onclick:()=>navigate("/signup",{replace:true})},' Sign Up'),
    button({onclick:()=>navigate("/signout",{replace:true})},' Sign Out'),
    button({onclick:()=>navigate("/account",{replace:true})},' Account '),
  )

}

export {
  NavMenu
}