import { REQUESTFOLLOW,REQUESTAFIL,LOGOUT } from "../actions/request"

const initialState = {
    statusCode: "200"
}

export default (state = initialState,action) => {
    switch(action.type) {
        case REQUESTFOLLOW: 
            return {
                statusCode: responseStatus
            }
        case REQUESTAFIL:
            return{
                statusCode: responseStatus
            }
            case LOGOUT:
                return{
                    statusCode: null
                }
    }

    return state;
};