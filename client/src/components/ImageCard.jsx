import React, { Component } from "react";
import { withStyles } from "@material-ui/styles";
import PropTypes from "prop-types";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import ButtonBase from "@material-ui/core/ButtonBase";
import Typography from "@material-ui/core/Typography";
import Chip from "@material-ui/core/Chip";
import { connect } from "react-redux";
import { postImage } from "../actions/imageActions";
import { Button } from "@material-ui/core";

const styles = theme => ({
  card: {
    maxWidth: 345
  },
  media: {
    height: 140
  }
});

class ImageCard extends Component {

  render() {
    const { classes } = this.props;

    return (
      <Card className={classes.card} onClick={this.props.postImage()}>
        <CardActionArea>
          <CardMedia className={classes.media} image={this.props.image} />
          <CardContent>
          </CardContent>
        </CardActionArea>
        <CardActions>
        </CardActions>
      </Card>
    );
  }
}

ImageCard.propTypes = {
  classes: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  image: state.image
});
export default connect(
  mapStateToProps,
  { postImage }
)(withStyles(styles)(ImageCard));
