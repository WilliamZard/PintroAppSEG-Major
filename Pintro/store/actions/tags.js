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


    const tags = await resData;
    const loadedTags = [];
    for(const element in tags){
      loadedTags.push(new Tag("",tags[element].name,tags[element].uuid));
    }
    const tagList = [...tagSet];
    console.log("Loaded " + tagList.length +" Tags");





const favorites1 = await fetch('https://first-rest-api-sen.herokuapp.com/favs/1',
{
    method:"GET",
    headers:{
        "Content-Type":"application/json"
    }
    
}
);

const returnedFaves1 = await favorites1.json();

const loadedfavTags1 = [];
for(const fav1 in returnedFaves1){
loadedfavTags1.push(new Tag("2009",returnedFaves1[fav1].name,returnedFaves1[fav1].uuid));
}

const favorites2 = await fetch('https://first-rest-api-sen.herokuapp.com/favs/2',
{
    method:"GET",
    headers:{
        "Content-Type":"application/json"
    }
    
}
);

const returnedFaves2 = await favorites2.json();

const loadedfavTags2 = [];
for(const fav2 in returnedFaves2){
loadedfavTags2.push(new Tag("2009",returnedFaves2[fav2].name,returnedFaves2[fav2].uuid));
}


const favorites3 = await fetch('https://first-rest-api-sen.herokuapp.com/favs/3',
{
    method:"GET",
    headers:{
        "Content-Type":"application/json"
    }
    
}
);

const returnedFaves3 = await favorites3.json();

const loadedfavTags3 = [];
for(const fav3 in returnedFaves3){
loadedfavTags3.push(new Tag("2009",returnedFaves3[fav3].name,returnedFaves3[fav3].uuid));
}


//console.log("1: " + loadedfavTags1 + " 2: " + loadedfavTags2 + " 3: " + loadedfavTags3);

    dispatch({type: GETTAGS,tagsArray:tagList,favs1:loadedfavTags1,favs2:loadedfavTags2,favs3:loadedfavTags3});
    
    

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