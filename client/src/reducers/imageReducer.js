import {
    POST_IMAGE,
    SEARCH_TAGS,
    GET_IMAGES,
    DELETE_IMAGE,
    IMAGES_LOADING
  } from "../actions/types.js";
  
  const initialState = {
    items: [],
    loading: false
  };
  
  export default function(state = initialState, action) {
    switch (action.type) {
      case POST_IMAGE:
        return {
          ...state,
          items: [action.payload, ...state.items]
        };
      case SEARCH_TAGS:
        return {
          ...state,
          items: state.items.filter(item => item._id !== action.payload)
        };
      case GET_IMAGES:
        return {
          ...state,
          items: action.payload,
          loading: false
        };
      case DELETE_IMAGE:
        return {
          ...state,
          items: state.items.filter(item => item._id !== action.payload)
        };
      case IMAGES_LOADING:
        return {
          ...state,
          loading: true
        };
      default:
        return state;
    }
  }
  