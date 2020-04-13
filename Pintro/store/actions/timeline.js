import TimelinePost from '../../Model/TimelinePost';

export const GET_TIMELINE = 'GET_TIMELINE';
export const WRITE_POST = 'WRITE_POST';
export const LOGOUT = 'LOGOUT';
function cleanTags(property, array) {
    var mySet = new Set();
    return array.filter(function(x) {
      var key = property(x), isNew = !mySet.has(key);
      if (isNew) mySet.add(key);
      return isNew;
    });
  }
  
async function getPicFromMail(emailAddress,bear) {
    console.log("Pic called");
    var response = await fetch('https://bluej-pintro-project.appspot.com/users/'+emailAddress,
    {
        method:'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+bear
        },
        redirect: 'follow'
     } );

     if(!response.ok){
        const errorResData = await response.text();
        console.log(errorResData); 
    }
  
const data = await response.json();
const name = await data.full_name;
const pic = await data.profile_image;
const image = pic.substring(2, pic.length - 1);
const missing = {
    user_name:name,
    img:image,

}
return missing;
 };


async function getNameFromMail(emailAddress,bear) {
    console.log("CALEED");
    var response = await fetch('https://bluej-pintro-project.appspot.com/users/'+emailAddress,
    {
        method:'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+bear
        },
        redirect: 'follow'
     } );

     if(!response.ok){
        const errorResData = await response.text();
        console.log(errorResData); 
    }
  
const data = await response.json();
const name = await data.full_name;
return name;
 };


async function apiGetAll () {
    
    var response = await fetch('http://www.uuidgenerator.net/api/version1');
    const data = await response.text();
return data;
 };

export const fetchTimeline = () => {
    console.log("MOIN");
    return async (dispatch,getState) => {
        const email = getState().user.email;
        const bearer = getState().auth.tokenToGet;
        const response = await fetch(
            "https://europe-west2-bluej-pintro-project.cloudfunctions.net/generate_timeline/",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json",
                    'Authorization': 'Bearer '+getState().auth.tokenToGet
                },body:JSON.stringify({
                email:email
                })
                
            }
        );
        if(!response.ok){
            const errorResData = await response.text();
            console.log(errorResData); 
        }
 
        const resData = await response.json();
 
       const posts = resData.results;
    
       const loadedProduct = [];
       for(const element in posts){
       const data = await getPicFromMail(posts[element].user_email,bearer);
       loadedProduct.push(new TimelinePost(
        posts[element].content,
        posts[element].created,
        posts[element].user_email,
        posts[element].modified,
        posts[element].uuid,
        data.user_name,
        data.img)
        
        );
       }
 
       const filterdTags = cleanTags(x => x.uuid, loadedProduct);

    dispatch({type: GET_TIMELINE,timelinePosts:filterdTags});

 
    };
    
};

/*

export const fetchTimeline = () => {
    return async dispatch => {
        const response = await fetch(
            //'https://api.myjson.com/bins/13r5yy',
           'https://api.myjson.com/bins/qyazy',
        );
       const resData = await response.json();
        //console.log(resData);
        const loadedProduct = [];

    for(const elementt in resData){
        console.log(elementt+ " " +resData[elementt].content);
        loadedProduct.push(new TimelinePost(resData[elementt].content,resData[elementt].modified,resData[elementt].uuid))
    }
    console.log(loadedProduct);
        dispatch({type: GET_TIMELINE,timelinePosts:loadedProduct});

    };
    
};

*/
export const uploadPost = (postContent,hashtag) => {
  
    return async (dispatch,getState) => {
    const email = getState().user.email;
    const uuidKey = await apiGetAll();
    const content = postContent.replace(/(\r\n|\n|\r)/gm, "");
    const uuid =  uuidKey.replace(/(\r\n|\n|\r)/gm, "");
console.log(email);
console.log(content);
console.log(uuid);

 
    const response = await fetch('https://bluej-pintro-project.appspot.com/posts/',{
    method: 'POST',
    headers:{
      'Content-Type':'application/json',
      'Authorization': 'Bearer '+getState().auth.tokenToGet
    },
    body:JSON.stringify({
        
            "content": content,
            "uuid": uuidKey,
            "created": "2020-04-12T08:05:30.839Z",
            "modified": "2020-04-12T08:05:30.839Z",
            "user_email": email,
            "hashtags": hashtag
          
          
          
    })

    }


    
    );


if(!response.ok){
    const errorResData = await response.text();
    console.log(errorResData); 
}
console.log("Mojn");
console.log(response.status);



dispatch({
    type:WRITE_POST,

})

}

};

/**
 * 
 * {
  "content": "Testing again",
  "uuid": "a2d35213-2ea2-4050-bc86-d195663179f8",
  "created": "2020-03-10T16:38:50.711Z",
  "modified": "2020-03-10T16:38:50.711Z",
  "user_email": "abc2@kcl.com"
}

 */


export const logout = () => {
    return { type: LOGOUT };
  };
