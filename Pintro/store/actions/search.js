import User from '../../Model/User';
import { BearerToken }  from '../../Constants/BearerToken';
export const LOGOUT = 'LOGOUT';
export const GETRESULTS = 'GETRESULTS';
export const getResults = (item) => {
    return async (dispatch,getState) => {
        const response = await fetch("https://bluej-pintro-project.appspot.com/search/",
            {
              method: 'POST',
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + getState().auth.tokenToGet
              },
              body: JSON.stringify({
                query: item
              }),
              redirect: 'follow'
            }   
        );
        //console.log("search: " + response.status);
        if(!response.ok) {
          const errorResData = await response.json();
          console.log(errorResData);
          let message = 'Something went wrong';
          throw new Error(message);
        }

        const resData = await response.json();

        const searchResultsArray = [];
       
        for(const searchResult in resData){
          searchResultsArray.push(new User(
          resData[searchResult].education,
          resData[searchResult].email,
          resData[searchResult].full_name,
          resData[searchResult].gender,
          resData[searchResult].job_title,
          resData[searchResult].location,
          resData[searchResult].password,
          resData[searchResult].phone,
          resData[searchResult].preferred_name,
          resData[searchResult].profile_image,
          resData[searchResult].profile_type,
          resData[searchResult].score,
          resData[searchResult].short_bio,
          resData[searchResult].story
          )

         );

        }
        dispatch({type: GETRESULTS,usersArray:searchResultsArray});
    };
};


export const logout = () => {
  return { type: LOGOUT };
};
