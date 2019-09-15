import React, { Component } from "react";
import ImagesNoStatus from "./ImagesNoStatus";
import ImageCard from "./ImageCard";
import {getImages, deleteImage} from "../actions/imageActions.js";
import { connect} from 'react-redux';

class CardList extends Component {
  componentDidMount() {
    this.props.getImages();
  }

  render() {
    const { images } = this.props.image;
    console.log(images);
    return (
      <div>

      </div>
    );
  }
}

const mapStatetoProps = state => ({
  image: state.image
});

export default connect(
  mapStatetoProps,
  { getImages, deleteImage }
)(CardList);
