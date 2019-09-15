import {
    REGISTER,
    LOGIN
  } from "../actions/types.js";
  
  const initialState = {
    info: {},
    body: {},
  };
  
  export default function(state = initialState, action) {
    switch (action.type) {
      case REGISTER:
        return {
          ...state,
          body: action.payload
        };
      case LOGIN:
        return {
          ...state,
          info: action.payload
        };
      default:
        return state;
    }
  }
  
