import {
    GETTAGS
    } from '../actions/tags';
    const initialState = {
      tagsArray: [],
      favs1: [],
      favs2: [],
      favs3: []
    };
    
    export default (state = initialState, action) => {
      switch (action.type) {
        case GETTAGS:
          return {
            tagsArray: action.tagsArray,
            favs1: action.favs1,
            favs2: action.favs2,
            favs3: action.favs3,
          };
      }
      return state;
    };
