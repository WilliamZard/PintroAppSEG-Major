import { 
    GETBUSINESS 
    } from '../actions/business';
    const initialState = {
        businessObj: null
    };

    export default (state = initialState, action) => {
        switch(action.type) {
            case GETBUSINESS:
                return {
                    businessObj: action.businessObj
                };
        }
        return state;
    };