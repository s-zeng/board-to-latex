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
