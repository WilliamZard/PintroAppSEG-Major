import React, {useState} from 'react';
import {useSelector, useDispatch} from 'react-redux';
import { StyleSheet, Text, View, Button, FlatList,TextInput,ScrollView,TouchableOpacity } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import RNPickerSelect from 'react-native-picker-select';
import Colors from '../../Constants/Colors';
import Color from '../../Constants/Colors';
import {ListItem,SearchBar } from 'react-native-elements';
import * as userAction from '../../store/actions/user';
const EditPassion = props => {
    const dispatch = useDispatch();
    const [currentlyChanging,setCurrentlyChanin] = useState(false);
    const [searchKeyword,setSearchKeyword] = useState();
    const [suggestions,setSuggestions] = useState([]);
    const [suggestedItems,setItems] = useState([])
    const [chosenTags,setChosenTags] = useState(useSelector(state => state.user.passions));
    
    const loadedTags = useSelector(state => state.tags.passionTags);
    const loadedTagsShuffled = useSelector(state => state.tags.passionTagsSHUFFLED);

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


    const doneHandler = async () => {
        await dispatch(userAction.update_passions(chosenTags));
        props.navigation.navigate({routeName:'Account'})
        
    }

    return(
        <KeyboardAwareScrollView
        resetScrollToCoords={{ x: 0, y: 0 }}
        contentContainerStyle={styles.container}
        scrollEnabled={true}>
        <View>
            <View style={{marginHorizontal:30,marginTop:30}}>
                <View style={{marginVertical:20}}>
                    <Text style={{fontSize:25,fontFamily:'Poppins-Bold'}}>What are your passions?</Text>
                </View>
            <View style={{marginBottom:30}}>
            <Text style={styles.aboveInputText}>Choose your passions(6 minimum). Current Selection:</Text>
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
            <Text>Choose from the full list</Text>
           
            <SearchBar

containerStyle={{width: 300,backgroundColor:'#efeff0',width:'100%'}}
inputContainerStyle={{backgroundColor:'white' ,width:'100%',}}
onChangeText={searchWord => onTextChanged(searchWord)}
value={searchKeyword}
clearIcon={null}/>
{suggestedItems}

<Text style={styles.aboveInputText}>or choose from the most popular</Text>
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
                    <View style={{marginTop:20}}> 
                        <TouchableOpacity 
                        style={{backgroundColor:'black',height:40,borderRadius:30, alignItems:'center',justifyContent:'center'}}
                        onPress={()=>{
                           doneHandler()
                        }}
                        ><Text style={{color:'white'}}>Done</Text></TouchableOpacity>
            </View>
               </View>
        </View>
        </KeyboardAwareScrollView>
    );
};



const styles = StyleSheet.create({
    horizintalLineStyle:{
        borderBottomColor: 'black',
         borderBottomWidth: StyleSheet.hairlineWidth,
         marginBottom:10
    },tagButton:{
    backgroundColor:'grey',
          
        padding:10,
        borderRadius:20,
        margin:10,

        },choosenButton:{
             backgroundColor:'black',
            borderWidth: 1,
            padding:10,
            borderRadius:20,
            margin:10,
            },
});


export default EditPassion;