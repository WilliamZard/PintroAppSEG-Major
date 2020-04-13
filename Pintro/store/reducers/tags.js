import {

    GETTAGS,
    LOGOUT
    } from '../actions/tags';
    const initialState = {
      businessTags:[],
      passionTags:[],
      helpOthersWithTags:[],
      searchTags:[],
      businessTagsSHUFFLED:[],
      passionTagsSHUFFLED:[],
      helpOthersWithTagsSHUFFLED:[],
    };
    
    export default (state = initialState, action) => {
      switch (action.type) {
        case GETTAGS:
          return {
            businessTags:action.businessTagsToGet,
            passionTags:action.passionTagsToGet,
            helpOthersWithTags:action.helpOthersWithTagsToGet,
            searchTags:action.searchTagsToGet,
            businessTagsSHUFFLED:action.businessTagsSHUFFLEDTOGET,
            passionTagsSHUFFLED:action.passionTagsSHUFFLEDTOGET,
            helpOthersWithTagsSHUFFLED:action.helpOthersWithTagsSHUFFLEDTOGET
          }
          case LOGOUT:
            return {
              businessTags:[],
      passionTags:[],
      helpOthersWithTags:[],
      searchTags:[],
      businessTagsSHUFFLED:[],
      passionTagsSHUFFLED:[],
      helpOthersWithTagsSHUFFLED:[],
            }
      }
      return state;
    };

