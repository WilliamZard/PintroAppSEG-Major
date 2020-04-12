import { BearerToken } from '../../Constants/BearerToken';
export const REQUESTFOLLOW = 'REQUESTFOLLOW';
export const REQUESTAFIL = 'REQUESTAFIL';
export const requestFol = (user1, user2) => {
    return async dispatch => {
        try{
            const response = await fetch("https://bluej-pintro-project.appspot.com/request/follow/" + user1 + "/" + user2,
            {
                method: 'POST',
                headers: {
                    'Authorization': BearerToken
                },
                redirect: 'follow'
            });
            console.log("follow request: " + response.status);
        } catch (error) {
            console.log(error);
        }
        dispatch({type: REQUESTFOLLOW,responseStatus:"101"});
    }
};

export const requestAfil = (user1, user2) => {
    return async dispatch => {
        const response = await fetch("https://bluej-pintro-project.appspot.com/request/affiliation/" + user1 + "/" + user2,
        {
            method: 'POST',
            headers: {
                'Authorization': BearerToken
            },
            redirect: 'follow'
        });
        console.log("affiliation request: " + response.status);
        
        if(!response.ok) {
            const errorResData = await response.text();
            console.log(errorResData); 
        }
        dispatch({type: REQUESTAFIL,responseStatus:"101"});
    }
}