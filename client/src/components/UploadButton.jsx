import React, { Component } from "react";
import PropTypes from "prop-types";
import IconButton from "@material-ui/core/IconButton";
import UploadIcon from "@material-ui/icons/CloudUpload";
import { withStyles } from "@material-ui/styles";
import Input from "@material-ui/core/Input";
import { connect } from "react-redux";
import { postImage } from "../actions/imageActions";

const styles = theme => ({
  input: {
    maxWidth: 345
  }
});
class UploadButton extends Component {
  componentDidMount() {
    var data = new FormData();
    for (const file of this.myInput.files) {
      data.append("files", file, file.name);
    }
    this.props.postImage(data);
  }

  render() {
    const { classes } = this.props;
    return (
      <div>
        <input
          id="myInput"
          type="file"
          ref={ref => (this.myInput = ref)}
          style={{ display: "none" }}
        />
        <IconButton
          className="floatingButton"
          onClick={e => this.myInput.click()}
        >
          <UploadIcon />
        </IconButton>
      </div>
    );
  }
}

UploadButton.propTypes = {
  classes: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  image: state.image
});
export default connect(
  mapStateToProps,
  { postImage }
)(withStyles(styles)(UploadButton));
