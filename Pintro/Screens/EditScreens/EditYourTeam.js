import React, { useState } from 'react';
import { View,StyleSheet,Text,TextInput,Picker,Alert,ScrollView } from 'react-native';
import Colors from '../../Constants/Colors';
import BlackTag from '../../Components/BlackTag';
import TeamMember from '../../Components/TeamMember';
import User from '../../Model/User';
import { BearerToken } from '../../Constants/BearerToken';

const EditYourTeam = props => {
    const [searchKeyword,setSearchKeyword] = useState();
    const [teamMembers,setMembers] = useState([]);
    const [teamEmails,setEmails] = useState([])

    function onTextChanged(searchWord) {
        setSearchKeyword(searchWord);
    }

    function onPressRemove(value) {
        setMembers(teamMembers.filter((element)=>element!==value));
    }

    async function handleKeyPress() {
        const response = await fetch('https://bluej-pintro-project.appspot.com/users/' + searchKeyword,
        {
            method: 'GET',
            headers: {
                'Content-type': 'application/json',
                'Authorization': BearerToken       
            },
            redirect: 'follow'
        })
        console.log(response.status);
        if(!response.ok) {
            if(response.status == '404') {
                Alert.alert('No results found','No users were found that match your search');
            } else if (response.status == '422') {
                Alert.alert('Invalid search term','Please enter an email address');
            } else {
                const errorResData = await response.json();
                console.log(errorResData);
                let message = 'Something went wrong';
                throw new Error(message);
            }
        } else {
            const resData = await response.json();

            if(resData === []){
                Alert.alert('No results found','No users were found that match your search');
            } else {
                let searchedUser = new User(resData.education,resData.email,resData.full_name,resData.gender,resData.job_title,resData.location,resData.password,resData.phone,resData.preferred_name,resData.profile_image,resData.profile_type,"",resData.short_bio,resData.story);
                setEmails(searchedUser.email);
                teamMembers.push(searchedUser);
                console.log(teamEmails);
            }
        }
    }

    async function onPressDone() {
        console.log("You pressed done");
        console.log(teamMembers);
        /*try{
            const response = await fetch('https://bluej-pintro-project.appspot.com/users/' + props.navigation.state.params.business.email,
                {
                    method: 'PUT',
                    headers: {
                        'Content-type': 'application/json',
                        'Authorization': BearerToken
                    },
                    redirect: 'follow',
                    body: JSON.stringify({
                        email: props.navigation.state.params.business.email,
                        password: props.navigation.state.params.business.password,
                        full_name: props.navigation.state.params.business.full_name,
                        profile_image: props.navigation.state.params.business.profile_image,
                        phone: props.navigation.state.params.business.phone,
                        location: props.navigation.state.params.business.location.replace(/'/g,"\\'"),
                        short_bio: props.navigation.state.params.business.short_bio.replace(/'/g,"\\'"),
                        story: props.navigation.state.params.business.story.replace(/'/g,"\\'"),
                        tags: props.navigation.state.params.business.tags,
                        date_founded: props.navigation.state.params.business.date_founded,
                        company_size: props.navigation.state.params.business.company_size,
                        funding: props.navigation.state.params.business.funding,
                        team_members: teamMembers,
                        seeking_investment: props.navigation.state.params.business.seeking_investment,
                        currently_hiring: props.navigation.state.params.business.currently_hiring
                    })
                }
            );
            console.log(response.status);
            dispatch(BusinessActions.getBusiness(props.navigation.state.params.business.email));  
        } catch (error) {
            console.log(error);
        }*/   
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
            {teamMembers.map((item) => <TeamMember key={item.email} props={props.TeamMember} callback={value => onPressRemove(value)} userObj={item}/>)}
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