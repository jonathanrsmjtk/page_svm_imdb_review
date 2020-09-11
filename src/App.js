import React, { Component}  from 'react';
import {InputTextarea} from 'primereact/inputtextarea';
import './App.css';
import './style/style.css'
import 'primereact/resources/themes/saga-green/theme.css';
import 'primereact/resources/primereact.min.css';
import { Button } from 'primereact/button';
import axios from 'axios';

class Post extends Component {
  constructor(props){
    super(props);
    this.initialState = {
      header : {
        data : ''
      },
      result : {
        data: '',
        sentiment : ''
      },
      textValue : '',
    };
    this.state = this.initialState

  }

  handleChange = event => {
    const { name, value } = event.target;

    const newHeader = { ...this.state.header };
    newHeader[name] = value;

    this.setState({
        header: newHeader
    });
    console.log(newHeader);
}

  onPress = () => {
      if(this.state.header.data === ''){
        this.setState({textValue: 'Enter the text first!'});
      }
      else{
      this.setState({textValue: this.state.result.sentiment});
      console.log("RES");
      console.log(this.state.textValue);
      }
    
  }

  postData = inputForm => {
    console.log("Done");
    var data = this.state.header.data;
    let post = null;
    console.log(this.state.header.data)
    axios.post('http://localhost:8000/tweets/classify', {
      data: data
    }).then(response => {
      console.log("Success");
      console.log(response.data);
      post = response.data;
      this.state.result.sentiment = response.data.sentiment;
      console.log(this.state.result.sentiment);
      this.onPress();
    }).catch(err => {
      console.log(err);
    })
  }

  render(){
    return (
      <div className="App">
        <header className="App-header">
        
        <label className='label'>MOVIE REVIEW SENTIMENT ANALYZER</label>
        
        <div className="p-grid p-align-end vertical-container">
        
          <div className="p-fluid">
        
          <div className="p-field">
              <InputTextarea className="inputs" 
              name="data"
              value = {this.state.header.data}
              placeholder='Enter text' 
              rows={5} 
              cols={30} 
              onInput={this.handleChange.bind(this)} 
              onChange = {this.handleChange}
              />
          </div>
          <div className="p-field">
              <Button className="enter"  label="Click to Classify" onClick={() => {
                this.postData(); 
                }}/>
          </div>
        
          </div>

        </div>
  
        <label className="result">{this.state.textValue}</label>
  
        </header>
      </div>
    );
  }
} 

function App() {
  return(
    <div>
      <Post />
    </div>
  )
}

export default App;
