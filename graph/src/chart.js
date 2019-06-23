import React, { Component } from "react";
import {
  LineChart, Line, XAxis ,ResponsiveContainer, YAxis, CartesianGrid, Tooltip, Legend,
} from 'recharts';

// import '../style/graph.css'

class Chart extends Component {
  state = {
    data: []
  }
  componentDidMount() {
    console.log(this.props.data)
  }
  componentDidMount() {
    this.timerID = setInterval(
      () => this.tick(),
      1000
    );
  }

  tick() {
    this.setState({
      data: this.props.data
    })
  }
  render() {
    return (
        <LineChart
          width={600}
          height={500}
          data={this.props.data}
          margin={{
            top: 5, right: 30, left: 20, bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="person_detected" stroke="#8884d8" activeDot={{ r: 8 }} />
          {/* <Line type="monotone" dataKey="M" stroke="#82ca9d" /> */}
        </LineChart>
    
    )
  }
}

export default Chart;