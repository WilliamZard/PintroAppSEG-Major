import User from '../../Model/User';
export const GETRESULTS = 'GETRESULTS';
export const getResults =  () => {
    return async dispatch => {
        console.log("Search word:");
        const response = await fetch('https://bluej-pintro-project.appspot.com/search',
            {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                query: "Post Man2"
              })
            }   
        );
        console.log(4);
        if(!response.ok) {
            console.log(5);
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