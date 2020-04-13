
import {
GET_TIMELINE,
LOGOUT
} from '../actions/timeline';
const initialState = {
  availablePosts: []
};

export default (state = initialState, action) => {
  switch (action.type) {
    case GET_TIMELINE:
      return {
        availablePosts: action.timelinePosts
      }
      case LOGOUT:
      return {
        availablePosts: []
      };
  }
  return state;
};
