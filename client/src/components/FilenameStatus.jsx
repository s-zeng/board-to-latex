import React, {Component} from "react";
import Typography from "@material-ui/core/Typography";

class FilenameStatus extends Component {

  render() {
    return (
      <Typography variant="h6" component="h6">
        {this.props.filename} loaded 
      </Typography>
    );
  }
}

export default FilenameStatus;
