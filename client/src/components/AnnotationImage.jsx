import React from "react";
import { Image } from "react-konva";

class AnnotationImage extends React.Component {
  state = {
    image: null
  };
  componentDidMount() {
    const image = new window.Image();
    image.src = this.props.src;
    image.onload = () => {
      this.setState({
        image
      });
    };
  }

  render() {
    const {
      state: { image }
    } = this;
    return <Image image={image} zIndex={0} />;
  }
}
export default AnnotationImage;
