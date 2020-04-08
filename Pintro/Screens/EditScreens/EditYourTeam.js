import React, { useState } from 'react';
import {useSelector, useDispatch} from 'react-redux';
import { View,StyleSheet,Text,TouchableOpacity,Image,TextInput,Picker,Alert } from 'react-native';
import { fonts } from '../../Constants/Fonts';
import Colors from '../../Constants/Colors';
import BlackTag from '../../Components/BlackTag';
import TeamMember from '../../Components/TeamMember';
import * as SearchActions from "../../store/actions/search";

const EditYourTeam = props => {
    const dispatch = useDispatch();
    const [searchKeyword,setSearchKeyword] = useState();
    const [teamMembers,setMembers] = useState([]);
    searchResults = useSelector(state => state.actions.usersArray);
    

    function onTextChanged(searchWord) {
        setSearchKeyword(searchWord);
    }

    function onPressRemove(value) {
        setMembers(teamMembers.filter((element)=>element!==value));
    }

    async function handleKeyPress() {
        console.log("Search keyword: " + searchKeyword);
        await dispatch(SearchActions.getResults(searchKeyword));
        console.log("1");
        console.log("Search results length: " + searchResults.length);
        let personProfiles = searchResults.filter((item) => (item.profile_type === "person")? item : null).filter(profile => profile !== null);
        if(personProfiles.length == 0) {
            Alert.alert('No results found','No users were found that match your search');
        } else {
            setMembers(personProfiles);
        }
    }

    function onPressDone() {
        console.log("You pressed done(a lot)");
    }

    return (
        <View style={styles.primaryContainer}>
            <Text style={styles.title}>Edit your team</Text>
            <Text style={styles.search}>Search and invite your people</Text>
            <Text style={styles.subtitle}>Team member name</Text>
            <View style={styles.rowContainer}>
                <TextInput 
                    style={styles.inputText} 
                    onChangeText={value => onTextChanged(value)}
                    onSubmitEditing={() => handleKeyPress()}>
                Start typing...
                </TextInput>
                <Picker style={{borderWidth: 1}}></Picker>
            </View>
            <View style={styles.horizintalLineStyle}/>
            <Text style={styles.subtitle}>Current members:</Text>
            {teamMembers.map((item) => <TeamMember key={item.email} props={props.TeamMember} callback={value => onPressRemove(value)} userObj={item}/>)}
            <BlackTag props={props.BlackTag} onPress={() => onPressDone()}>Done</BlackTag>
        </View>
    )
}

const styles = StyleSheet.create({
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
    inputText: {
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        height: 50, 
        width: 370
    },
    rowContainer: {
        flexDirection: 'row'
    },
    horizintalLineStyle:{
        borderBottomColor: 'black',
        borderBottomWidth: StyleSheet.hairlineWidth,
        marginBottom:30,
        marginTop:10,
    },
    primaryContainer: {
        marginHorizontal: 30,
        paddingTop: 70,
        marginBottom: 20,
    },
    search: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        marginBottom: 50,
    },
    teamContainer: {
        flexDirection: 'row',
        backgroundColor: 'white',
        marginBottom: 10,
        borderRadius: 20,
        width: 370,
        height: 75,
    },
    circleImage: {
        width: 40,
        height: 40,
        borderRadius: 20,
        marginBottom: 10,
        marginTop: 17,
        marginHorizontal: 10,
    },
    textContainer: {
        marginTop: 18,
        flex: 1
    },
    cross: {
        height: 20, 
        width: 20, 
        marginTop: 30, 
        marginRight: 20
    }
})

export default EditYourTeam;