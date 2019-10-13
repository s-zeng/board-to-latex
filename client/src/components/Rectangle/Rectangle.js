import React from 'react';
import { Rect } from 'react-konva';

class Rectangle extends React.Component {
  // compare batchDraw() and draw();
  componentDidUpdate() {
    // this.rect.getLayer().draw();
    this.rect.getLayer().batchDraw();
  }

  handleChange = (event) => {
    const {
      props: { onTransform },
    } = this;
    const shape = event.target;
    // take a look into width and height properties
    // by default Transformer will change scaleX and scaleY
    // while transforming
    // so we need to adjust that properties to width and height
    onTransform({
      x: shape.x(),
      y: shape.y(),
      width: shape.width() * shape.scaleX(),
      height: shape.height() * shape.scaleY(),
      rotation: shape.rotation(),
    });
  };

  // if use rect.draw(), the new rectangle will cover its transformer
  handleMouseEnter = (event) => {
    const shape = event.target;
    shape.stroke('#3DF6FF');
    shape.getStage().container().style.cursor = 'move';
    // this.rect.draw();
    this.rect.getLayer().draw();
  };

  handleMouseLeave = (event) => {
    const shape = event.target;
    shape.stroke('#00A3AA');
    shape.getStage().container().style.cursor = 'crosshair';
    // this.rect.draw();
    this.rect.getLayer().draw();
  };

  render() {
    const {
      props: {
        x, y, width, height, name, stroke,
      },
      handleChange,
      handleMouseEnter,
      handleMouseLeave,
    } = this;
    return (
      <Rect
        x={x}
        y={y}
        width={width}
        height={height}
        // force no scaling
        // otherwise Transformer will change it
        scaleX={1}
        scaleY={1}
        stroke={stroke}
        strokeWidth={5}
        name={name}
        // save state on dragend or transformend
        onDragEnd={handleChange}
        onTransformEnd={handleChange}
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
        draggable
        ref={(node) => {
          this.rect = node;
        }}
      />
    );
  }
}

export default Rectangle;
