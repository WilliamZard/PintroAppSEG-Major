import React, {useState} from 'react';
import {useSelector, useDispatch} from 'react-redux';
import {
    View,
    Text,
    StyleSheet,
    TextInput,TouchableOpacity,
    ScrollView
} from 'react-native';

import Color from '../../Constants/Colors';
import Colors from '../../Constants/Colors';
import {ListItem,SearchBar } from 'react-native-elements';

const BusinessTags = props => {


    const dispatch = useDispatch();
    const [searchKeyword,setSearchKeyword] = useState();
    const [suggestions,setSuggestions] = useState([]);
    const [suggestedItems,setItems] = useState([])
    const [chosenTags,setChosenTags] = useState([])
    const loadedTags = useSelector(state => state.tags.tagsArray);
    var tagNames = loadedTags.map(function(item) {
        return item['name'];
      });
      function onTextChanged(searchWord) {
        setSearchKeyword(searchWord);
        if (searchWord.length > 2) {
            
            const regex = new RegExp(`^${searchWord}`,'i');
            //console.log(tagList.sort().filter(v => regex.test(v)));
            setSuggestions(tagNames.sort().filter(v => regex.test(v))); 
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
          <ScrollView horizontal={true}>
    {chosenTags.map((tag)=>  <TouchableOpacity key={tag} style ={styles.choosenButton}><Text style={{color:Color.pintroYellow}}>{tag}</Text></TouchableOpacity> )}
                        
                        </ScrollView>
                        </View>   
        </View>
        </View>
        <View style={styles.main}>
        <Text>Choose from the full list</Text>
        <SearchBar

containerStyle={{width: 300,backgroundColor:Colors.pintroBlack}}
inputContainerStyle={{backgroundColor:Colors.pintroBlack ,width: 280,}}
onChangeText={searchWord => onTextChanged(searchWord)}
value={searchKeyword}
clearIcon={null}/>
{suggestedItems}
        <View style={styles.horizintalLineStyle}></View>
        <Text>Or choose from the most popular</Text>
       


        <View style={styles.horizintalLineStyle}></View>
        </View>
        <ScrollView horizontal={true}>
    <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Feminism</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.choosenButton} ><Text style={{color:'white'}}>Coaching</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Mindfulness</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>

 <ScrollView horizontal={true}>
    <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Feminism</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.choosenButton} ><Text style={{color:'white'}}>Coaching</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Mindfulness</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>

 <ScrollView horizontal={true}>
    <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Feminism</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.choosenButton} ><Text style={{color:'white'}}>Coaching</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Mindfulness</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>

 <ScrollView horizontal={true}>
    <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Feminism</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.choosenButton} ><Text style={{color:'white'}}>Coaching</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Mindfulness</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>
 <View style={{marginHorizontal:30}}>
        <TouchableOpacity style={styles.Button} onPress={() =>props.navigation.navigate({routeName:'DetailsBusiness'})}><Text style={styles.TextButton}>Step 2 of 5</Text></TouchableOpacity>
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
        fontSize:14
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