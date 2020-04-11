
export const CREATE_USER = 'CREATE_USER';
export const UPDATE_STORY = 'UPDATE_STORY';
export const UPDATE_EXPERIENCE = 'UPDATE_EXPERIENCE';
export const UPDATE_PASSIONS = 'UPDATE_PASSIONS';
export const UPDATE_HELP_OTHERS = 'UPDATE_HELP_OTHERS';
export const GETUSER = 'GETUSER';

import { APIKEY }  from '../../Constants/APIKEY';
import User from '../../Model/User';
import { Alert } from 'react-native';
import { BearerToken }  from '../../Constants/BearerToken';

export const create_User = (Industry,academic_Level,current_Company,email,full_name,gender,help_Others,location,passions,
  phone_number,preferrred_name,previous_Company,profile_image,story,university,job_title,
  years_in_industry) => {
  return async (dispatch,getState) => {
console.log("Bearer "+getState().auth.tokenToGet);
    const response = await fetch('https://bluej-pintro-project.appspot.com/users/',
      {
        method: 'POST',
        headers: {                'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+getState().auth.tokenToGet},
           body: JSON.stringify({
            "Industry":Industry,
          "current_Company":current_Company,
          "active": "True",
          "academic_Level":academic_Level,
          "years_in_industry":years_in_industry,
          "education": university,
          "email": email,
          "full_name": full_name,
          "gender": gender,
          "help_others": help_Others,
          "job_title": job_title,
          "location": location,
          "passions": passions,
          "phone": phone_number,
          "preferred_name": preferrred_name,
          "previous_Company": previous_Company,
          "profile_image": "b'" + profile_image+"'",
          "story": story
          
      }), redirect: 'follow'

      }
    );
    if (!response.ok) {
      const errorResData = await response.json();
      console.log(errorResData);   
    }
console.log("HEY");
    dispatch({type: CREATE_USER,
      IndustryToGet:Industry,
      current_CompanyToGet:current_Company,
      academic_LevelToGet:academic_Level,
      years_in_industryToGet:years_in_industry,
      educationToGet: university,
      emailToGet: email,
      full_nameToGet: full_name,
      genderToGet: gender,
      help_othersToGet: help_Others,
      job_titleToGet: job_title,
      locationToGet: location,
      passionsToGet: passions,
      phoneToGet: phone_number,
      preferred_nameToGet: preferrred_name,
      previous_CompanyToGet: previous_Company,
      profile_imageToGet: profile_image,
      storyToGet: story
    });
  };
};





export const get_User_To_Load = () => {
  return async (dispatch,getState) => {
  console.log("Yes boy");
    const response = await fetch('https://bluej-pintro-project.appspot.com/users/'+getState().auth.emailToGet,
      {
        method: 'GET',
        headers: {'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+getState().auth.tokenToGet},
         redirect: 'follow'

      }
    );
    if (!response.ok) {
      const errorResData = await response.json();
      console.log(errorResData);   
    }

    const resData = await response.json();

      const pic = await resData.profile_image;
      const image = pic.substring(2, pic.length - 1);
    const active = resData.active;
    console.log("User is "+active);
    if(active==="False"){
      throw new Error("You're blocked");
    }

    dispatch({type: CREATE_USER,
      IndustryToGet:  resData.Industry,
      current_CompanyToGet:  resData.current_Company,
      academic_LevelToGet:  resData.academic_Level,
      years_in_industryToGet:  resData.years_in_industry,
      educationToGet:  resData.university,
      emailToGet:  resData.email,
      full_nameToGet:  resData.full_name,
      genderToGet:  resData.gender,
      help_othersToGet:  resData.help_others,
      job_titleToGet:  resData.job_title,
      locationToGet:  resData.location,
      passionsToGet:  resData.passions,
      phoneToGet:  resData.phone_number,
      preferred_nameToGet:  resData.preferrred_name,
      previous_CompanyToGet:  resData.previous_Company,
      profile_imageToGet:  image,
      storyToGet:  resData.story
    });
 
  };
};

export const update_story = (full_name,job_title,current_Company,story) => {
  return async (dispatch,getState) => {
console.log("Updating " + getState().user.email);
console.log("Updating " + getState().user.current_Company);
    const response = await fetch('https://bluej-pintro-project.appspot.com/users/'+getState().user.email,
      {
        method: 'PUT',
        headers: { 'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+getState().auth.tokenToGet}
        , body: JSON.stringify({
       
          "current_Company":current_Company,
          "full_name":full_name,
          "job_title":job_title,
          "story":story,
          "passions":getState().user.passions,
          "help_others":getState().user.help_Others,


      })

      }
    );
    if (!response.ok) {
      console.log("shit");
      const errorResData = await response.text();
      let message = 'Something went wrong with the update story';
      console.log(errorResData);
    }
    console.log("updated");
    dispatch({
      type:UPDATE_STORY,
      IndustryToGet:  getState().user.Industry,
      current_CompanyToGet:  current_Company,
      academic_LevelToGet:  getState().user.academic_Level,
      years_in_industryToGet:  getState().user.years_in_industry,
      educationToGet:  getState().user.education,
      emailToGet:  getState().user.email,
      full_nameToGet:  full_name,
      genderToGet:  getState().user.gender,
      help_othersToGet:  getState().user.help_others,
      job_titleToGet: job_title,
      locationToGet:  getState().user.location,
      passionsToGet:  getState().user.passions,
      phoneToGet:  getState().user.phone,
      preferred_nameToGet:  getState().user.preferrred_name,
      previous_CompanyToGet:  getState().user.previous_Company,
      profile_imageToGet:  getState().user.profile_image,
      storyToGet: story
      
    });

    console.log("Updating " + getState().user.email);
    console.log("Updating " + getState().user.passions);
  };
};










export const login = (email, password) => {
    return async dispatch => {
      const response = await fetch(
        'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key='+APIKEY,
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

 


export const update_experience = (workExperience,industry,previous_Company,education,academic_Level) => {
  return async (dispatch,getState) => {
console.log("Updating " + getState().user.email);
const response = await fetch('https://bluej-pintro-project.appspot.com/users/'+getState().user.email,
      {
        method: 'PUT',
        headers: {                'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+getState().auth.tokenToGet}
        , body: JSON.stringify({
          "Industry":industry,
          "academic_Level":academic_Level,
          "years_in_industry":workExperience,
          "education":education,
          "previous_Company":previous_Company,
          "passions":getState().user.passions,
          "help_others":getState().user.help_Others,
      })

      }
    );
    if (!response.ok) {
      console.log("shit");
      const errorResData = await response.json();
      let message = 'Something went wrong with the upate work experience';
      throw new Error(message);
    }

    dispatch({type:UPDATE_STORY,
      IndustryToGet:  industry,
      current_CompanyToGet:  getState().user.current_Company,
      academic_LevelToGet:  academic_Level,
      years_in_industryToGet:  workExperience,
      educationToGet: education,
      emailToGet:  getState().user.email,
      full_nameToGet: getState().user.full_name,
      genderToGet:  getState().user.gender,
      help_othersToGet:  getState().user.help_others,
      job_titleToGet: getState().user.job_title,
      locationToGet:  getState().user.location,
      passionsToGet:  getState().user.passions,
      phoneToGet:  getState().user.phone,
      preferred_nameToGet:  getState().user.preferrred_name,
      previous_CompanyToGet: previous_Company,
      profile_imageToGet:  getState().user.profile_image,
      storyToGet: getState().user.story
    });
  };
};


export const update_passions = (passions) => {
  return async (dispatch,getState) => {
console.log("Updating " + getState().user.email);
const response = await fetch('https://bluej-pintro-project.appspot.com/users/'+getState().user.email,
      {
        method: 'PUT',
        headers: {                'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+getState().auth.tokenToGet}
        , body: JSON.stringify({
       
          "help_others":getState().user.help_others,
          "passions":passions,
          "email":getState().user.email
      })

      }
    );
    if (!response.ok) {
      console.log("shit");
      const errorResData = await response.json();
      let message = 'Something went wrong with the update passions';
      console.log(errorResData);
      throw new Error(message);
    }
    dispatch({
      type:UPDATE_STORY,
      IndustryToGet: getState().user.Industry,
      current_CompanyToGet:  getState().user.current_Company,
      academic_LevelToGet:  getState().user.academic_Level,
      years_in_industryToGet:  getState().user.years_in_industry,
      educationToGet: getState().user.education,
      emailToGet:  getState().user.email,
      full_nameToGet: getState().user.full_name,
      genderToGet:  getState().user.gender,
      help_othersToGet:  getState().user.help_others,
      job_titleToGet: getState().user.job_title,
      locationToGet:  getState().user.location,
      passionsToGet:  passions,
      phoneToGet:  getState().user.phone,
      preferred_nameToGet:  getState().user.preferred_name,
      previous_CompanyToGet: getState().user.previous_Company,
      profile_imageToGet:  getState().user.profile_image,
      storyToGet: getState().user.story
    });
    
  };
};


export const update_help_Others = (help_Others) => {
 
  return async (dispatch,getState) => {
console.log("Updating " + getState().user.email);
const response = await fetch('https://bluej-pintro-project.appspot.com/users/'+getState().user.email,
      {
        method: 'PUT',
        headers: {                'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+getState().auth.tokenToGet}
        , body: JSON.stringify({
       
          "help_others":help_Others,
          "passions":getState().user.passions,
          "email":getState().user.email
      })

      }
    );
    if (!response.ok) {
      console.log("shit");
      const errorResData = await response.json();
      let message = 'Something went wrong with the update passions';
      console.log(errorResData);
      throw new Error(message);
    }
    dispatch({
      type:UPDATE_STORY,
      IndustryToGet: getState().user.Industry,
      current_CompanyToGet:  getState().user.current_Company,
      academic_LevelToGet:  getState().user.academic_Level,
      years_in_industryToGet:  getState().user.years_in_industry,
      educationToGet: getState().user.education,
      emailToGet:  getState().user.email,
      full_nameToGet: getState().user.full_name,
      genderToGet:  getState().user.gender,
      help_othersToGet: help_Others,
      job_titleToGet: getState().user.job_title,
      locationToGet:  getState().user.location,
      passionsToGet:  getState().user.passions,
      phoneToGet:  getState().user.phone,
      preferred_nameToGet:  getState().user.preferred_name,
      previous_CompanyToGet: getState().user.previous_Company,
      profile_imageToGet:  getState().user.profile_image,
      storyToGet: getState().user.story
    });
    
  };
};



export const update_Photo = (pic) => {
 
  return async (dispatch,getState) => {
console.log("Updating " + getState().user.email);
const response = await fetch('https://bluej-pintro-project.appspot.com/users/'+getState().user.email,
      {
        method: 'PUT',
        headers: {                'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+getState().auth.tokenToGet}
        , body: JSON.stringify({
       
          "help_others":getState().user.help_others,
          "passions":getState().user.passions,
          "email":getState().user.email,
          "profile_image": "b'" + pic + "'",
      })

      }
    );
    if (!response.ok) {
      console.log("shit");
      const errorResData = await response.json();
      let message = 'Something went wrong with the update passions';
      console.log(errorResData);
      throw new Error(message);
    }
    dispatch({
      type:UPDATE_STORY,
      IndustryToGet: getState().user.Industry,
      current_CompanyToGet:  getState().user.current_Company,
      academic_LevelToGet:  getState().user.academic_Level,
      years_in_industryToGet:  getState().user.years_in_industry,
      educationToGet: getState().user.education,
      emailToGet:  getState().user.email,
      full_nameToGet: getState().user.full_name,
      genderToGet:  getState().user.gender,
      help_othersToGet: getState().user.help_others,
      job_titleToGet: getState().user.job_title,
      locationToGet:  getState().user.location,
      passionsToGet:  getState().user.passions,
      phoneToGet:  getState().user.phone,
      preferred_nameToGet:  getState().user.preferred_name,
      previous_CompanyToGet: getState().user.previous_Company,
      profile_imageToGet:  pic,
      storyToGet: getState().user.story
    });
    
  };
};







export const send_Verification_Mail = () => {
  return async (dispatch,getState) => {
 
console.log("Bearer "+getState().auth.tokenToGet);
const response = await fetch('https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key='+APIKEY,
{method:'POST',
headers: {
  'Content-Type': 'application/json'
},body: JSON.stringify({
  "requestType":"VERIFY_EMAIL",
  "idToken": getState().auth.tokenToGet
})
});
    if (!response.ok) {
      console.log("shit");
      const errorResData = await response.json();
      console.log(errorResData);
   
    }
console.log("didnt crash");
 
  };
};

 


export const isUserVerified = () => {
  return async (dispatch,getState) => {
    const response = await fetch('https://identitytoolkit.googleapis.com/v1/accounts:lookup?key='+APIKEY,
    {method:'POST',
    headers: {
      'Content-Type': 'application/json'
    },body: JSON.stringify({
      "idToken": getState().auth.tokenToGet
    })
    });
    if (!response.ok) {
      console.log("shit");
      const errorResData = await response.json();
      console.log(errorResData);
   
    }

    const resData = await response.json();
    console.log(resData.users[0].emailVerified);
 
  };
};


 


  export const resetPassword = (emailUser) => {
      return async (dispatch,getState) => {
 
        const response = await fetch('https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key='+APIKEY,
        {method:'POST',
    headers: {
      'Content-Type': 'application/json'
    },body: JSON.stringify({
      "requestType":"PASSWORD_RESET",
      "email":emailUser}
    )
    });
        if (!response.ok) {
          console.log("shit");
          const errorResData = await response.json();
          console.log(errorResData);
       
        }
    
        
     
      };
    };
    
    

export const GETUSER = 'GETUSER';
export const getUser = searchEmail => {
  return async dispatch => {
    try {
      const response = await fetch('https://bluej-pintro-project.appspot.com/users/' + searchEmail,
        {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': BearerToken
          },
          redirect: 'follow'
        } 
      );
      console.log("Get user: " + (response.status));

      if(!response.ok) {
        if(response.status == '404') {
          Alert.alert('No results found','No users were found that match your search');
        } else if (response.status == '422') {
          Alert.alert('Invalid search term','Please enter an email address');
        } else {
          const errorResData = await response.json();
          console.log(errorResData);
          let message = 'Something went wrong';
          throw new Error(message);
        }
      } else {
        const resData = await response.json();
          let searchedUser = new User(
            resData.education,
            resData.email,
            resData.full_name,
            resData.gender,
            resData.job_title,
            resData.location,
            resData.password,
            resData.phone,
            resData.preferred_name,
            resData.profile_image,
            "",
            "",
            resData.short_bio,
            resData.story
          );
          dispatch({type: GETUSER,userObj:searchedUser});
      }
    } catch (error) {
      console.log(error);
    }
  }
}

