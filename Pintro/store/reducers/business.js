import { 
    GETBUSINESS ,
    LOGOUT
    } from '../actions/business';
import Business from '../../Model/Business';
    const initialState = {
        businessObj: new Business("2","No","ddd","dwawqd","dwqqdw","qdwwqd","ewfewfewf","fewfewfewf","qwdqwd","qqdwqwd","dqwdqwdqw","cwececw","dwqqwdqwd",[],"qwddqwdwq")
    };

    export default (state = initialState, action) => {
        switch(action.type) {
            case GETBUSINESS:
                return {
                    businessObj: action.businessObj
                };
                case LOGOUT:
                    return{
                businessObj: new Business("2","No","ddd","dwawqd","dwqqdw","qdwwqd","ewfewfewf","fewfewfewf","qwdqwd","qqdwqwd","dqwdqwdqw","cwececw","dwqqwdqwd",[],"qwddqwdwq")
                    }
                
        }
       
        return state;
    };