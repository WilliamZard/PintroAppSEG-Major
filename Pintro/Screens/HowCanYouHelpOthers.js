import React, {useState} from 'react';
import { Alert, StyleSheet, Text, View, Button, FlatList,TextInput,ScrollView,TouchableOpacity, ColorPropType } from 'react-native';
import {useSelector, useDispatch} from 'react-redux';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import SignInUpButton from '../Components/SignInUpButton';
import InvertedSignInUpButton from '../Components/InvertedSignInUpButton';
import * as Animatable from 'react-native-animatable';
import {ListItem,SearchBar } from 'react-native-elements';
import GoBack from '../Components/GoBack';
import RNPickerSelect from 'react-native-picker-select';
import Color from '../Constants/Colors';
import { fonts } from '../Constants/Fonts.js';
import Colors from '../Constants/Colors';
import * as userActions from '../store/actions/user';
import * as reqActions from '../store/actions/request';

/**
 * Sign Up Screen to allow the user to sign up. The Screen consists of 5 required input fields,
 * 2 buttons, and the logo. Furthermore, the input fields will move up if the keyboard hides them.
 * 
 * @param {} props 
 */

const WhatAreYourPassions = props => {


const phoneNumber = props.navigation.getParam('phoneToPass');
const email = props.navigation.getParam('emailToPass');
const name = props.navigation.getParam('nameToPass');
const currentJobTitle = props.navigation.getParam('currentJobTitleToPass');
const currentCompany = props.navigation.getParam('currentCompanyToPass');
const story = props.navigation.getParam('storyToPass');
const workExperience = props.navigation.getParam('workExperienceToPass');
const industry = props.navigation.getParam('industryToPass');
const previousCompany = props.navigation.getParam('previousCompanyToPass');
const pastEducation = props.navigation.getParam('pastEducationToPass');
const academicLevel = props.navigation.getParam('academicLevelToPass');
const passions = props.navigation.getParam('passionsToPass');
const photo = props.navigation.getParam('photoToPass');


    const dispatch = useDispatch();
    const [currentlyChanging,setCurrentlyChanin] = useState(false);
    const [searchKeyword,setSearchKeyword] = useState();
    const [suggestions,setSuggestions] = useState([]);
    const [suggestedItems,setItems] = useState([])
    const [chosenTags,setChosenTags] = useState([])

    const loadedTags = useSelector(state => state.tags.helpOthersWithTags);
    const loadedTagsShuffled = useSelector(state => state.tags.helpOthersWithTagsSHUFFLED);

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
       console.log(chosenTags)
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

    const verification = () => {

        if(chosenTags.length<6){
    Alert.alert("Error","Please choose 6 superpowers");
            return false;
        }
        return true;
    };
    return (
        <KeyboardAwareScrollView
            style={{ backgroundColor: '#1a1a1a' }}
            resetScrollToCoords={{ x: 0, y: 0 }}
            contentContainerStyle={styles.container}
            scrollEnabled={true}>
            <View style={styles.backGround}>
                <View style={styles.main}>
                    <View style={styles.inputController}>
                        <Animatable.View animation="fadeIn">

                        <Text style={styles.signInText}>How can you help others?</Text>
                        <View style={styles.BottomMargin}>
                        <Text style={styles.aboveInputText}>Choose your superpowers(6 minimum). Current Selection:</Text>
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
         
                        <Text style={styles.aboveInputText}>Choose from the full list</Text>
                        <SearchBar

                    containerStyle={{width: 300,backgroundColor:Colors.pintroBlack}}
                    inputContainerStyle={{backgroundColor:Colors.pintroBlack ,width: 280,}}
                    onChangeText={searchWord => onTextChanged(searchWord)}
                    value={searchKeyword}
                    clearIcon={null}/>
                {suggestedItems}
                       
                        </Animatable.View>
                        </View>
 <View style={styles.horizintalLineStyle}></View>
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
                            <InvertedSignInUpButton style={{width:'80%'}} 
                         onPress={ //create user

                         ()=> {
                             
                            if(!verification()===false){
                                
                           dispatch(userActions.create_User(industry,academicLevel,currentCompany,email,name,"NA",chosenTags,"NA",passions,phoneNumber,name,previousCompany,photo,story,pastEducation,currentJobTitle,workExperience))
                         props.navigation.navigate({routeName:'BusinessYesNo'})}}
                        
                         }>Finish</InvertedSignInUpButton>
                            
                


                   


                    </View>
                
            </View>

        </KeyboardAwareScrollView>
    );
};


const styles = StyleSheet.create({
    backGround: {
        backgroundColor: '#1a1a1a',
        flex: 1
    },
    main: {
        flex: 1,
        alignItems: 'center',
        paddingTop: 20,
        //justifyContent:'center',
        flexDirection: 'column',
        //backgroundColor:'blue'
    },tagButton:{
    borderColor:'white',
      borderWidth: 1,
    padding:10,
    borderRadius:20,
    margin:10,
    color:'white'
    },choosenButton:{
        borderColor:Color.pintroYellow,
          borderWidth: 1,
        padding:10,
        borderRadius:20,
        margin:10,
        color:Color.pintroYellow
        },
    inputController: {
        flex: 1,
        paddingTop: 0,
        justifyContent: 'flex-start',
        alignContent: 'center',
        width: '80%'

    },
    textContainer: {
        flexDirection: 'row'
    },
    inputTexts: {
        color: 'black'
    },

    inputBox: {
        height: 40,
        textAlign:'left',
        fontFamily: 'Poppins-Light',
        fontWeight: 'normal',
        color:'white'

    }, signInText: {
        color: 'white',
        fontFamily: 'Poppins-Bold',
        fontSize: 25
    },
    aboveInputText:{
        color:'grey',
        fontFamily:'Poppins-Regular'
    },
    horizintalLineStyle:{
        borderBottomColor: 'white',
         borderBottomWidth: StyleSheet.hairlineWidth,
         marginBottom:30,
         marginTop:10
    },backButton:{
        width:'80%',
        alignContent:'flex-start',
        alignItems:'flex-start',

    },
    BottomMargin:{
        marginBottom:60
    },

    inputBoxFullStory: {
        height: 110,
        alignItems:'flex-start',
        justifyContent:'flex-start',
        textAlign:'left',
        fontFamily: 'Poppins-Light',
        fontWeight: 'normal',
        color:'white',
        textAlignVertical:'top'

    },textInputCentered:{
        alignItems: 'flex-start',
        textAlignVertical: 'top',

    },list:{
        flexGrow:1,
  justifyContent:'flex-end',
    //  alignItems:'center'  
    },listItem:{
        borderColor:'#ccc',
        borderWidth: 1,
        padding:15,
        marginVertical:10,
        backgroundColor:'white',
        flexDirection:'row',
        justifyContent:'space-between',
        width:'100%'
    }
});

export default WhatAreYourPassions;
