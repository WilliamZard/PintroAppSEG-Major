import { 
    GETRESULTS 
    } from '../actions/search';
    const initialState = {
        usersArray: []
    };

    export default (state = initialState, action) => {
        switch(action.type) {
            case GETRESULTS:
                console.log("3");
                console.log("In search reducer: " + action.usersArray.length);
                return {
                    usersArray: action.usersArray
                };              
        }
        console.log("4")
        return state;
    };