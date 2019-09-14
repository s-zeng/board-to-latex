import React, { Component } from "react";
import { withStyles } from '@material-ui/styles';
import PropTypes from 'prop-types';
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import Chip from "@material-ui/core/Chip";

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
      <Card className={classes.card}>
        <CardActionArea>
          <CardMedia
            className={classes.media}
            image={this.props.image}
          />
          <CardContent>
            <Typography variant="body2" color="textSecondary" component="p">
              <Chip
                variant="outlined"
                size="small"
                label={this.props.label}
                className={classes.chip}
              />
            </Typography>
          </CardContent>
        </CardActionArea>
        <CardActions>
          <Button size="small" color="primary">
            Open
          </Button>
        </CardActions>
      </Card>
    );
  }
}

ImageCard.propTypes = {
    classes: PropTypes.object.isRequired,
  };

export default withStyles(styles)(ImageCard);
