export const CREATE_USER = 'CREATE_USER';

import { BearerToken }  from '../../Constants/BearerToken';
export const create_User = (Industry,academic_Level,current_Company,email,full_name,gender,help_Others,location,passions,
  phone_number,preferrred_name,previous_Company,previous_Company_Year_Finished,profile_image,short_bio,story,university,
  university_Year_Finished,years_in_industry) => {
  return async (dispatch,getState) => {
console.log("Bearer "+getState().auth.tokenToGet);
    const response = await fetch('https://bluej-pintro-project.appspot.com/users/',
      {
        method: 'POST',
        headers: {                'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+getState().auth.tokenToGet},
           body: JSON.stringify({
            "education": university,
            "email": email,
            "full_name": full_name,
            "gender": gender,
            "help_others":help_Others,
            "job_title": current_Company,
            "location": location,
            "passions": passions,
            "password": "",
            "phone": phone_number,
            "preferred_name": preferrred_name,
            "previous_Company_Year_Finished": previous_Company_Year_Finished,
            "profile_image": profile_image,
            "short_bio": short_bio,
            "story": story
      }), redirect: 'follow'

      }
    );
    if (!response.ok) {
      console.log("shit");
      const errorResData = await response.json();
      console.log(errorResData);
   
    }
console.log("didnt crash");
    dispatch({type: CREATE_USER,
       full_nameTP:full_name,
       preferrred_nameTP:preferrred_name,
       profile_imageTP:profile_image,
       short_bioTP:short_bio,
       genderTP:gender,
       storyTP:story,
       emailTP:email,
       phone_numberTP:phone_number,
       current_CompanyTP:current_Company,
       years_in_industryTP:years_in_industry,
       IndustryTP:Industry,
       previous_CompanyTP:previous_Company,
       previous_Company_Year_FinishedTP:previous_Company_Year_Finished,
       universityTP:university,
       university_Year_FinishedTP:university_Year_Finished,
       academic_LevelTP:academic_Level,
       locationTP:location,
       passionsTP:passions,
       help_OthersTP:help_Others
    });
  };
};











export const update_story = (full_name,job_title,story,) => {
  return async (dispatch,getState) => {
console.log("Updating " + getState().user.email);
    const response = await fetch('https://bluej-pintro-project.appspot.com/users',
      {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        }, body: JSON.stringify({
          "email": getState().user.email,
          "password": getState().user.password,
          "full_name": full_name,
          "preferred_name": getState().user.preferred_name,
          "profile_image": getState().user.profile_image,
          "phone": getState().user.phone,
          "gender": getState().user.gender,
          "job_title": job_title,
          "location": getState().user.location,
          "short_bio": getState().user.short_bio,
          "story": story,
          "education": getState().user.education,
          "passions": [],
          "help_others": []
      })

      }
    );
    if (!response.ok) {
      console.log("shit");
      const errorResData = await response.json();
      let message = 'Something went wrong with the tags';
      throw new Error(message);
    }

    
  };
};







export const trya = () => {
  return async dispatch => {
    const response = await fetch(
        'https://bluej-pintro-project.appspot.com/users',
        {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgzYTczOGUyMWI5MWNlMjRmNDM0ODBmZTZmZWU0MjU4Yzg0ZGI0YzUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYmx1ZWotcGludHJvLXByb2plY3QiLCJhdWQiOiJibHVlai1waW50cm8tcHJvamVjdCIsImF1dGhfdGltZSI6MTU4NTk4NzU5NCwidXNlcl9pZCI6IjVNdXZRVUkwYW5VSVpXVXYyV25jTWFDancyejIiLCJzdWIiOiI1TXV2UVVJMGFuVUlaV1V2MlduY01hQ2p3MnoyIiwiaWF0IjoxNTg1OTg3NTk0LCJleHAiOjE1ODU5OTExOTQsImVtYWlsIjoicmhlZHVlYmVAaHJpeGlybi5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsicmhlZHVlYmVAaHJpeGlybi5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.Y7vFE8FGDbyrpHZL4sVxXUYeFKbmh8Kv5NQMv4SlEpEX6R8SoruBbCCRYgJUf9Gzk9nV0bd3fcMr8bBBrZQjzEJYIbNvMkfNWY1_-xLJxst_cxcY8PJJA8AWhawFWbU2cDlZo4p9yY23d9w3AsVKNellg0_iSR9WQYWwFQJ2GAtHVJJRPdaGtKglvDqGplHyQGFCcBfRv5_upYefKsy2teVUFsULnq9eOB4PTyJOxLYJTYJmCmXhMO99OHJVogsNK7oRo_ajx_m6TX0Y1HDV_a3nrBSJKRH457S_nWMxSVxLLF7Xp8WYuH-scQZsNOnRJAqpZZNc69j2upbpwvPrfQ'
            },
            body: JSON.stringify({
              "email": "mdn@dddddfg.lu"

            })
          }
        );
    
        if (!response.ok) {
            const errorResData = await response.json();
            console.log(errorResData);
          }
    
        };
    };

export const login = (email, password) => {
    return async dispatch => {
      const response = await fetch(
        'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyCZUeHC1zcLM__APOSB0dCXJkNPsOZuDKM',
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





export const trying = () => {
fetch('https://bluej-pintro-project.appspot.com/users',
 {
  method: 'POST', 
  headers: {
    'Content-Type': 'application/json',
    'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgzYTczOGUyMWI5MWNlMjRmNDM0ODBmZTZmZWU0MjU4Yzg0ZGI0YzUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYmx1ZWotcGludHJvLXByb2plY3QiLCJhdWQiOiJibHVlai1waW50cm8tcHJvamVjdCIsImF1dGhfdGltZSI6MTU4NTk4NzU5NCwidXNlcl9pZCI6IjVNdXZRVUkwYW5VSVpXVXYyV25jTWFDancyejIiLCJzdWIiOiI1TXV2UVVJMGFuVUlaV1V2MlduY01hQ2p3MnoyIiwiaWF0IjoxNTg1OTg3NTk0LCJleHAiOjE1ODU5OTExOTQsImVtYWlsIjoicmhlZHVlYmVAaHJpeGlybi5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsicmhlZHVlYmVAaHJpeGlybi5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.Y7vFE8FGDbyrpHZL4sVxXUYeFKbmh8Kv5NQMv4SlEpEX6R8SoruBbCCRYgJUf9Gzk9nV0bd3fcMr8bBBrZQjzEJYIbNvMkfNWY1_-xLJxst_cxcY8PJJA8AWhawFWbU2cDlZo4p9yY23d9w3AsVKNellg0_iSR9WQYWwFQJ2GAtHVJJRPdaGtKglvDqGplHyQGFCcBfRv5_upYefKsy2teVUFsULnq9eOB4PTyJOxLYJTYJmCmXhMO99OHJVogsNK7oRo_ajx_m6TX0Y1HDV_a3nrBSJKRH457S_nWMxSVxLLF7Xp8WYuH-scQZsNOnRJAqpZZNc69j2upbpwvPrfQ'
  },
  body: JSON.stringify({
    "email": "msdn@dddddfg.lu"
  }),
})
.then((response) => response.json())
.then((data) => {
  console.log('Success:', data);
})
.catch((error) => {
  console.error('Error:', error);
});

}