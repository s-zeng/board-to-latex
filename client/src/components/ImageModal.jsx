import React, { COmponent } from "react";

class ImageModal extends Component {
    constructor(props) {
        super(props);
        this.state = {

        }
    }
  render() {
    return (
      <Modal aria-labelledby="modal-title" aria-describedby="modal-description">
        <img src={this.props.filename} />
      </Modal>
    );
  }
}
