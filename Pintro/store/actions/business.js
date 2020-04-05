import Business from '../../Model/Business';
import { BearerToken } from '../../Constants/BearerToken';
export const GETBUSINESS = 'GETBUSINESS';
export const getBusiness = value => {
    return async dispatch => {
        const response = await fetch('https://bluej-pintro-project.appspot.com/businesses/' + value,
            {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': BearerToken
                },
                redirect: 'follow'
            }
        );

        console.log(response.status);
        if(!response.ok) {
            const errorResData = await response.json();
            let message = 'Something went wrong';
            throw new Error(message);
        }

        const resData = await response.json();


        var searchedBusiness = new Business(resData.company_size,resData.currently_hiring,resData.date_founded,resData.email,resData.full_name,resData.funding,resData.location,resData.password,resData.phone,resData.profile_image,resData.seeking_investment,resData.short_bio,resData.story,resData.tags,resData.team_members);
        //console.log("New Business = " + searchedBusiness);

        dispatch({type: GETBUSINESS,businessObj:searchedBusiness});
    }
}