import React from 'react';
import { Transformer } from 'react-konva';

class RectTransformer extends React.Component {
  componentDidMount() {
    this.checkNode();
  }

  componentDidUpdate() {
    this.checkNode();
  }

  checkNode = () => {
    // here we need to manually attach or detach Transformer node
    const stage = this.transformer.getStage();
    const { selectedShapeName } = this.props;
    const selectedNode = stage.findOne(`.${selectedShapeName}`);
    // do nothing if selected node is already attached
    if (selectedNode === this.transformer.node()) {
      return;
    }

    if (selectedNode) {
      // attach to another node
      this.transformer.attachTo(selectedNode);
    } else {
      // remove transformer
      this.transformer.detach();
    }
  };

  render() {
    return (
      <Transformer
        ref={(node) => {
          this.transformer = node;
        }}
        rotateEnabled={false}
      />
    );
  }
}

export default RectTransformer;
