import axios from "axios";
import request from "request";
import FormData from "form-data";

import {
  GET_IMAGES,
  POST_IMAGE,
  DELETE_IMAGE,
  SEARCH_TAGS,
  IMAGES_LOADING
} from "./types.js";

export const postImage = (rectangles, image, filename, token) => dispatch => {
  var formData = new FormData();
  formData.set("rectangles", JSON.stringify(rectangles));
  formData.set("token", token);
  formData.set("filename", filename);
  formData.append("file", image);
  let config = {
    header: {
      "Content-Type": "multipart/form-data"
    }
  };
  axios.post("/api/images", formData, config).then(res =>
    dispatch({
      type: POST_IMAGE,
      payload: res
    })
  );
};

export const searchTags = id => dispatch => {
  axios.get(`/api/images/${id}`).then(res =>
    dispatch({
      type: SEARCH_TAGS,
      payload: id
    })
  );
};

export const getImages = info => dispatch => {
  var token = info["token"];
  dispatch(setImagesLoading());
  request.get("http://localhost:5000/api/images?token=" + token, function(
    err,
    httpres,
    body
  ) {
    dispatch({
      type: GET_IMAGES,
      payload: JSON.parse(body)
    });
  });
};

export const deleteImage = id => dispatch => {
  axios.delete(`/api/items/${id}`).then(res =>
    dispatch({
      type: DELETE_IMAGE,
      payload: id
    })
  );
};

export const setImagesLoading = () => {
  return {
    type: IMAGES_LOADING
  };
};
