import React, {Component} from "react";
import AppNavbar from "./components/AppNavbar.jsx";
import Editor from "./components/Editor.jsx";
import CardList from "./components/CardList.jsx";
import ImagesNoStatus from "./components/ImagesNoStatus.jsx";
import FilenameStatus from "./components/FilenameStatus.jsx";
import store from "./store";
import {Provider } from "react-redux";

class App extends Component {
  render() {
    const request = require('request')

// Register
request.post('http://localhost:5000/api/register',
			{form:{username: 'redside100', password: 'lmaoyeet'}},
			function(err, httpres, body){
				console.log(body);
			});

var token = "";
var uuid = "";
// Login
request.post('http://localhost:5000/api/login', {form:{username: 'redside100', password: 'lmaoyeet'}},
function(err, httpres, body){
	console.log(body);
	var info = JSON.parse(body);
	token = info['token'];
	uuid = info['uuid'];
	console.log(token);
	console.log(uuid);
});


// Post image

  return (
    <Provider store={store}>
      <div className="App">
        <AppNavbar />
        <ImagesNoStatus numberofimages={10} />
        <CardList />
        <Editor />
        <FilenameStatus filename={"filename"} />
      </div>
    </Provider>
  );
  }
}

export default App;
