import {
    GETTAGS
    } from '../actions/tags';
    const initialState = {
      tagsArray: []
    };
    
    export default (state = initialState, action) => {
      switch (action.type) {
        case GETTAGS:
          return {
            tagsArray: action.tagsArray
          };
      }
      return state;
    };
