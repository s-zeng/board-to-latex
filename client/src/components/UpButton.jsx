import React, { Component, Children } from "react";
import Modal from "@material-ui/core/Modal";
import PropTypes from "prop-types";
import Button from "@material-ui/core/Button";
import IconButton from "@material-ui/core/IconButton";
import MessageIcon from "@material-ui/icons/Message";
import AnnotationImage from "./AnnotationImage";
import { Stage, Layer } from "react-konva";
import Rectangle from "./Rectangle/Rectangle";
import RectTransformer from "./Rectangle/RectTransformer";
import uuid from "uuid";
import { postImage } from "../actions/imageActions";
import { connect } from "react-redux";

class Upload extends React.Component {
  state = {
    file: null,
    filename: null,
    rectangles: [],
    rectCount: 0,
    selectedShapeName: "",
    mouseDown: false,
    mouseDraw: false,
    newRectX: 0,
    newRectY: 0
  };
  constructor(props) {
    super(props);
    this.prevProps = this.props;
    this.handleChange = this.handleChange.bind(this);
  }

  // File Upload
  handleChange = (event) =>{
    this.setState({
      file: URL.createObjectURL(event.target.files[0]),
      filename: event.target.files[0].name
    });
  }

  handleClose = () => {
    this.setState({
      open: false
    });
  };

  handleClick = () => {
    this.setState({
      open: true
    });
  };

  // Bounding Box
  handleStageMouseDown = event => {
    const { rectangles } = this.state;
    // clicked on stage - clear selection or ready to generate new rectangle
    if (event.target.className === "Image") {
      const stage = event.target.getStage();
      const mousePos = stage.getPointerPosition();
      this.setState({
        mouseDown: true,
        newRectX: mousePos.x,
        newRectY: mousePos.y,
        selectedShapeName: ""
      });
      return;
    }
    // clicked on transformer - do nothing
    const clickedOnTransformer =
      event.target.getParent().className === "Transformer";
    if (clickedOnTransformer) {
      return;
    }

    // find clicked rect by its name
    const name = event.target.name();
    const rect = rectangles.find(r => r.name === name);
    if (rect) {
      this.setState({
        selectedShapeName: name,
        rectangles
      });
    } else {
      this.setState({
        selectedShapeName: ""
      });
    }
  };

  handleRectChange = (index, newProps) => {
    const { rectangles } = this.state;
    rectangles[index] = {
      ...rectangles[index],
      ...newProps
    };

    this.setState({ rectangles });
  };

  handleNewRectChange = event => {
    const { rectangles, rectCount, newRectX, newRectY } = this.state;
    const stage = event.target.getStage();
    const mousePos = stage.getPointerPosition();
    if (!rectangles[rectCount]) {
      rectangles.push({
        x: newRectX,
        y: newRectY,
        width: mousePos.x - newRectX,
        height: mousePos - newRectY,
        name: `rect${rectCount + 1}`,
        stroke: "#00A3AA",
        key: uuid.v4()
      });
      return this.setState({ rectangles, mouseDraw: true });
    }
    rectangles[rectCount].width = mousePos.x - newRectX;
    rectangles[rectCount].height = mousePos.y - newRectY;
    return this.setState({ rectangles });
  };

  handleStageMouseUp = () => {
    const { rectCount, mouseDraw } = this.state;
    if (mouseDraw) {
      this.setState({ rectCount: rectCount + 1, mouseDraw: false });
    }
    this.setState({ mouseDown: false });
  };

  render() {
    const { open } = this.state;
    const {
      state: { rectangles, selectedShapeName, mouseDown },
      handleStageMouseDown,
      handleNewRectChange,
      handleRectChange,
      handleStageMouseUp
    } = this;
    return (
      <div>
        <input type="file" onChange={this.handleChange} />
        <IconButton className="iconButton" onClick={this.handleClick}>
          <MessageIcon />
        </IconButton>
        <Modal open={open} onClose={this.handleClose}>
          <div id="modal-container">
            <Stage
              width={window.innerWidth * 0.8}
              height={window.innerHeight * 0.8}
              container="modal-container"
              width={994}
              height={640}
              onMouseDown={handleStageMouseDown}
              onTouchStart={handleStageMouseDown}
              onMouseMove={mouseDown && handleNewRectChange}
              onTouchMove={mouseDown && handleNewRectChange}
              onMouseUp={mouseDown && handleStageMouseUp}
              onTouchEnd={mouseDown && handleStageMouseUp}
            >
              <Layer>
                <AnnotationImage src={this.state.file} />
              </Layer>
              <Layer>
                {rectangles.map((rect, i) => (
                  <Rectangle
                    sclassName="rect"
                    key={rect.key}
                    {...rect}
                    onTransform={newProps => {
                      handleRectChange(i, newProps);
                    }}
                  />
                ))}
                <RectTransformer selectedShapeName={selectedShapeName} />
              </Layer>
            </Stage>
            <Button
              color="primary"
              onClick={e => {
                this.handleClose();
                console.log(this.state.rectangles)
                this.props.postImage(this.state.rectangles,this.state.file,this.state.filename,this.props.info.token);
              }}
            >
              OK
            </Button>
          </div>
        </Modal>
      </div>
    );
  }
}

Upload.propTypes = {
  postImage: PropTypes.func.isRequired
};

Modal.propTypes = {
  /**
   * A single child content element.
   */
  children: PropTypes.element.isRequired
};

const mapStatetoProps = state => {
  let ret = {
    rectangles: state.imageReducer.rectangles,
    info: state.loginReducer.info,
  };
  return ret;
};

export default connect(
  mapStatetoProps,
  { postImage }
)(Upload);
