import React, { useState } from 'react';
import { View,StyleSheet,Text,Picker } from 'react-native';
import Colors from '../../Constants/Colors.js';
import BlackTag from '../../Components/BlackTag.js';
import GreyTag from '../../Components/GreyTag.js';
import { TextInput, ScrollView } from 'react-native-gesture-handler';
import data2 from '../../Constants/data2.json';
import { ListItem } from 'react-native-elements';
import { fonts } from '../../Constants/Fonts.js';
import { useDispatch } from 'react-redux';
import * as BusinessActions from '../../store/actions/business.js';

const EditBusinessTag = props => {
    const dispatch = useDispatch();
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

    function onTagPress(tagName) {
        if(!chosenTags.includes(tagName)){
            chosenTags.push(tagName);
            setChosenTags(chosenTags);
        }else{
            setChosenTags(chosenTags.filter((arrayElement)=>arrayElement!==tagName));
        }
    }

    async function onPressDone() {
        console.log(chosenTags);
        const response = await fetch('https://bluej-pintro-project.appspot.com/businesses/' + props.navigation.state.params.business.email,
            {
                method: 'PUT',
                headers: {
                    'Content-type': 'application/json'
                },
                redirect: 'follow',
                body: JSON.stringify({
                    email: props.navigation.state.params.business.email,
                    password: props.navigation.state.params.business.password,
                    full_name: props.navigation.state.params.business.full_name.replace(/'/g,"\\'"),
                    profile_image: props.navigation.state.params.business.profile_image,
                    phone: props.navigation.state.params.business.phone,
                    location: props.navigation.state.params.business.location.replace(/'/g,"\\'"),
                    short_bio: props.navigation.state.params.business.short_bio.replace(/'/g,"\\'"),
                    story: props.navigation.state.params.business.story.replace(/'/g,"\\'"),
                    tags: chosenTags,
                    date_founded: props.navigation.state.params.business.date_founded,
                    company_size: props.navigation.state.params.business.company_size,
                    funding: props.navigation.state.params.business.funding,
                    team_members: props.navigation.state.params.business.team_members,
                    seeking_investment: props.navigation.state.params.business.seeking_investment,
                    currently_hiring: props.navigation.state.params.business.currently_hiring,
                })
            }
        );
        console.log(response.status);
        dispatch(BusinessActions.getBusiness());
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
                    <GreyTag props={props.GreyTag} callback={value => onTagPress(value)} val={"Feminisim"}>FEMINISIM</GreyTag>
                    <GreyTag props={props.GreyTag} callback={value => onTagPress(value)} val={"Start-up"}>START-UP</GreyTag>
                    <GreyTag props={props.GreyTag} callback={value => onTagPress(value)} val={"Mindulness"}>MINDFULNESS</GreyTag>
                </View>
                <View style={styles.tagContainer}>
                    <GreyTag props={props.GreyTag} callback={value => onTagPress(value)} val={"Personal Growth"}>PERSONAL GROWTH</GreyTag>
                    <GreyTag props={props.GreyTag} callback={value => onTagPress(value)} val={"App"}>APP</GreyTag>
                    <GreyTag props={props.GreyTag} callback={value => onTagPress(value)} val={"Networking"}>NETWORKING</GreyTag>
                </View>
                <View style={styles.tagContainer}>
                    <GreyTag props={props.GreyTag} callback={value => onTagPress(value)} val={"Neuroscience"}>NEUROSCIENCE</GreyTag>
                    <GreyTag props={props.GreyTag} callback={value => onTagPress(value)} val={"Nutrition"}>NUTRITION</GreyTag>
                    <GreyTag props={props.GreyTag} callback={value => onTagPress(value)} val={"Innovation"}>INNOVATION</GreyTag>
                </View>
                <View style={styles.tagContainer}>
                    <GreyTag props={props.GreyTag} callback={value => onTagPress(value)} val={"Pre-seed"}>PRE-SEED</GreyTag>
                    <GreyTag props={props.GreyTag} callback={value => onTagPress(value)} val={"Diversity"}>DIVERSITY</GreyTag>
                    <GreyTag props={props.GreyTag} callback={value => onTagPress(value)} val={"Co-working"}>CO-WORKING</GreyTag>
                </View>
                <View style={{marginVertical: 20}}/>
                <BlackTag props={props.BlackTag} onPress={() => onPressDone()}>Done</BlackTag>
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