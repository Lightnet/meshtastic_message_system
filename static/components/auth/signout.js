

import van from 'vanjs-core';
import { Router, Link, getRouterParams, navigate } from "vanjs-routing";

const { div, button, input, label, table, tbody, tr, td } = van.tags;

function SignOut(){

  return div(
    label("Are you sure you logout?"),
    button({onclick:()=>navigate("/")},'Okay'),
    button({onclick:()=>navigate("/")},' Back '),
  )
}

export default SignOut;
