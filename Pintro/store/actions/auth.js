export const SIGNUP = 'SIGNUP';
export const LOGIN = 'LOGIN';
export const LOGOUT = 'LOGOUT';

export const signup = (email, password) => {
  return async dispatch => {
    const response = await fetch(
        'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyCZUeHC1zcLM__APOSB0dCXJkNPsOZuDKM',
        {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              email: email,
              password: password,
              returnSecureToken: true
            })
          }
        );
    
        if (!response.ok) {
            const errorResData = await response.json();
            const errorId = errorResData.error.message;
            let message = 'Something went wrong!';
            if (errorId === 'EMAIL_EXISTS') {
              message = 'This email exists already!';
            }
            throw new Error(message);
          }
    
        const resData = await response.json();
       const tokenID = await resData.idToken;
        console.log("ID="+email);
        console.log("REFRESh"+resData.refreshToken);
        console.log("MM"+tokenID);
        dispatch({ type: SIGNUP, tokenToGet:tokenID,refreshToken:resData.refreshToken, userId: resData.localId, emailToGet:email});

      };
    };

export const login = (email, password) => {
    return async dispatch => {
      const response = await fetch(
        'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyCZUeHC1zcLM__APOSB0dCXJkNPsOZuDKM',
        {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              email: email,
              password: password,
              returnSecureToken: true
            })
          }
        );
    
        if (!response.ok) {
          const errorResData = await response.json();
          const errorId = errorResData.error.message;
          let message = 'Something went wrong!';
          if (errorId === 'EMAIL_NOT_FOUND') {
            message = 'This email could not be found!';
          } else if (errorId === 'INVALID_PASSWORD') {
            message = 'This password is not valid!';
          }
          throw new Error(message);
        }
    
        const resData = await response.json();
 
        dispatch({ type: LOGIN, token: resData.idToken, userId: resData.localId, email:email });
      };
    };
    

    export const logout = () => {
      return { type: LOGOUT };
    };



    export const newToken = () => {
      return async (dispatch,getState) => {
        const response = await fetch(
          'https://securetoken.googleapis.com/v1/token?key=AIzaSyCZUeHC1zcLM__APOSB0dCXJkNPsOZuDKM',
          {
              method: 'GET',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                "grant_type":getState().auth.refreshToken,
                "refresh_token":refresh_token,
              })
            }
          );
      
          if (!response.ok) {
            const errorResData = await response.json();
            const errorId = errorResData.error.message;
            let message = 'Something went wrong!';
            if (errorId === 'EMAIL_NOT_FOUND') {
              message = 'This email could not be found!';
            } else if (errorId === 'INVALID_PASSWORD') {
              message = 'This password is not valid!';
            }
            throw new Error(message);
          }
      
          const resData = await response.json();
          console.log(resData);
          
        };
    }