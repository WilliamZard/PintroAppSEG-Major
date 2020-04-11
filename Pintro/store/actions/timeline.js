import TimelinePost from '../../Model/TimelinePost';

export const GET_TIMELINE = 'GET_TIMELINE';
export const WRITE_POST = 'WRITE_POST';



async function getNameFromMail(emailAddress,bear) {
    var response = await fetch('https://bluej-pintro-project.appspot.com/users/'+emailAddress,
    {
        method:'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+bear
        },
        redirect: 'follow'
     } );
    const data = await response.json();
return data.full_name;
 };


async function apiGetAll () {
    
    var response = await fetch('http://www.uuidgenerator.net/api/version1');
    const data = await response.text();
return data;
 };

export const fetchTimeline = () => {
 
    return async (dispatch,getState) => {
        const email = getState().auth.email;
        const bearer = getState().auth.tokenToGet;
        const response = await fetch(
            "https://europe-west2-bluej-pintro-project.cloudfunctions.net/generate_timeline",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },body:JSON.stringify({
                email:email
                })
                
            }
        );
    
        const resData = await response.json();
       const posts = resData.results;
       const loadedProduct = [];
       
       for(const element in posts){
       const nameOfwriter = await getNameFromMail(posts[element].email,bearer);
      // const picture = await getNameFromMail(posts[element].email,bearer);
       loadedProduct.push(new TimelinePost(
        posts[element].content,
        posts[element].created,
        posts[element].email,
        posts[element].modified,
        posts[element].uuid,
        nameOfwriter)
        );
       }


    dispatch({type: GET_TIMELINE,timelinePosts:loadedProduct});

 
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
export const uploadPost = (postContent) => {
  
    return async (dispatch,getState) => {
        const email = getState().auth.email;
    const uuidKey = await apiGetAll();
    const content = postContent.replace(/(\r\n|\n|\r)/gm, "");
    const uuid =  uuidKey.replace(/(\r\n|\n|\r)/gm, "");

    console.log
    const response = await fetch('https://bluej-pintro-project.appspot.com/posts',{
    method: 'POST',
    headers:{
      'Content-Type':'application/json'  
    },
    body:JSON.stringify({
            "content": content,
            "uuid":uuid,
            "created": "2020-03-10T16:38:50.711Z",
            "modified": "2020-03-10T16:38:50.711Z",
            "user_email": email,
    })

    }
    
    );


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