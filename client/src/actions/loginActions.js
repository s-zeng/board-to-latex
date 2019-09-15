import request from "request";

import {
  REGISTER,
  LOGIN,
} from "./types.js";

export const register = (username, password) => dispatch => {
  request.post(
    "http://localhost:5000/api/register",
    { form: { username: "redside100", password: "lmaoyeet" } },
    function(err, httpres, body) {
        console.log(JSON.parse(body))
      dispatch({
        type: REGISTER,
        payload: JSON.parse(body)
      });
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
