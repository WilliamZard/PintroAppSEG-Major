import { 
    GETBUSINESS 
    } from '../actions/business';
    const initialState = {
        businessArray: []
    };

    export default (state = initialState, action) => {
        switch(action.type) {
            case GETBUSINESS:
                return {
                    businessArray: action.businessArray
                };
        }
        return state;
    };