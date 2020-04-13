import Tag from '../../Model/Tag';
import { BearerToken } from '../../Constants/BearerToken';
export const GETTAGS = 'GETTAGS';
export const LOGOUT = 'LOGOUT';

function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;
  while (0 !== currentIndex) {
   
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

export const getTags = () => {
  return async (dispatch,getState) => {
        const passionTags = await fetch('https://bluej-pintro-project.appspot.com/tags/',
          { 
              method:"POST",
              headers:{
                'Content-Type':'application/json',
                'Authorization': 'Bearer ' + getState().auth.tokenToGet
              },
              body: JSON.stringify({
                "labels":["PassionsTag"]
              }),
              redirect: 'follow'
          }
      );
      const helpOtherTags = await fetch('https://bluej-pintro-project.appspot.com/tags/',
      {
          method:"POST",
          headers:{
            'Content-Type':'application/json',
            'Authorization': 'Bearer ' + getState().auth.tokenToGet
               },
          body: JSON.stringify({
            "labels":["CanHelpWithTag"]
          }),
          redirect: 'follow'
      }
  );
  const businessTags = await fetch('https://bluej-pintro-project.appspot.com/tags/',
  {
      method:"POST",
      headers:{
        'Content-Type':'application/json',
        'Authorization': 'Bearer ' + getState().auth.tokenToGet
      },
      body: JSON.stringify({
        "labels":["BusinessTag"]
      }),
      redirect: 'follow'
  },
);
 
      

const searchTagsReq = await fetch('https://bluej-pintro-project.appspot.com/tags/',
  {
      method:"POST",
      headers:{
        'Content-Type':'application/json',
        'Authorization': 'Bearer ' + getState().auth.tokenToGet
      },
      body: JSON.stringify({
        "labels":['PassionsTag', 'BusinessTag', 'CanHelpWithTag','HelpMeWithTag', 'IntroMeToTag', 'JobTitleTag']
      }),
      redirect: 'follow'
  }
);
    const searchTags = await searchTagsReq.json();

      const passionData = await passionTags.json();
      const helpOthersData = await helpOtherTags.json();
      const businessData = await businessTags.json();
      const passionSHUFFLE = shuffle(passionData);
      const helpOthersSHUFFLE = shuffle(helpOthersData);
      const businessSHUFFLE = shuffle(businessData);


    dispatch({type: GETTAGS, businessTagsToGet:businessData,
      passionTagsToGet:passionData,
      helpOthersWithTagsToGet:helpOthersData,
      searchTagsToGet:searchTags,

      businessTagsSHUFFLEDTOGET:businessSHUFFLE,
      passionTagsSHUFFLEDTOGET:passionSHUFFLE,
      helpOthersWithTagsSHUFFLEDTOGET:helpOthersSHUFFLE});
  };
};
 

export const logout = () => {
  return { type: LOGOUT };
};
