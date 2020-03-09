import TimelinePost from '../../Model/TimelinePost';

export const GET_TIMELINE = 'GET_TIMELINE';

/*
export const fetchTimeline = () => {
    return async dispatch => {
        const response = await fetch(
            "https://europe-west2-bluej-pintro-project.cloudfunctions.net/generate_timeline",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },body:JSON.stringify({
                email:"ben2@gmail.com"
                })
                
            }
        );
       const resData = await response.text();
        console.log(resData);
        dispatch({type: GET_TIMELINE,timelinePosts:[]});

    };
    
};

*/

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

