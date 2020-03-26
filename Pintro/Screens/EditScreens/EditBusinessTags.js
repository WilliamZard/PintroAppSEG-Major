import React, { useState } from 'react';
import { View,StyleSheet,Text,Picker } from 'react-native';
import Colors from '../../Constants/Colors.js';
import BlackTag from '../../Components/BlackTag.js';
import GreyTag from '../../Components/GreyTag.js';
import { TextInput, ScrollView } from 'react-native-gesture-handler';
import data2 from '../../Constants/data2.json';
import { ListItem } from 'react-native-elements';
import { fonts } from '../../Constants/Fonts.js';

const EditBusinessTag = props => {
    const [searchKeyword,setSearchKeyword] = useState();
    const [chosenTags,setChosenTags] = useState([]);
    const [suggestions,setSuggestions] = useState([]);
    const [suggestedItems,setItems] = useState([])
    
    var tagNames = data2.map(function(item) {
        return item['name'];
    });

    function onTextChanged(searchWord) {
        setSearchKeyword(searchWord);
        if (searchWord.length > 2) {
            
            const regex = new RegExp(`^${searchWord}`,'i');
            //console.log(tagList.sort().filter(v => regex.test(v)));
            setSuggestions(tagNames.sort().filter(v => regex.test(v))); 
        }
        renderSuggestions();
    }

    function onListItemPress(item) {
        //console.log(item);
       
        setItems(null);
        if(!chosenTags.includes(item)){
            chosenTags.push(item);
            setChosenTags(chosenTags);
        }else{
            setChosenTags(chosenTags.filter((arrayElement)=>arrayElement!==item));
        }
       console.log(chosenTags)
    }

    function renderSuggestions() {
        if(suggestions.length === 0 || searchKeyword.length < 3) {
            setItems(null);
        } else {
            setItems(suggestions.map((item) => 
                <ListItem 
                    key={item}
                    containerStyle={{width: 300, height: 50}} 
                    titleStyle={fonts.story} 
                    title={item}
                    button
                    onPress={() => onListItemPress(item)}
                />)
            );
        }
    }

    return(
        <ScrollView>
            <View style={styles.primaryContainer}>
                <Text style={styles.title}>Edit your Tags</Text>
                <Text style={styles.categorise}>Categorise your business (3 minimum)</Text>
                <Text style={styles.subtitle}>Choose from the full list</Text>
                <View style={styles.rowContainer}>
                    <TextInput 
                    style={styles.inputText} 
                    onChangeText={value => onTextChanged(value)}>
                        Start typing...
                    </TextInput>
                    <Picker style={{borderWidth: 1}}></Picker>
                </View>
                <View style={styles.horizintalLineStyle}/>
                {suggestedItems}
                <Text style={styles.subtitle}>Or choose from the most popular</Text>
                <View style={styles.tagContainer}>
                    <GreyTag props={props.GreyTag}>FEMINISIM</GreyTag>
                    <GreyTag props={props.GreyTag}>START-UP</GreyTag>
                    <GreyTag props={props.GreyTag}>MINDFULNESS</GreyTag>
                </View>
                <View style={styles.tagContainer}>
                    <GreyTag props={props.GreyTag}>PERSONAL GROWTH</GreyTag>
                    <GreyTag props={props.GreyTag}>APP</GreyTag>
                    <GreyTag props={props.GreyTag}>NETWORKING</GreyTag>
                </View>
                <View style={styles.tagContainer}>
                    <GreyTag props={props.GreyTag}>NEUROSCIENCE</GreyTag>
                    <GreyTag props={props.GreyTag}>NUTRITION</GreyTag>
                    <GreyTag props={props.GreyTag}>INNOVATION</GreyTag>
                </View>
                <View style={styles.tagContainer}>
                    <GreyTag props={props.GreyTag}>PRE-SEED</GreyTag>
                    <GreyTag props={props.GreyTag}>DIVERSITY</GreyTag>
                    <GreyTag props={props.GreyTag}>CO-WORKING</GreyTag>
                </View>
                <View style={{marginVertical: 20}}/>
                <BlackTag props={props.BlackTag}>Done</BlackTag>
            </View>
        </ScrollView>
        
    )
}

const styles = {
    horizintalLineStyle:{
        borderBottomColor: 'black',
        borderBottomWidth: StyleSheet.hairlineWidth,
        marginBottom:30,
        marginTop:10,
    },
    title:  {
        color: 'black',
        fontFamily: 'Poppins-Bold',
        fontSize: 28,
    },
    subtitle: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        marginBottom: 10,
    },
    primaryContainer: {
        marginHorizontal: 30,
        paddingTop: 70,
        marginBottom: 20,
    },
    categorise: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        marginTop: 10,
        marginBottom: 50,
    },
    rowContainer: {
        flexDirection: 'row',
    },
    inputText: {
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
    },
    inputText: {
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        height: 50, 
        width: 370
    },
    tagContainer: {
        flexDirection: 'row',
        marginLeft: -35,
        marginBottom: 10,
    },
}

export default EditBusinessTag;