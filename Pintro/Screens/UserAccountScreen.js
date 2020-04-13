import React, { useState } from 'react';
import { useSelector,useDispatch } from 'react-redux';
import { Dimensions, StyleSheet, View, Text, Image, ScrollView, TouchableOpacity, FlatList } from 'react-native';
import FollowMe from '../Components/FollowMe.js';
import MsgMe from '../Components/MsgMe.js';
import BlackTag from '../Components/BlackTag.js';
import WhiteTag from '../Components/WhiteTag.js';
import HelpMeWith from '../Components/HelpMeWith.js';
import Edit from '../Components/Edit.js';
import { fonts } from '../Constants/Fonts.js';
import PencilBlack from '../Components/PencilBlack.js';
import PencilWhite from '../Components/PencilWhite.js';
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
        //Do something
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
                        <Text style={styles.fullnameBlack}>John Doe</Text>
                        <Text style={styles.currentJob}>Founder of John Doe industries</Text>
                        <Text style={styles.shortBio}>"Upon visualising tig bits I made my glorious snacc company"</Text>
                        <Text style={styles.location}>King's College London</Text>
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
                    <HelpMeWith props={props.HelpMeWith}>Business Modelling</HelpMeWith>
                    <HelpMeWith props={props.HelpMeWith}>Crepe Investments</HelpMeWith>
                    <HelpMeWith props={props.HelpMeWith}>Home Workouts</HelpMeWith>
            </ScrollView>
        </ScrollView>
    );
};

/*
{userObj.full_name}
{userObj.job_title}
{userObj.short_bio}
{userObj.location}
*/

const styles = StyleSheet.create({
    accountTop: {
        marginBottom: 0,
        marginTop: 15,
        width: 320,
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
        fontSize: 12,
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
    myStoryHead: {
        fontSize: 12,
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold'        
    },
    background: {
        backgroundColor: Colors.pintroWhite,
        flex: 1,
    }
});

/*
            <View style={styles.accountTop}>
                <Image source={require('../images/blank-profile-picture.png')} style={{ width: 60, height: 60}}/>
                <View>
                    <Text style={fonts.name_black}>John Doe</Text>
                    <Text style={fonts.title_black}>Founder of John Doe industries</Text>
                    <Text style={fonts.bio}>"Upon visualising tig bits I made my glorious snacc company"</Text>
                    <Text style={fonts.location}>King's College London</Text>
                    </View>
            </View>
            <View style={styles.rowContainer}>
                <FollowMe props={props.FollowMe}>+ FOLLOW ME</FollowMe>
                <MsgMe props={props.MsgMe}>MESSAGE ME</MsgMe>
                <Edit props={props.Edit}>. . .</Edit>
            </View>
            <View>
                <ScrollView> 
                    <HelpMeWith props={props.HelpMeWith}>interdimensional travel</HelpMeWith>
                    <HelpMeWith props={props.HelpMeWith}>find the szechuan sauce</HelpMeWith>
                    <HelpMeWith props={props.HelpMeWith}>Heists</HelpMeWith>
                </ScrollView>
            </View>
            <View>
                <Text style={fonts.title_black}>My Story</Text>
                <Text style={fonts.story}>
                Some really really really long text in latin that 
                sounds really fancy.
                </Text>
                <Text style={fonts.more_yellow}>More</Text>
            </View>
            <View>
                <Text style={fonts.title_black}>Talk to me about</Text>
                <View style={styles.rowContainer}>
                    <BlackTag props={props.BlackTag}>Rick and Morty</BlackTag>
                    <BlackTag props={props.BlackTag}>Comedy</BlackTag>
                    <BlackTag props={props.BlackTag}>Memes</BlackTag>
                </View>
            </View>
            <View>
                <Text style={fonts.title_black}>I can help with</Text>
                <View style={styles.rowContainer}>
                    <WhiteTag props={props.WhiteTag}>Cooking</WhiteTag>
                    <WhiteTag props={props.WhiteTag}>My golf game</WhiteTag>
                    <WhiteTag props={props.WhiteTag}>Oooweee</WhiteTag>
                </View>
            </View> 
            <View>
                <Text style={fonts.title_black}>Experience</Text>
                <View>
                    <Text style={fonts.title_black}>Work Experience:</Text><Text style={fonts.story}>DC</Text>
                    <Text style={fonts.title_black}>Industry:</Text><Text style={fonts.story}>Sending VKs</Text>
                </View>
            </View>
            <View>
                <Text style={fonts.title_black}>Groups</Text><Text style={fonts.more_white}>See all</Text>
                <View style={styles.name_title}>
                    <Image source={require('../images/blank-profile-picture.png')} />
                    <Text style={fonts.title_black}>Group 1</Text>
                    <Text style={fonts.story}>69 members</Text>
                </View>
                <View style={styles.name_title}>
                    <Image source={require('../images/blank-profile-picture.png')} />
                    <Text style={fonts.title_black}>Group 2</Text>
                    <Text style={fonts.story}>42 members</Text>
                </View>
            </View>
            <View>
                <Text style={fonts.title_black}>Community</Text><Text style={fonts.more_white}>See all</Text>
                <View>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 30, width: 30}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 30, width: 30}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 30, width: 30}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 30, width: 30}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 30, width: 30}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 30, width: 30}}/></Button>
                </View>
            </View>
            <View>
                <Text style={fonts.name_title}>Recommendations</Text>
                <View>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 70, width: 70}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 70, width: 70}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 70, width: 70}}/></Button>
                </View>
            </View>
*/

export default UserAccountScreen;