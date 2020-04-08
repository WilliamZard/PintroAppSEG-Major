import User from '../../Model/User';
import { BearerToken }  from '../../Constants/BearerToken';
export const GETRESULTS = 'GETRESULTS';
export const getResults = (item) => {
    return async dispatch => {
        console.log("Keyword for the DB is: " + item);
        const response = await fetch("https://bluej-pintro-project.appspot.com/search/",
            {
              method: 'POST',
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': BearerToken
              },
              body: JSON.stringify({
                query: item
              }),
              redirect: 'follow'
            }   
        );
        console.log(response.status);
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
        console.log("2");
        console.log("In search actions: " + searchResultsArray.length);
        dispatch({type: GETRESULTS,usersArray:searchResultsArray});
    };
};