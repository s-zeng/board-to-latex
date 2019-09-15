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
          images: [action.payload, ...state.body],
          body: state.body
        };
      case LOGIN:
        return {
          ...state,
          images: [action.payload, ...state.info],
          body: state.body,
          info: state.info
        };
      default:
        return state;
    }
  }
  
