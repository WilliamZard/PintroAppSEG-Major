import Tag from '../../Model/Tag';
export const GETTAGS = 'GETTAGS';
export const getTags = () => {
  return async dispatch => {

    const response = await fetch('https://bluej-pintro-project.appspot.com/tags',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          labels:["Tag"]
        })
      }
    );
      
    if (!response.ok) {
      const errorResData = await response.json();
      
      let message = 'Something went wrong with the tags';
      throw new Error(message);
    }
  
    const resData = await response.json();
   
    const tags = resData;
    const loadedTags = [];
   
    for(const element in tags){
      console.log(tags[element].name);
      loadedTags.push(new Tag(tags[element].created,tags[element].name,tags[element].uuid));
    }
    dispatch({type: GETTAGS,tagsArray:loadedTags});
  };
};
