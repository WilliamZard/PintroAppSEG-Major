import { 
    GETRESULTS,LOGOUT
    } from '../actions/search';
    const initialState = {
        usersArray: []
    };

    export default (state = initialState, action) => {
        switch(action.type) {
            case GETRESULTS:
                return {
                    usersArray: action.usersArray
                }
                case LOGOUT:
                return {
                    usersArray: []
                };              
        }

        return state;
    };