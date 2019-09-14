import axios from "axios";
import {
  GET_IMAGES,
  POST_IMAGE,
  DELETE_IMAGE,
  SEARCH_TAGS,
  IMAGES_LOADING
} from "./types.js";

export const postImage = image => dispatch => {
  axios.post("/api/images", image).then(res =>
    dispatch({
      type: POST_IMAGE,
      payload: res.data
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

export const getImages = () => dispatch => {
  dispatch(setItemsLoading());
  axios.get("/api/images").then(res =>
    dispatch({
      type: GET_IMAGES,
      payload: res.data
    })
  );
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
