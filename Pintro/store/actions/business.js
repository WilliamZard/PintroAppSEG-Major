import Business from '../../Model/Business';
import { BearerToken } from '../../Constants/BearerToken';
export const GETBUSINESS = 'GETBUSINESS';
export const LOGOUT = 'LOGOUT';
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

        console.log("getBusiness: " + response.status);
        if(!response.ok) {
            const errorResData = await response.json();
            console.log(errorResData);
            let message = 'Something went wrong';
            throw new Error(message);
        }

        const resData = await response.json();

        const pic = await resData.profile_image;
        let image;
        if(pic.length>2){
          image = pic.substring(2, pic.length - 1);
        } else {
          image = pic;
        }

        var searchedBusiness = new Business(
          resData.company_size,
          resData.currently_hiring,
          resData.date_founded,
          resData.email,
          resData.full_name,
          resData.funding,
          resData.location,
          resData.password,
          resData.phone,
          image,
          resData.seeking_investment,
          resData.short_bio,
          resData.story,
          resData.tags,
          resData.team_members);
        //console.log("New Business = " + searchedBusiness);

        dispatch({type: GETBUSINESS,businessObj:searchedBusiness});
    }
};



export const create_business = (profile_image,location,story,tags,
    date_founded,company_size,funding,team_members,seeking_investment,currently_hiring) => {
    return async (dispatch,getState) => {
   console.log(profile_image);
      const response = await fetch('https://bluej-pintro-project.appspot.com/businesses/',
        {
          method: 'POST',
          headers: {'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer '+getState().auth.tokenToGet},
             body: JSON.stringify(
                {
                    "email": getState().user.email,
                    "password":"not here",
                    "full_name": getState().user.full_name,
                    "profile_image":"b'" + profile_image+"'" ,
                    "phone": getState().user.phone,
                    "location": location,
                    "short_bio":"NOT A FIELD" ,
                    "story": story,
                    "tags": tags,
                    "date_founded": date_founded,
                    "company_size": company_size,
                    "funding": funding,
                    "seeking_investment": seeking_investment,
                    "currently_hiring": currently_hiring
                  }
        ), redirect: 'follow'
  
        }
      );
      if (!response.ok) {
        const errorResData = await response.json();
        console.log(errorResData);   
      }
  console.log("DDD");
       
    };
  };

export const putBusiness = busObj => {
  return async dispatch => {
    try{
      const response = await fetch('https://bluej-pintro-project.appspot.com/businesses/' + busObj.email,
        {
          method: 'PUT',
          headers: {
            'Content-type': 'application/json',
            'Authorization': BearerToken
          },
          redirect: 'follow',
          body: JSON.stringify(busObj)
        }
      );
      console.log("putBusiness: " + response.status);    
    } catch (error) {
      console.log(error);
    }   
  }
};


export const logout = () => {
  return { type: LOGOUT };
};
