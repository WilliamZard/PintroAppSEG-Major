import React, {useState} from 'react';
import {useSelector, useDispatch} from 'react-redux';
import { StyleSheet, Text, View, Button, FlatList,TextInput,ScrollView,TouchableOpacity } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import RNPickerSelect from 'react-native-picker-select';
import Colors from '../../Constants/Colors';
import Color from '../../Constants/Colors';
import {ListItem,SearchBar } from 'react-native-elements';
const EditHelpOthers = props => {
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
    return(
        <KeyboardAwareScrollView
        resetScrollToCoords={{ x: 0, y: 0 }}
        contentContainerStyle={styles.container}
        scrollEnabled={false}>
        <View>
            <View style={{marginHorizontal:30,marginTop:30}}>
                <View style={{marginVertical:20}}>
                    <Text style={{fontSize:25,fontFamily:'Poppins-Bold'}}>How can you help others?</Text>
                </View>
            <View style={{marginBottom:30}}>
            <Text>Choose your superpowers (6 minimum)</Text>
            </View>
            <Text>Choose from the full list</Text>
            <Text>Your Selection</Text>
            <ScrollView horizontal={true}>
    {chosenTags.map((tag)=>  <TouchableOpacity key={tag} style ={styles.choosenButton}><Text style={{color:'white'}}>{tag}</Text></TouchableOpacity> )}
                        </ScrollView>
            <SearchBar

containerStyle={{width: 300,backgroundColor:'#efeff0',width:'100%'}}
inputContainerStyle={{backgroundColor:'white' ,width:'100%',}}
onChangeText={searchWord => onTextChanged(searchWord)}
value={searchKeyword}
clearIcon={null}/>
{suggestedItems}
<Text style={styles.aboveInputText}>or choose from the most popular</Text>
 <ScrollView horizontal={true}>
    <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'black'}}>Feminism</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.choosenButton} ><Text style={{color:'white'}}>Coaching</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'black'}}>Mindfulness</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'black'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'black'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'black'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>
 <ScrollView horizontal={true}>
 <TouchableOpacity style ={styles.choosenButton}><Text style={{color:'white'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'black'}}>Personal Growth</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'black'}}>EdTech</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'black'}}>Inclusivity</Text></TouchableOpacity>

   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'black'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'black'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>
 <ScrollView horizontal={true}>
 <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'black'}}>Wireframing</Text></TouchableOpacity>
 <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'black'}}>Social Media</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.choosenButton} ><Text style={{color:'white'}}>SEO</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'black'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'black'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'black'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>
 <ScrollView horizontal={true}>
 <TouchableOpacity style ={styles.tagButton}><Text style={{color:'black'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.choosenButton}><Text style={{color:'white'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'black'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>
                    <View style={{marginTop:20}}> 
                        <TouchableOpacity style={{backgroundColor:'black',height:40,borderRadius:30, alignItems:'center',justifyContent:'center'}}><Text style={{color:'white'}}>Done</Text></TouchableOpacity>
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


export default EditHelpOthers;