import Tag from '../../Model/Tag';
export const GETTAGS = 'GETTAGS';


export const getTags = () => {

  return async (dispatch) => {
        const response = await fetch('https://first-rest-api-sen.herokuapp.com/tags/',
          {
              method:"GET",
              headers:{
                  "Content-Type":"application/json"
              }
              
          }
      );
  
      const resData = await response.json();


    const tags = resData;
    const loadedTags = [];
    for(const element in tags){
      loadedTags.push(new Tag("2009",tags[element].name,tags[element].uuid));
   }
   console.log("Loaded " + loadedTags.length +" Tags");
    dispatch({type: GETTAGS,tagsArray:loadedTags});
    

  };
  
};

/*

export const getTags = () => {
 console.log("HEy");
  return async (dispatch) => {
        const response = await fetch('bluej-pintro-project.appspot.com/tags',
          {
              method:"POST",
              headers:{
                  "Content-Type":"application/json"
              },body:JSON.stringify(
                
                  {
                    "labels":["Tag"]
                  }
                
                )
              
          }
      );
  
      const resData = await response.json();
    console.log(resData);
    const tags = resData;
    const loadedTags = [];
    for(const element in tags){
      loadedTags.push(new Tag(tags[element].created,tags[element].name,tags[element].uuid));
   }
    dispatch({type: GETTAGS,tagsArray:loadedTags});
    dispatch({type: GETTAGS,tagsArray:loadedTags});
  

  };
  
};
*/