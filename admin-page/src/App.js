import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import './App.css';


class App extends Component {

constructor(){
  super();

  this.state = {userEmail: '',ApiKey:''};
  this.handleChangeEmail = this.handleChangeEmail.bind(this);
  this.handleChangeKey = this.handleChangeKey.bind(this);
  this.handleSubmit = this.handleSubmit.bind(this);
}


componentDidMount(){
 
}


handleChangeEmail(event) {
  this.setState({userEmail: event.target.value});
 
}
handleChangeKey(event) {
  this.setState({ApiKey: event.target.value});
 
}
handleSubmit(event) {
  alert('USer email' + this.state.userEmail + " token " + this.state.ApiKey);
  event.preventDefault();
}
/*
fetch('https://bluej-pintro-project.appspot.com/users/activate/222dd22@wflefkn.com/', {
    method: 'PUT', 
   
    headers: {
      'Content-Type':'application/json', 'Accept': 'application/json',
      'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImRjMGMzNWZlYjBjODIzYjQyNzdkZDBhYjIwNDQzMDY5ZGYzMGZkZWEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYmx1ZWotcGludHJvLXByb2plY3QiLCJhdWQiOiJibHVlai1waW50cm8tcHJvamVjdCIsImF1dGhfdGltZSI6MTU4NjU5MzI0OCwidXNlcl9pZCI6IklDWnZxYWk5NTVVVkc2UmVxTkVWeHhCU2ZQbTEiLCJzdWIiOiJJQ1p2cWFpOTU1VVZHNlJlcU5FVnh4QlNmUG0xIiwiaWF0IjoxNTg2NTkzMjQ4LCJleHAiOjE1ODY1OTY4NDgsImVtYWlsIjoiZGpkbmRqZUBoZWJkaXIuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImRqZG5kamVAaGViZGlyLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.IVpCglonHcJsBtiDMjp_FdXOtfYaVnf1lpQInwV-u2liKhFSB_F6WGfaVYWBSKmJWRHdbhg4j0e5Er8ystKK1I-LiEp9l1DqA-UjtgNZT43TIdANh051_CAmr_TKTK_o8I38IS9ei8SosiJvKnOFzmSAzhCBjjHd0uXJo4prsIrDYWtHOqFlozQIt2oDpwvSy2LoZd4KB6XzBb-Vy_x9q4IDxMyaqylvl3vBh1Nr6X4nHmhFzUgvhNfH4vgp6AxvdDVi9pePraXbNg3M4MdmGbBCYIWkc-C24s_eMXWqvHD0Qh77e6PQHwZPx5qB40D0-m5tfSLeNLCmXXHaYMwCRA'
   
    },
    redirect: 'follow', // manual, *follow, error
  }).then(response => alert("??"))
  
   const response = await fetch(`https://api.coinmarketcap.com/v1/ticker/?limit=10`);
    const json = await response.json();
*/
  async blockUser(){
    try{



      
    const response = await fetch('/users/deactivate/'+this.state.userEmail, {
      method: 'PUT', 
      headers: {
        
        'Accept': 'application/json',
        'Authorization': 'Bearer '+this.state.ApiKey
      }, mode: "cors"
    })

    await response;
  }catch(err){
    alert("done " + err);

    }  }


    async activateUser(){
      try{
      const response = await fetch('/users/activate/'+this.state.userEmail, {
        method: 'PUT', 
        headers: {
          
          'Accept': 'application/json',
          'Authorization': 'Bearer '+this.state.ApiKey
        }, mode: "cors"
      })
  
      await response;
    }catch(err){
      alert("done " + err);
  
      }  }





      async LOGIN(){
          
        const response = await fetch('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyCZUeHC1zcLM__APOSB0dCXJkNPsOZuDKM', {
          
        method: 'POST', 
        headers: {

          'Accept': 'application/json'
        },body: JSON.stringify({
          "email":"admin@admin.test",
          "password":"fewfewf353n2l!",
          "returnSecureToken":true
        })

      })
  
      const daza = await response.json();
      const toke =  await daza.idToken
      return toke;
      
      }


      async getUser(){
        const key = await this.LOGIN();
        try{
        const response = await fetch('/users/'+this.state.userEmail, {
          method: 'GET', 
          headers: {
            
            'Accept': 'application/json',
            'Authorization': 'Bearer '+key
          }, mode: "cors"
        })
    
        const daza = await response.json();
        alert("Name = "+ daza.full_name + '\n' +
        "Email = "+ daza.email + '\n' +
        "help others = "+ daza.help_others + '\n' +
        "Passions = "+ daza.passions + '\n' + 
        "Phone = "+ daza.phone_number + '\n' +
        "Previous Company = "+ daza.previous_Company + '\n' +
        "Story = "+ daza.story + '\n' +
        "Active  = "+ daza.active);
      }catch(err){
        alert("done " + err);
    
        }  }
  


        
        
        


  render(){

   
     

    return (



  <div className="App">
 <div className="Options" style={{    display: "flex",
  justifyContent: "center",
  alignItems: "center",
  flexDirection:'column',
  height:100,
  backgroundColor:'#1B1B1B'}}>
<h1 style={{color:'white',fontFamily:'Helvetica'}}>Pintro Admin Page</h1>
</div>
<div className="App" style={{     
    display: "flex",
  justifyContent:'center',
  alignItems: "center",
  backgroundColor: "#F1F2EF",
  flexDirection:'column',
  height:'100%'
  }}>
   
    <div className="in" style={{margin:10}}>
  <h2>User Details</h2>
        <label>
          User Email:
          <input type="text"  style={{borderRadius:7, height:25, width:140}} value={this.state.userEmail} onChange={this.handleChangeEmail} />
        </label>
        </div> 
        <div>
    </div> 
 
 
 <div className="buttons" style = {{flexDirection:'row',margin:10}}>
  <Button variant="contained" color="secondary" onClick={() => this.blockUser()}>
  Deactivate
</Button>

<Button style={{margin:10}} variant="contained" color="primary" onClick={() => this.activateUser()}>
  Activate
</Button>

<Button style={{margin:10}} variant="contained" color="primary" onClick={() => this.getUser()}>
  Get User
</Button>
</div>

      </div>       
  </div>
  );
  }
    
}
export default App;
