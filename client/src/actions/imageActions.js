import axios from "axios";
import {
  GET_IMAGES,
  ADD_IMAGE,
  DELETE_IMAGE,
  SEARCH_TAGS,
  IMAGES_LOADING
} from "./types.js";

export const getImages = () => dispatch => {
  dispatch(setItemsLoading());
  axios.get("/api/images").then(res =>
    dispatch({
      type: GET_IMAGES,
      payload: res.data
    })
  );
};

export const addImage = item => dispatch => {
  axios.post("/api/images", item).then(res =>
    dispatch({
      type: ADD_IMAGE,
      payload: res.data
    })
  );
};

export const deleteImage = id => dispatch => {
  axios.delete(`/api/images/${id}`).then(res =>
    dispatch({
      type: DELETE_IMAGE,
      payload: id
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

export const setImagesLoading = () => {
  return {
    type: IMAGES_LOADING
  };
};
