import { 
    GETRESULTS 
    } from '../actions/search';
    const initialState = {
        usersArray: []
    };

    export default (state = initialState, action) => {
        switch(action.type) {
            case GETRESULTS:
                return {
                    usersArray: action.usersArray
                };              
        }

        return state;
    };