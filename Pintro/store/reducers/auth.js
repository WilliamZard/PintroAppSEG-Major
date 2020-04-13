import { LOGIN, SIGNUP, LOGOUT } from '../actions/auth';

const initialState = {
  tokenToGet: null,
  refreshToken: null,
  userId: null,
  emailToGet:null,
};

export default (state = initialState, action) => {
  switch (action.type) {
    case SIGNUP:
      return {
        tokenToGet: action.tokenToGet,
        refreshToken:action.refreshToken,
        userId: action.userId,
        emailToGet:action.emailToGet
      }
      case LOGIN:
      return {
        tokenToGet: action.tokenToGet,
        refreshToken:action.refreshToken,
        userId: action.userId,
        emailToGet:action.emailToGet
      }
      case LOGOUT:
        return{
          tokenToGet: null,
      refreshToken: null,
      userId: null,
      emailToGet:null,
        }
    default:
      return state;
  }
};
