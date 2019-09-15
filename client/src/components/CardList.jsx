import React, { Component } from "react";
import {PropTypes} from "prop-types";
import ImagesNoStatus from "./ImagesNoStatus";
import ImageCard from "./ImageCard";
import {
  getImages,
  deleteImage
} from "../actions/imageActions.js";
import {
  login,
  register
} from "../actions/loginActions.js";
import { connect } from "react-redux";

class CardList extends Component {
  componentDidMount() {
    this.props.register();
    this.props.login();
    this.props.getImages();
  }

  render() {
   // const { images } = this.props.image;
  //  console.log(images);
    return <div></div>;
  }
}

CardList.propTypes = {
    getImages: PropTypes.func.isRequired,
    image: PropTypes.object.isRequired,
    body: PropTypes.object.isRequired,
    info: PropTypes.object.isRequired
  };

const mapStatetoProps = state => ({
  info: state.info,
  body: state.body,
  image: state.image
});

export default connect(
  mapStatetoProps,
  { register, login, getImages, deleteImage }
)(CardList);
