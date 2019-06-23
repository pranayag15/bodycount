import React, { Component } from "react";
import './App.css'
import Chart from './chart'
import axios from 'axios'

// import '../style/graph.css'

class App extends Component {
  state = {
    data:[]
  }
  componentDidMount(){
    axios({
      method: 'get',
      url: 'http://localhost:8080/allperson',
  })
      .then(function (response) {
          console.log(response.data);
          this.setState({
            data:response.data
          })
          
      }.bind(this))
      .catch(function (error) {
          console.log(error);
      });
  }
  render() {
    return (
      <div className="container-fluid">
        <div class="row">
          <div class="col-12">
            {this.state.data.length!=0 && <Chart data={this.state.data}></Chart>}
          </div>
        </div>
      </div>
    
    )
  }
}

export default App;
