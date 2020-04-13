import React, { useState } from 'react';
import { View,StyleSheet,Text,TextInput,Picker,Alert,ScrollView } from 'react-native';
import Colors from '../../Constants/Colors';
import BlackTag from '../../Components/BlackTag';
import TeamMember from '../../Components/TeamMember';
import { BearerToken } from '../../Constants/BearerToken';
import User from '../../Model/User';
import { useDispatch } from 'react-redux';
import * as RequestActions from '../../store/actions/request';

const EditYourTeam = props => {
    const dispatch = useDispatch();
    const [searchKeyword,setSearchKeyword] = useState();
    const [teamMembers,setMembers] = useState([]);
    const [teamEmails,setEmails] = useState((props.navigation.state.params.business.teamMembers)? props.navigation.state.params.business.teamMembers : []);
    const [searchedUser,setUser] = useState();

    function onTextChanged(searchWord) {
        setSearchKeyword(searchWord);
    }

    function onPressRemove(value) {
        setMembers(teamMembers.filter((element) => element!==value));
        setEmails(teamEmails.filter((element) => element!==value.email));
    }

    async function handleKeyPress() {
        console.log(searchKeyword);

        try {
            const response = await fetch('https://bluej-pintro-project.appspot.com/users/' + searchKeyword,
                {
                    method: 'GET',
                    headers: {
                    'Content-Type': 'application/json',
                    'Authorization': BearerToken
                    },
                    redirect: 'follow'
                } 
            );
            console.log("Get user: " + (response.status));
      
            if(!response.ok) {
                if(response.status == '404') {
                    Alert.alert('No results found','No users were found that match your search');
                    setUser(undefined);
                } else if (response.status == '422') {
                    Alert.alert('Invalid search term','Please enter an email address');
                    setUser(undefined);
                } else {
                    const errorResData = await response.json();
                    console.log(errorResData);
                    let message = 'Something went wrong';
                    throw new Error(message);
                }
            } else {
                const resData = await response.json();
                const resUser = new User(
                    resData.education,
                    resData.email,
                    resData.full_name,
                    resData.gender,
                    resData.job_title,
                    resData.location,
                    resData.password,
                    resData.phone,
                    resData.preferred_name,
                    resData.profile_image,
                    "",
                    "",
                    resData.short_bio,
                    resData.story
                );
                setUser(resUser);
                if(resData !== undefined) {
                    console.log("searched user: " + resData.email);
                    if(teamEmails.includes(resData.email)){
                        console.log("Do not add it ");
                    } else {
                        teamEmails.push(resData.email);
                        teamMembers.push(resUser);
                    }
                }
            }
        } catch (error) {
            console.log(error);
        }

        setEmails(teamEmails);
        setMembers(teamMembers);
    }

    async function onPressDone() {
        console.log("You pressed done");
        console.log("team emails: " + teamEmails.length);
        if(teamEmails.length > 0) {
            teamEmails.map((item) => dispatch(RequestActions.requestAfil(props.navigation.state.params.business.email,item)));
        }
    }

    return (
    <ScrollView>
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
            {(teamMembers==[])? null: teamMembers.map((item) => 
                <TeamMember 
                key={item.email} 
                props={props.TeamMember} 
                callback={value => onPressRemove(value)} 
                userObj={item}/>
            )}
            <BlackTag props={props.BlackTag} onPress={() => onPressDone()}>Done</BlackTag>
        </View>
    </ScrollView>
        
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