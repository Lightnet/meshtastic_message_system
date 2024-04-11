

import van from 'van';

const { div, button, input, label, table, tbody, tr, td } = van.tags;

function SignIn(){


  const alias = van.state('test');
  const passphrase = van.state('pass');

  async function btnsign(){
    const resp = await fetch('/api/auth/signin',{
      method:'POST',
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify({
        alias:alias.val,
        passphrase:passphrase.val
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
            label(' Passphrase: ')
          ),
          td(
            input({value:passphrase,oninput:e=>passphrase.val=e.target.value})
          ),
        ),
        tr(
          td({colspan:"2"},
            button({onclick:btnsign},'Login'),
            button({onclick:btnsign},'Cancel')
          )
        ),
        
      )
    )
  )
}

export default SignIn;
