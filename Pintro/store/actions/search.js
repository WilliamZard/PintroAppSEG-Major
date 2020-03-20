import User from '../../Model/User';
export const GETRESULTS = 'GETRESULTS';
export const getResults = searchWord => {
    return async dispatch => {
        console.log("Search word: " + searchWord);
        console.log(3);
        const response = await fetch('https://bluej-pintro-project.appspot.com/search',
            {
              method: 'Post',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                query: searchWord
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
        console.log(6);
        const resData = await response.json();

        const users = resData;
        const loadedUsers = [];

        for(const element in users) {
            loadedUsers.push(new User(users[element].email,users[element].full_name))
        }
    
        dispatch({type: GETRESULTS,usersarray: loadedUsers});
    };
};