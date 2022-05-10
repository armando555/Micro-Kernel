import React, { Component } from "react"
import { w3cwebsocket as W3CWebSocket } from "websocket";



const client = new W3CWebSocket('ws://127.0.0.1:7777');



class App extends Component {

  constructor(){
    super();
    this.state = {
      btnDirectorio: false,
      directorio: ""
    }
  }


  componentWillMount() {
    client.onopen = () => {
      console.log('WebSocket Client Connected');
    };
    client.onmessage = (message) => {
      console.log(message);
    };
  }

  render() {
    return (
      <div style={{
        display: "flex",
        flexDirection: "column",
        alignContent:"center",
        alignItems:"center"
      }}>
        <button onClick={() => {
          this.setState({btnDirectorio: !this.state.btnDirectorio})
          
        }}>{this.state.btnDirectorio ? <>Cerrar</> :<>Crear directorio</>}</button>
        {this.state.btnDirectorio ? (
          <div>
            <input placeholder="Nombre" value={this.state.directorio} onChange= {(e)=>{(this.setState({directorio:e.target.value}))}}></input>
            <button onClick={() =>{
              const data = {
                cmd: "1",
                msg: this.state.directorio,
                scr: "abueno2",
                dst: "destino :V"
              }
              console.log(data)
              client.send(JSON.stringify(data))
              
            }}>Crear</button>
          </div>
        ):<></>}


        <button>
          crear Archiivo
        </button>
      </div>
    );
  }


}

export default App;
