import React from 'react';
import AppNavbar from "./components/AppNavbar.jsx";
import Editor from "./components/Editor.jsx";
import ImageCard from "./components/ImageCard.jsx";
import ImagesNoStatus from './components/ImagesNoStatus.jsx';
import FilenameStatus from './components/FilenameStatus.jsx';

function App() {
  return (
    <div className="App">
      <AppNavbar />
      <ImagesNoStatus numberofimages={10} />
      <ImageCard image={"/bglock.jpg"} label={"tag"} />
      <Editor />
      <FilenameStatus filename={"filename"} />
    </div>
  );
}

export default App;