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
      dispatch({
        type: REGISTER,
        payload: body
      });
      console.log(body);
    }
  );
};

export const login = (username, password) => dispatch => {
  var info = {};
  // Login
  request
    .post(
      "http://localhost:5000/api/login",
      { form: { username: "redside100", password: "lmaoyeet" } },
      function(err, httpres, body) {
        console.log(body);
        var linfo = JSON.parse(body);
        info = linfo;
      dispatch({
        type: LOGIN,
        payload: info
      })
      }
    )
    /*
      */
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
  var token = info["token"];
  dispatch(setImagesLoading());
  axios.get("http://localhost:5000/api/images?" + token).then(res =>
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
