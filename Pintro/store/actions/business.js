import Business from '../../Model/Business';
export const GETBUSINESS = 'GETBUSINESS';
export const getBusiness = () => {
    return async dispatch => {
        console.log(1);
        const response = await fetch('https://bluej-pintro-project.appspot.com/business/postman_business@post.man',
            {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                },
                redirect: 'follow'
            }
        );
        console.log(2);
        console.log(response.ok);
        if(!response.ok) {
            console.log(3);
            const errorResData = await response.json();
            let message = 'Something went wrong';
            throw new Error(message);
        }
        console.log(4);
        const resData = await response.json();

        const queryArray = [];

        for(const searchResult in resData){
            queryArray.push(new Business(
            resData[searchResult].email,
            resData[searchResult].full_name,
            resData[searchResult].location,
            resData[searchResult].password,
            resData[searchResult].phone,
            resData[searchResult].profile_image,
            resData[searchResult].short_bio,
            resData[searchResult].story
            )
            );
        }
        dispatch({type: GETBUSINESS,businessArray:queryArray});
    }
}