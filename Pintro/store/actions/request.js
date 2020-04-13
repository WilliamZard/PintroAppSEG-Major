import { BearerToken } from '../../Constants/BearerToken';
export const REQUESTFOLLOW = 'REQUESTFOLLOW';
export const LOGOUT = 'LOGOUT';
export const requestFol = (user1,user2) => {
    return async dispatch => {
        try{
            const response = await fetch("https://bluej-pintro-project.appspot.com/request/follow/" + user1 + "/" + user2 + "/",
            {
                method: 'POST',
                headers: {
                    'Authorization': getState().auth.tokenToGet
                },
                redirect: 'follow'
            });
            console.log("follow request: " + response.status);
        } catch (error) {
            console.log(error);
        }
    }
};

export const REQUESTAFIL = 'REQUESTAFIL';
export const requestAfil = (user1,user2) => {
    return async (dispatch,getState) => {
        console.log("You got here");
        const response = await fetch("https://bluej-pintro-project.appspot.com/request/affiliation/" + user1 + "/" + user2,
        {
            method: 'POST',
            headers: {
                'Authorization': getState().auth.tokenToGet
            },
            redirect: 'follow'
        });
        console.log("affiliation request: " + response.status);
        const resData = await response.text();
        
        if(!response.ok) {
            const errorResData = await response.json();
            console.log(errorResData); 
        }
        dispatch({type: REQUESTAFIL,responseStatus:"101"});
    }
}



 

export const logout = () => {
    return { type: LOGOUT };
  };
