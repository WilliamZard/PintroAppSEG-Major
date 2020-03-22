import Tag from '../../Model/Tag';
export const GETTAGS = 'GETTAGS';
export const getTags = () => {
  return async dispatch => {
    const response = await fetch('http://demo9967300.mockable.io/tags',
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
        
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
      loadedTags.push(new Tag(tags[element].created,tags[element].name,tags[element].uuid));
    }
    dispatch({type: GETTAGS,tagsArray:loadedTags});
  };
};