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
            <View style={styles.accountTop}>
                <View style={styles.rowContainer}>
                    <TouchableOpacity style={{flex: 1}} onPress={() => onPressBack()}>
                        <Image source={require('../assets/backWhite.png')} style={styles.back}/>
                    </TouchableOpacity>
                    <TouchableOpacity>
                        <Image source={require('../assets/shareWhite.png')} style={styles.shareImage}/>
                    </TouchableOpacity> 
                </View>
                <Image source={require('../images/blank-profile-picture.png')} style={{ width: 60, height: 60}}/>
                <PencilWhite onPress={() => switchEditPhoto()}/>
                <View>
                    <Text style={fonts.name_black}>John Doe</Text>
                    <Text style={fonts.title_black}>Founder of John Doe industries</Text>
                    <Text style={fonts.bio}>"Upon visualising tig bits I made my glorious snacc company"</Text>
                    <Text style={fonts.location}>King's College London</Text>
                    </View>
            </View>
        </ScrollView>
    );
};

const styles = StyleSheet.create({
    background: {
        backgroundColor: Colors.pintroWhite,
        flex: 1
    },
    accountTop: {
        width: 375,
        height: 160,
        backgroundColor: Colors.pintroWhite,
    },
    helpUs_button: {
        color: Colors.pintroWhite
    },
    back: {
        height: 20, 
        width: 20, 
        marginLeft: 10,
    },
    shareImage: {
        height: 20, 
        width: 20,  
        marginRight: 10,

    },
    rowContainer: {
        flexDirection: 'row'
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