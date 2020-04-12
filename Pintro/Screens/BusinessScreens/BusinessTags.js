import React, {useState} from 'react';
import {useSelector, useDispatch} from 'react-redux';
import {
    View,
    Text,
    StyleSheet,
    TextInput,TouchableOpacity,
    ScrollView,
    FlatList
} from 'react-native';

import Color from '../../Constants/Colors';
import Colors from '../../Constants/Colors';
import {ListItem,SearchBar } from 'react-native-elements';

const BusinessTags = props => {



    //NAV
    const seekingInvestments = props.navigation.getParam('seekingInvestmentsToPass');
    const currentlyHiring = props.navigation.getParam('currentlyHiringToPass');
    const companyName = props.navigation.getParam('companyNameToPass');
    const tagLine = props.navigation.getParam('tagLineToPass');
    const companyStory = props.navigation.getParam('companyStoryToPass');


    const dispatch = useDispatch();
    const [searchKeyword,setSearchKeyword] = useState();
    const [suggestions,setSuggestions] = useState([]);
    const [currentlyChanging,setCurrentlyChanin] = useState(false);
    const [suggestedItems,setItems] = useState([])
    const [chosenTags,setChosenTags] = useState([])
  
    const loadedTags = useSelector(state => state.tags.businessTags);
    const loadedTagsShuffled = useSelector(state => state.tags.businessTagsSHUFFLED);

          const favs1 = loadedTagsShuffled.slice(1, 7);
        const favs2 = loadedTagsShuffled.slice(8, 16);
        const favs3 = loadedTagsShuffled.slice(20, 27);

      function onTextChanged(searchWord) {
        setSearchKeyword(searchWord);
        if (searchWord.length > 2) {
            
            const regex = new RegExp(`^${searchWord}`,'i');
            //console.log(tagList.sort().filter(v => regex.test(v)));
            setSuggestions(loadedTags.sort().filter(v => regex.test(v))); 
        }
        if(suggestions!==null){
        renderSuggestions();
        }
    }

    function onListItemPress(item) {
        //console.log(item);
       
        setItems(null);
        setSuggestions(null);
        setSearchKeyword(null);
        if(!chosenTags.includes(item)){
            chosenTags.push(item);
            setChosenTags(chosenTags);
        }else{
            setChosenTags(chosenTags.filter((arrayElement)=>arrayElement!==item));
        }
       console.log(chosenTags);
    }
    
    function renderSuggestions() {
        if(suggestions.length === 0 || searchKeyword.length < 3 || suggestions===null) {
            setItems(null);
        } else {
            setItems(suggestions.map((item) =>{
                
               if(chosenTags.includes(item)){
                return( <ListItem 
                    key={item}
                    containerStyle={{width: 300, height: 50,backgroundColor:'green'}} 
                    title={item}
                    button
                    onPress={() => onListItemPress(item)}
                />);
               }else{
                return( <ListItem 
                    key={item}
                    containerStyle={{width: 300, height: 50}} 
                    title={item}
                    button
                    onPress={() => onListItemPress(item)}
                />);
               }
               
                
            })
            );
        }
    }

    return(<View style={styles.screen}>
        <View style = {styles.header}>
        <View style = {styles.headerBigText}>
        <Text style={styles.headerText}>Your business tags</Text>
        </View>
        <View >
        <Text style={styles.smallHeader}>Categorise your business (3 minimum)</Text>
          <View style={{height:100}}>          
          <FlatList data ={chosenTags} renderItem={
  ({item})=> {
     
    return (<TouchableOpacity key={item} onPress={()=>{
        chosenTags.splice(chosenTags.indexOf(item),1);
           
        setChosenTags(chosenTags);
        setCurrentlyChanin(!currentlyChanging);

    }} style ={styles.choosenButton}><Text style={{color:Color.pintroYellow}}>{item}</Text></TouchableOpacity>);
  }}
 keyExtractor={item => item}
 horizontal={true}
 extraData={currentlyChanging}
 />
                        </View>   
        </View>
        </View>
        <View style={styles.main}>
        <Text>Choose from the full list</Text>
        <SearchBar

containerStyle={{width: 300,backgroundColor:Colors.pintroBlack,borderRadius:30}}
inputContainerStyle={{backgroundColor:Colors.pintroBlack ,width: 280,borderRadius:20}}
onChangeText={searchWord => onTextChanged(searchWord)}
value={searchKeyword}
clearIcon={null}/>
{suggestedItems}
        <View style={styles.horizintalLineStyle}></View>
        <Text>Or choose from the most popular</Text>
       


        <View style={styles.horizintalLineStyle}></View>
        </View>
        <FlatList data ={favs1} renderItem={
  ({item})=> {
     
      if(chosenTags.includes(item)){
        return (<TouchableOpacity key={item} onPress={()=>{
            chosenTags.splice(chosenTags.indexOf(item),1);
        setChosenTags(chosenTags);
        setCurrentlyChanin(!currentlyChanging);
        }}style ={styles.choosenButton}><Text style={{color:Color.pintroYellow}}>{item}</Text></TouchableOpacity>);
      }else{
        return (<TouchableOpacity key={item}  onPress={()=>{
          
          
            chosenTags.push(item);
           
            setChosenTags(chosenTags);
            setCurrentlyChanin(!currentlyChanging);
        }} style ={styles.tagButton}><Text style={{color:'white'}}>{item}</Text></TouchableOpacity>);
      }
  }}
 keyExtractor={item => item}
 horizontal={true}
 extraData={currentlyChanging}
 />

<FlatList data ={favs2} renderItem={
  ({item})=> {
     
      if(chosenTags.includes(item)){
        return (<TouchableOpacity key={item} onPress={()=>{
            chosenTags.splice(chosenTags.indexOf(item),1);
        setChosenTags(chosenTags);
        setCurrentlyChanin(!currentlyChanging);
        }}style ={styles.choosenButton}><Text style={{color:Color.pintroYellow}}>{item}</Text></TouchableOpacity>);
      }else{
        return (<TouchableOpacity key={item}  onPress={()=>{
          
          
            chosenTags.push(item);
           
            setChosenTags(chosenTags);
            setCurrentlyChanin(!currentlyChanging);
        }} style ={styles.tagButton}><Text style={{color:'white'}}>{item}</Text></TouchableOpacity>);
      }
  }}
 keyExtractor={item => item}
 horizontal={true}
 extraData={currentlyChanging}
 />

<FlatList data ={favs3} renderItem={
  ({item})=> {
     
      if(chosenTags.includes(item)){
        return (<TouchableOpacity key={item} onPress={()=>{
            chosenTags.splice(chosenTags.indexOf(item),1);
        setChosenTags(chosenTags);
        setCurrentlyChanin(!currentlyChanging);
        }}style ={styles.choosenButton}><Text style={{color:Color.pintroYellow}}>{item}</Text></TouchableOpacity>);
      }else{
        return (<TouchableOpacity key={item}  onPress={()=>{
          
          
            chosenTags.push(item);
           
            setChosenTags(chosenTags);
            setCurrentlyChanin(!currentlyChanging);
        }} style ={styles.tagButton}><Text style={{color:'white'}}>{item}</Text></TouchableOpacity>);
      }
  }}
 keyExtractor={item => item}
 horizontal={true}
 extraData={currentlyChanging}
 />

 <View style={{marginHorizontal:30}}>
        <TouchableOpacity style={styles.Button} onPress={() =>props.navigation.navigate({
            routeName:'DetailsBusiness',params:{

                seekingInvestmentsToPass:seekingInvestments,
                currentlyHiringToPass:currentlyHiring,
                companyNameToPass:companyName,
                tagLineToPass:tagLine,
                companyStoryToPass:companyStory,
                BusinessTagsToPass:chosenTags,
                }
            
            })}><Text style={styles.TextButton}>Step 2 of 5</Text></TouchableOpacity>
      </View>
    </View>
    );    
};
const styles= StyleSheet.create({
    screen:{
        flex:1,
        backgroundColor:'white'
    },header:{
        marginTop:0,
        alignItems:'flex-start',
       
    },headerText:{
        fontSize:35
    },headerBigText:{
        marginHorizontal:30,
        marginBottom:20
    },smallHeader:{
        fontSize:14,
        marginHorizontal:30
    },headerSmallText:{
        marginHorizontal:30
    },
    horizintalLineStyle:{
        borderBottomColor: 'black',
         borderBottomWidth: StyleSheet.hairlineWidth,
         marginBottom:30,
         marginTop:10
    },main:{
        marginHorizontal:30,
        marginTop:50
    },inputBox:{
marginTop:20
    },inputBoxFullStory: {
        height: 110,
        alignItems:'flex-start',
        justifyContent:'flex-start',
        textAlign:'left',
        fontFamily: 'Poppins-Light',
        fontWeight: 'normal',
        color:'black',
        textAlignVertical:'top'

    },checkBoxes:{
        flexDirection:'row',
      marginVertical:30
    },Button:{
        backgroundColor:'black',
        height:40,
        borderRadius:27,
        alignItems:'center',
        justifyContent:'center',
        marginBottom:50,
    },TextButton:{
        color:'white'
    },
    tagButton:{
        backgroundColor:'grey',
        padding:10,
        borderRadius:20,
        margin:10,
        color:'black',
        height:45
        },
        choosenButton:{
        backgroundColor:'black',
        borderWidth: 1,
        padding:10,
        borderRadius:20,
        margin:10,
        color:'white',
        height:45
            },


});

export default BusinessTags;