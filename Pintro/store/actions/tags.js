import Tag from '../../Model/Tag';
import { BearerToken } from '../../Constants/BearerToken';
export const GETTAGS = 'GETTAGS';
export const getTags = () => {

  return async (dispatch) => {
    const response = await fetch('https://bluej-pintro-project.appspot.com/tags/',
      {
          method:"POST",
          headers:{
            'Content-Type':'application/json',
            'Authorization': BearerToken
          },
          body: JSON.stringify({
            "labels":["Tag"]
          }),
          redirect: 'follow'
      }
    );
  
    const resData = await response.json();

    const loadedfavTags1 = ["Accounting","Job Evaluation","Jordan","JVM","Kazakhstan","Judge"];
    const loadedfavTags2 = ["Keyword Research","Lawyer","Lead Generation","Legal Research","Licensing Agreements","Lighting"];
    const loadedfavTags3 = ["Loan Origination","Local Marketing","Machine Learning Engineer","Maintenance Management","Market Planning","Marketing Expert"];
    
    dispatch({type: GETTAGS,tagsArray:resData,favs1:loadedfavTags1,favs2:loadedfavTags2,favs3:loadedfavTags3});
  };
};