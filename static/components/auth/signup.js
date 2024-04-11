

import van from 'van';

const { div, button, input, label, table, tbody, tr, td } = van.tags;

function SignUp(){

  const alias = van.state('test');
  const passphrase1 = van.state('pass');
  const passphrase2 = van.state('');

  async function btnsign(){
    const resp = await fetch('/api/auth/signup',{
      method:'POST',
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify({
        alias:alias.val,
        passphrase:passphrase1.val
      })
    })
    const data = await resp.json();
    console.log(data)
  }
  
  return div(
    table(
      tbody(
        tr(
          td(
            label(' Alias: ')
          ),
          td(
            input({value:alias,oninput:e=>alias.val=e.target.value})
          ),
        ),
        tr(
          td(
            label(' Passphrase #1: ')
          ),
          td(
            input({value:passphrase1,oninput:e=>passphrase1.val=e.target.value})
          ),
        ),
        tr(
          td(
            label(' Passphrase #2: ')
          ),
          td(
            input({value:passphrase2,oninput:e=>passphrase2.val=e.target.value})
          ),
        ),
        tr(
          td({colspan:"2"},
            button({onclick:btnsign},'Register'),
            button({onclick:btnsign},'Cancel')
          )
        ),
        
      )
    )
  )

}

export default SignUp;
