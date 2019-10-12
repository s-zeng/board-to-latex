import React, { Component, Children } from "react";
import Modal from "@material-ui/core/Modal";
import PropTypes from "prop-types";
import Button from "@material-ui/core/Button";
import IconButton from "@material-ui/core/IconButton";
import MessageIcon from "@material-ui/icons/Message";

class Upload extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      file: null
    };
    this.prevProps = this.props;
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({
      file: URL.createObjectURL(event.target.files[0])
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

  render() {
    const { open } = this.state;
    return (
      <div>
        <input type="file" onChange={this.handleChange} />
        <IconButton className="iconButton" onClick={this.handleClick}>
          <MessageIcon />
        </IconButton>
        <Modal open={open} onClose={this.handleClose}>
          <div>
            <img src={this.state.file} style={{ width: "80%" }} />
            <Button color="primary" onClick={this.handleClose}>
              OK
            </Button>
          </div>
        </Modal>
      </div>
    );
  }
}
Modal.propTypes = {
  /**
   * A single child content element.
   */
  children: PropTypes.element.isRequired
};

export default Upload;
