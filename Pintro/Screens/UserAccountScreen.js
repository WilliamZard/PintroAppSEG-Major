import React, { useState } from 'react';
import { useSelector,useDispatch } from 'react-redux';
import { Dimensions, StyleSheet, View, Text, Image, ScrollView, TouchableOpacity, FlatList } from 'react-native';
import MsgMe from '../Components/MsgMe.js';
import BlackTag from '../Components/BlackTag.js';
import WhiteTag from '../Components/WhiteTag.js';
import HelpMeWith from '../Components/HelpMeWith.js';
import Edit from '../Components/Edit.js';
import PencilBlack from '../Components/PencilBlack.js';
import Colors from '../Constants/Colors.js';
import JourneyPoint from '../Components/JourneyPoint.js';
import TimelinePostComponent from '../Components/TimelinePostComponent.js';
import UserProfileCircle from '../Components/UserProfileCircle.js';
import UserMoodCircle from '../Components/UserMoodCircle.js';
import Svg, { Ellipse } from "react-native-svg";
import ConnectButton from '../Components/ConnectButton.js';

/**
 * The account page for a personal account
 *  being viewed by another user consisting 
 * of a view for: there name and profile picture and location,
 * a follow and message me and edit button, there story, what they can help you with
 * what they need help with and there experience
 * @param {*} props
 */
const UserAccountScreen = props => {
    const user = useSelector(state => state.user.userObj);
    const [lines, setLineNumber] = useState(2);
    const [see, setSee] = useState("More");
    const [more, setMore] = useState(true);

    function onPressMore(){
        if(more){
            setLineNumber(10);
            setSee("See less");
            setMore(false);
        } 
        else{
            setLineNumber(4);
            setSee("More");
            setMore(true);
        }   
    }

    function switchEditStory() {
        props.navigation.navigate('Story', {user: userObj});
    }

    function switchEditPassions() {
        props.navigation.navigate('Passions', {user: userObj});
    }

    function switchEditHelpOthers() {
        props.navigation.navigate('HelpOthers', {user: userObj});
    }

    function switchEditExperience() {
        props.navigation.navigate('Experience', {user: userObj});
    }

    function switchEditPhoto() {
        props.navigation.navigate('Photo', {user: userObj});
    }
  
    function onPressBack() {
        props.navigation.goBack(null);
    }

    function onConnectPress() {
        //Follow Request functionality
    }

    return(
        <ScrollView style={styles.background}>
            <View style={styles.actionContainer}>
                <TouchableOpacity style={{flex: 1}} onPress={() => onPressBack()}>
                    <Image source={require('../assets/backBlack.png')} style={styles.back}/>
                </TouchableOpacity>
                <TouchableOpacity>
                    <Image source={require('../assets/shareBlack.png')} style={styles.shareImage}/>
                </TouchableOpacity> 
            </View>
            <View style={styles.accountTop}>
                <View style={styles.ellipseStackRow}>
                    <View style={styles.ellipseStack}>
                        <Svg viewBox="0 0 90.27 90.39" style={styles.profileImage}>
                            <Ellipse
                                strokeWidth={1}
                                fill="#1a1a1a"
                                stroke="rgba(230, 230, 230,1)"
                                cx={45}
                                cy={45}
                                rx={45}
                                ry={45}
                            ></Ellipse>
                        </Svg>
                        <Svg viewBox="0 0 45 45" style={styles.moodCircle}>
                            <Ellipse
                            strokeWidth={1}
                            fill="rgba(246,171,72,1)"
                            stroke="rgba(230, 230, 230,1)"
                            cx={22}
                            cy={22}
                            rx={22}
                            ry={22}
                            ></Ellipse>
                        </Svg>                    
                    </View>
                    <View>
                        <Text style={styles.fullnameBlack}>{userObj.full_name}</Text>
                        <Text style={styles.currentJob}>{userObj.job_title}</Text>
                        <Text style={styles.shortBio}>{userObj.short_bio}</Text>
                        <Text style={styles.location}>{userObj.location}</Text>
                        <PencilBlack onPress={() => switchEditPhoto()}/>
                    </View>    
                </View>
            </View>
            <View style= {styles.rowContainer}>
                <ConnectButton props={props.ConnectButton}/> 
                <MsgMe props={props.MsgMe}>MESSAGE ME</MsgMe>
                <Edit props={props.Edit}>. . .</Edit>
            </View>
            <ScrollView style={styles.helpContainer} horizontal={true}>
                    <HelpMeWith props={props.HelpMeWith}>{(userObj.passions[0]!==undefined)? userObj.passions[1].toUpperCase() : null}</HelpMeWith>
                    <HelpMeWith props={props.HelpMeWith}>{(userObj.passions[1]!==undefined)? userObj.passions[1].toUpperCase() : null}</HelpMeWith>
                    <HelpMeWith props={props.HelpMeWith}>{(userObj.passions[2]!==undefined)? userObj.passions[1].toUpperCase() : null}</HelpMeWith>
            </ScrollView>
            <View>
            <PencilBlack onPress={() => switchEditStory()}/>
            <Text style={styles.myStoryHead}>My Story</Text>
                <Text style={styles.storyContent} numberOfLines={lines}>
                    {userObj.story}
                </Text>
            <Text style={styles.more} onPress={() => onPressMore()}>{see}</Text>
            </View>
            <ScrollView style={styles.tagContainer} horizontal={true}>
            <Text style={styles.myStoryHead}>I am passionate about</Text>
                <BlackTag props={props.BlackTag}>{(userObj.passions[0]!==undefined)? userObj.passions[0].toUpperCase() : null}</BlackTag>
                <BlackTag props={props.BlackTag}>{(userObj.passions[1]!==undefined)? userObj.passions[1].toUpperCase() : null}</BlackTag>
                <BlackTag props={props.BlackTag}>{(userObj.passions[2]!==undefined)? userObj.passions[2].toUpperCase() : null}</BlackTag>
                <BlackTag props={props.BlackTag}>{(userObj.passions[3]!==undefined)? userObj.passions[0].toUpperCase() : null}</BlackTag>
                <BlackTag props={props.BlackTag}>{(userObj.passions[4]!==undefined)? userObj.passions[1].toUpperCase() : null}</BlackTag>
                <BlackTag props={props.BlackTag}>{(userObj.passions[5]!==undefined)? userObj.passions[2].toUpperCase() : null}</BlackTag>
            <PencilBlack onPress={() => switchEditPassions()}/>
            </ScrollView>
            <ScrollView style={styles.tagContainer} horizontal={true}>
            <Text style={styles.myStoryHead}>I can help with</Text>
            <PencilBlack onPress={() => switchEditHelpOthers()}/>
                <WhiteTag props={props.WhiteTag}>{(userObj.help_Others[0]!==undefined)? userObj.help_Others[0].toUpperCase() : null}</WhiteTag>
                <WhiteTag props={props.WhiteTag}>{(userObj.help_Others[1]!==undefined)? userObj.help_Others[1].toUpperCase() : null}</WhiteTag>
                <WhiteTag props={props.WhiteTag}>{(userObj.help_Others[2]!==undefined)? userObj.help_Others[2].toUpperCase() : null}</WhiteTag>
                <WhiteTag props={props.WhiteTag}>{(userObj.help_Others[3]!==undefined)? userObj.help_Others[0].toUpperCase() : null}</WhiteTag>
                <WhiteTag props={props.WhiteTag}>{(userObj.help_Others[4]!==undefined)? userObj.help_Others[1].toUpperCase() : null}</WhiteTag>
                <WhiteTag props={props.WhiteTag}>{(userObj.help_Others[5]!==undefined)? userObj.help_Others[2].toUpperCase() : null}</WhiteTag>
            </ScrollView>
            <View>
                <View style={styles.rowContainer}>
                <Text style={styles.journey}>Experience</Text>
                <PencilBlack onPress={() => switchEditExperience()}/>
                    <JourneyPoint default={"Work Experience:"} userData={userObj.years_in_industry}/>
                    <JourneyPoint default={"Industry:"} userData={userObj.Industry}/>
                    <JourneyPoint default={"Current Company"} userData={userObj.current_Company}/>
                    <JourneyPoint default={"Previous Company:"} userData={userObj.previous_Company}/>
                    <JourneyPoint default={"Education:"} userData={userObj.university}/>
                    <JourneyPoint default={"Academic Level:"} userData={userObj.academic_level}/>
                </View>
            </View>
        </ScrollView>
    );
};

const styles = StyleSheet.create({
    accountTop: {
        marginBottom: 0,
        marginTop: 15,
        width: 322,
        height: 115,
        backgroundColor: Colors.pintroWhite,
    },
    helpUs_button: {
        color: Colors.pintroWhite
    },
    actionContainer: {
        flexDirection: 'row',
        marginTop: 30,
        marginBottom: 10,
    },
    back: {
        height: 20, 
        width: 20, 
        marginLeft: 10,
    },
    shareImage: {
        height: 20, 
        width: 20,  
        marginRight: 20,

    },
    rowContainer: {
        flexDirection: 'row',
    },
    profileImage:{
        top: 0,
        left: 0,
        width: 90,
        height: 90,
        position: "absolute"        
    },
    moodCircle:{
        top: 55,
        left: 55,
        width: 45,
        height: 45,
        position: "absolute"
    },
    ellipseStack:{
        width: 60,
        height: 50,
    },
    ellipseStackRow: {
        height: 40,
        flexDirection: "row",
        marginTop: 10,
        marginLeft: 30,
        marginRight: 10,
    },
    fullnameBlack: {
        fontSize: 16,
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        marginLeft: 60,
    },
    currentJob: {
        fontSize: 14,
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        marginLeft: 60,
    },
    shortBio: {
        fontSize: 10,
        color: Colors.pintroGrey,
        fontFamily: 'Poppins-Light',
        marginLeft: 60,
    },
    location: {
        fontSize: 10,
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Light',
        marginLeft: 60,
    },
    helpContainer: {
        flexDirection: 'row',
        paddingLeft: 30,
        paddingRight: 30,
    },
    myStoryHead: {
        fontSize: 15,
        paddingLeft: 20,
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold'        
    },
    storyContent: {
        marginLeft: 30,
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize:12,
        marginRight: 20,
    },
    more: {
        marginLeft: 20,
        color: Colors.pintroYellow,
        fontFamily: 'Poppins-Bold',
        fontSize:12
    },
    tagContainer: {
        flexDirection: 'row',
        marginTop: 10,
        marginHorizontal: 0,
    },
    background: {
        backgroundColor: Colors.pintroWhite,
        flex: 1,
    }
});

export default UserAccountScreen;