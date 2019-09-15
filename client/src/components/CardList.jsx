import React, { Component } from "react";
import {PropTypes} from "prop-types";
import Button from '@material-ui/core/Button';
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
    // this.props.register();
    // this.props.login();
    // this.props.getImages();
  }

  render() {
   // const { images } = this.props.image;
    console.log(this.props);
    return <div>
      <Button onClick={this.props.register}>Register</Button>
      <Button onClick={this.props.login}>Login</Button>
      <Button onClick={()=>{this.props.getImages(this.props.info)}}>Get Images</Button>
    </div>;
  }
}

CardList.propTypes = {
    getImages: PropTypes.func.isRequired,
};

const mapStatetoProps = (state) => {
  let ret = {
    info: state.loginReducer.info,
    body: state.loginReducer.body,
    image: state.imageReducer.image
  }
  return ret;
}
// => ({
//   info: state.info,
//   body: state.body,
//   image: state.image
// });

export default connect(
  mapStatetoProps,
  { register, login, getImages, deleteImage }
)(CardList);
