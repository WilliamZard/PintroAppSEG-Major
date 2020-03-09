import React,{useEffect,useState,useCallback} from 'react';
import {useSelector, useDispatch} from 'react-redux';
import {
    View,
    Text,
    Button,
    StyleSheet,
    FlatList,
    RefreshControl,
    ActivityIndicator
} from 'react-native';
import * as timelineActions from '../../store/actions/timeline';
import TimelinePostComponent from '../../Components/TimelinePostComponent';

const HomeScreen = props => {
    const [error, setError] = useState();
    const [refreshing, setIsRefreshing] = useState(false);
const loadPosts = useCallback(
    async () => {
        setError(null);
      setIsRefreshing(true);
        try{
            await  dispatch(timelineActions.fetchTimeline());
        }catch (e){
            setError(e.message);
        }
        setIsRefreshing(false);
    },[dispatch,setIsLoading,setError]
);

    const [isLoading,setIsLoading] = useState(false);
const timelinePosts = useSelector(state => state.timelinePosts.availablePosts);

const dispatch = useDispatch();

useEffect(()=>{
    setIsLoading(true);
    loadPosts().then(() => { setIsLoading(false);});
   
   },[dispatch,loadPosts]);

if(isLoading){
    return(<View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
        <ActivityIndicator size='large' color='orange'/>
    </View>);
}

return(
    
<View style = {styles.screen}>

  <FlatList
  onRefresh={loadPosts}
  refreshing={refreshing}
  style={{width:'100%'}}
  numColumns={2}
   data={timelinePosts}
   keyExtractor={item => item.uuid}
   renderItem={
       itemData => (
        
<TimelinePostComponent uuid={itemData.item.uuid}  content={itemData.item.content}  modified={itemData.item.modified}/>

       )
   }
  />
</View>



);


};


const styles = StyleSheet.create({
screen:{
    flex:1,
    justifyContent:'center',
    alignItems:'center'
}

});

export default HomeScreen;