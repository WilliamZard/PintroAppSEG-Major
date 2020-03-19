import { LOGIN, SIGNUP, LOGOUT } from '../actions/auth';

const initialState = {
  token: null,
  userId: null,
  email:"ben@kcl.ac.uk"
};

export default (state = initialState, action) => {
  switch (action.type) {
    case SIGNUP:
      return {
        token: action.token,
        userId: action.userId,
        email:action.email
      }
      case LOGIN:
      return {
        token: action.token,
        userId: action.userId,
        email:action.email
      }
      case LOGOUT:
        return{
          token: null,
          userId: null,
          email:null
        }
    default:
      return state;
  }
};
