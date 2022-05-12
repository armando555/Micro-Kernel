import React, { Component } from "react"
import { w3cwebsocket as W3CWebSocket } from "websocket";



const client = new W3CWebSocket('ws://127.0.0.1:7777');



class App extends Component {

  constructor(){
    super();
    this.state = {
      logs:[],
      btnDirectorio: false,
      directorio: "",
      btnArchivo: false,
      archivo:"",
      styleSheet: {
        btnCrearDirectorio :{
          margin: "2vh"
        }
      }
    }
  }


  componentWillMount() {
    client.onopen = () => {
      console.log('WebSocket Client Connected');
    };
    client.onmessage = (message) => {

      console.log(message.data);
    };
    client.addEventListener('message', (event)=>{
      this.setState({logs: [...this.state.logs,event.data]})
      
    })
    
  }

  


  render() {
  
    return (
      <div style={{
        display: "flex",
        flexDirection: "column",
        alignContent:"center",
        alignItems:"center",

      }}>
        <button style={this.state.styleSheet.btnCrearDirectorio} onClick={() => {
          this.setState({btnDirectorio: !this.state.btnDirectorio})
          
        }}>{this.state.btnDirectorio ? <>Cerrar</> :<>Crear directorio</>}</button>
        {this.state.btnDirectorio ? (
          <div>
            <input placeholder="Nombre" value={this.state.directorio} onChange= {(e)=>{(this.setState({directorio:e.target.value}))}}></input>
            <button onClick={() =>{
              const data = {
                cmd: "1",
                msg: this.state.directorio,
                scr: "gui-user",
                dst: "file_manager",
              }
              client.send(JSON.stringify(data))              
            }}>Crear</button>

            


          </div>
        ):<></>}


        <button style={this.state.styleSheet.btnCrearDirectorio} onClick={()=>{
          this.setState({btnArchivo: !this.state.btnArchivo})
        }}>
          crear Archiivo
        </button>

        {this.state.btnArchivo ? (
          <div>
            <input placeholder="Nombre" value={this.state.archivo} onChange= {(e)=>{(this.setState({archivo:e.target.value}))}}></input>
            <button onClick={() =>{
              const data = {
                cmd: "2",
                msg: this.state.archivo,
                scr: "gui-user",
                dst: "file_manager",
              }
              console.log(data)
              client.send(JSON.stringify(data))              
            }}>Crear</button>


          </div>
        ):<></>}

        <ul>
        
        {
          this.state.logs?.map(item => <li>{item}</li>)
        }

        </ul>

      </div>
    );
  }


}

export default App;
