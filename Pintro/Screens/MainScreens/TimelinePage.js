import React,{useEffect,useState,useCallback} from 'react';
import {useSelector, useDispatch} from 'react-redux';
import { StyleSheet, Text, Button, View, ScrollView, TouchableOpacity,
    FlatList,
    RefreshControl,
    ActivityIndicator} from 'react-native';
import Icon from 'react-native-vector-icons/FontAwesome';
import SignInUpButton from '../../Components/SignInUpButton';
import Colors from '../../Constants/Colors';
import { SearchBar } from 'react-native-elements';


import * as timelineActions from '../../store/actions/timeline';
import TimelinePostComponent from '../../Components/TimelinePostComponent';



/**
 * Homescreen timeline page 
 * The screen consists of a scrollable timeline and the buttons heading to other pages.
 * @param {} props 
 */

 
const TimelinePage = props => {
const [currentSearch,setCurrentSearch] = useState(null);
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


const getFiltered = () => {
if(currentSearch===null){
    return timelinePosts;
} else {
    return timelinePosts.filter((post)=>post.content.toUpperCase().includes(currentSearch.toUpperCase()));
}

}

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

    <View style={styles.background}>
        <View style={styles.header}>
                <Text style={styles.pintroText}>pintro<Text style={styles.yellowAccent}>.</Text></Text>
                <View style={{flexDirection:'row',marginTop:5}}>
                    <View style={{width:'50%',alignItems:'center'}}><TouchableOpacity style={{height:40}} onPress={
                   ()=> props.navigation.navigate({routeName:'Map'})
                }><Text>Map</Text></TouchableOpacity></View>
                    <View style={{width:'50%',alignItems:'center',borderColor:'orange',borderBottomWidth:4}}><TouchableOpacity style={{height:40}}><Text>Feed</Text></TouchableOpacity></View>
                </View>
                
        </View>

        <View style={styles.searchView}>
            <SearchBar
                platform="default"
                placeholder="Tap to filter by..."
                placeholderTextColor='black'
                placeholderTextFontFamily="Poppins-Regular"
                round={true}
                searchIcon={false}
                lightTheme={true}
                containerStyle={{ alignItems:'center', justifyContent:'center', width: 345, borderRadius:20,position: 'absolute',top:25, left:20, right:20}}
                inputContainerStyle={{backgroundColor: 'white',width: 330}}
                onChangeText={(text)=>setCurrentSearch(text)}
                value={currentSearch}
            />
           
        </View>

       <View style={{}}>
        <FlatList
        
  onRefresh={loadPosts}
  refreshing={refreshing}
  style={{width:'100%'}}
  numColumns={2}
   data={getFiltered()}
   keyExtractor={item => item.uuid}
   renderItem={
       itemData => (
        
<TimelinePostComponent uuid={itemData.item.uuid}  content={itemData.item.content}  modified={itemData.item.modified} email={itemData.item.user_email}/>

       )
   }
  />
  </View>
       
    </View>
    );
};

const styles = StyleSheet.create({
    backGround: {
        flex:1,
  
    },
    body: {
        //backgroundColor: Colors.pintroWhite,

        paddingBottom: 1000,
        //flex: 1
    },
    searchView: {
        //backgroundColor: Colors.pintroWhite,

        paddingBottom: 90,
        //flex: 1
    },
    header: {
        alignItems: 'center',
        justifyContent: 'center',
        flexDirection: 'column',
        marginTop:30,
        paddingBottom: 0
    },
    pintroText: {
        color: 'black',
        //fontFamily: 'Poppins-Bold',
        fontSize: 40
    },
    yellowAccent: {
        color: Colors.pintroYellow,
        fontSize: 40
    },
    buttonContainer: {
        paddingTop: 20,
        width: '70%',
        fontFamily:'Poppins-Regular'
    },
    textContainer: {
        flexDirection: 'row',
        alignItems: 'center',
        paddingTop: 100
    },
    touchableText: {
        textAlign: 'left',
        color: 'black',
        fontFamily: 'Poppins-Regular',
        fontSize: 10,
        paddingBottom: 0
    },
    touchableContainer: {
        paddingBottom: 0,
        textAlign: 'left',
        flexDirection: 'row',
        justifyContent: 'space-around'
    },
    messageText : {
        color: 'white',
        fontFamily: 'Poppins-Bold',
        textAlign: 'center',
        paddingBottom: 100,
        fontSize: 30
    }
});

export default TimelinePage;