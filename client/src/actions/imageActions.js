import axios from "axios";
import request from "request";

import {
  REGISTER,
  LOGIN,
  GET_IMAGES,
  POST_IMAGE,
  DELETE_IMAGE,
  SEARCH_TAGS,
  IMAGES_LOADING
} from "./types.js";

export const register = (username, password) => dispatch => {
  request.post(
    "http://localhost:5000/api/register",
    { form: { username: "redside100", password: "lmaoyeet" } },
    function(err, httpres, body) {
      dispatch ({
        type: register,
        payload: body
      })
      console.log(body);
    }
  );
};

export const login = (username, password) => dispatch => {
  var token = "";
  var uuid = "";
  // Login
  request.post(
    "http://localhost:5000/api/login",
    { form: { username: "redside100", password: "lmaoyeet" } },
    function(err, httpres, body) {
      console.log(body);
      var info = JSON.parse(body);
      token = info["token"];
      uuid = info["uuid"];
      dispatch({
        type: login,
        payload: info
      })
      console.log(token);
      console.log(uuid);
    }
  );
};

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

export const getImages = info => dispatch => {
  dispatch(setImagesLoading());
  axios.get("http://localhost:5000/api/images?" + info["token"]).then(res =>
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
