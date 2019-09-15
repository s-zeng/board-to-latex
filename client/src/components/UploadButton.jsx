import React, { Component } from "react";
import PropTypes from "prop-types";
import IconButton from "@material-ui/core/IconButton";
import UploadIcon from "@material-ui/icons/CloudUpload";
import MessageIcon from "@material-ui/icons/Message";
import { withStyles } from "@material-ui/styles";
import Input from "@material-ui/core/Input";
import { connect } from "react-redux";
import { postImage } from "../actions/imageActions";
import Modal from "@material-ui/core/Modal";
import Button from "@material-ui/core/Button";

const styles = theme => ({
  paper: {
    position: "absolute",
    width: 400,
    backgroundColor: "#FFF",
    border: "2px solid #000",
    padding: (2, 4, 3)
  }
});

class UploadButton extends Component {
  constructor(props) {
    super(props);
    this.prevProps = this.props;
  }
  componentDidMount() {
    var data = new FormData();
    for (const file of this.myInput.files) {
      data.append("file", file, file.name);
    }
    this.setState({ data: this.props.data});
    console.log(this.props.datadata);
  }

  componentDidUpdate(prevProps) {
    if (this.props.open != prevProps.open) {
      this.handleClick();
    }
    console.log(this.props.info);
    if (this.myInput !== undefined && this.props.info !== undefined){
        for (const file of this.myInput.files){
            this.props.postImage(file, this.props.info['token'])
        }
    }
    const { open } = this.state;
    return (
      <div className={classes.root}>
        <input
          id="myInput"
          type="file"
          ref={ref => (this.myInput = ref)}
          style={{ display: "none" }}
        />

        <IconButton className="iconButton" onClick={e => this.myInput.click()}>
          <UploadIcon />
        </IconButton>
        <IconButton className="iconButton" onClick={this.handleClick}>
          <MessageIcon />
        </IconButton>
        <Modal open={open} onClose={this.handleClose}>
           {console.log()} 
          <Button color="primary" onClick={this.handleClose}>
            OK
          </Button>
        </Modal>
      </div>
    );
  }
}

UploadButton.propTypes = {
  classes: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  image: state.image,
    info: state.loginReducer.info
});
export default connect(
  mapStateToProps,
  { postImage }
)(withStyles(styles)(UploadButton));

/*

*/
