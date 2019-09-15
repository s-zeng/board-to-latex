import { combineReducers } from "redux";
import imageReducer from "./imageReducer";
import loginReducer from "./loginReducer";

export default combineReducers({
    imageReducer, loginReducer
});
