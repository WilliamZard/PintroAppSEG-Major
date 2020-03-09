
import {
GET_TIMELINE
} from '../actions/timeline';
const initialState = {
  availablePosts: []
};

export default (state = initialState, action) => {
  switch (action.type) {
    case GET_TIMELINE:
      return {
        availablePosts: action.timelinePosts
      };
  }
  return state;
};
