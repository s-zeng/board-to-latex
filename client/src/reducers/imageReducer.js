import {
    POST_IMAGE,
    SEARCH_TAGS,
    GET_IMAGES,
    DELETE_IMAGE,
    IMAGES_LOADING
  } from "../actions/types.js";
  
  const initialState = {
    images: [],
    tex: [],
    loading: false
  };
  
  export default function(state = initialState, action) {
    switch (action.type) {
      case POST_IMAGE:
        return {
          ...state,
          tex: action.payload
        };
      case SEARCH_TAGS:
        return {
          ...state,
          images: state.images.filter(image => image._id !== action.payload)
        };
      case GET_IMAGES:
        return {
          ...state,
          images: action.payload,
          loading: false
        };
      case DELETE_IMAGE:
        return {
          ...state,
          images: state.images.filter(image => image._id !== action.payload)
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
  
