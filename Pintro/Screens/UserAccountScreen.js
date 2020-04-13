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
import UserActions from '../store/actions/user.js';
import Color from '../Constants/Colors';

/**
 * The account page for a personal account
 *  being viewed by another user consisting 
 * of a view for: there name and profile picture and location,
 * a follow and message me and edit button, there story, what they can help you with
 * what they need help with and there experience
 * @param {*} props
 */
const UserAccountScreen = props => {
 
    const [lines, setLineNumber] = useState(2);
    const [see, setSee] = useState("More");
    const [more, setMore] = useState(true);

    const userObj = useSelector(state => state.user.otherUserObj);
    
    const job_title = useSelector(state => state.user.job_title);
    const currentCompany = useSelector(state => state.user.current_Company);
    const story = useSelector(state => state.user.story);
    const profilePic = useSelector(state => state.user.profile_image);
    const passions = useSelector(state => state.user.passions);
    const helpothers = useSelector(state => state.user.help_others);
    const name = useSelector(state => state.user.full_name);
    const education = useSelector(state => state.user.education);
    const academic_Level = useSelector(state => state.user.academic_Level);
    const years_in_industry = useSelector(state => state.user.years_in_industry);
    const previous_Company = useSelector(state => state.user.previous_Company);
    

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
        console.log("EEE");
        props.navigation.navigate('Story');
    }

    function switchEditPassions() {
        props.navigation.navigate('Passions');
    }

    function switchEditHelpOthers() {
        props.navigation.navigate('HelpOthers');
    }

    function switchEditExperience() {
        props.navigation.navigate('Experience');
    }

    function switchEditPhoto() {
        
        props.navigation.navigate('Photo');
    }
  
   

    function onConnectPress() {
        //Follow Request functionality
    }

    return(
        <ScrollView style={styles.background}>
            <View style={styles.actionContainer}>
            <TouchableOpacity onPress={()=>props.navigation.navigate('Settings')} style={{marginHorizontal:19,marginTop:10}} >
                    <Image source={require('../assets/settings.png')} style={styles.back}/>
                </TouchableOpacity>
            </View>
            <View style={styles.accountTop}>
                <View style={styles.ellipseStackRow}>
                    <View style={styles.ellipseStack}>
                        <Svg viewBox="0 0 90.27 90.39" style={styles.profileImage}>
                        <Image
        style={styles.userImage}
        source={{
          uri:
            'data:image/png;base64,'+profilePic,
        }}
      />

      
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
        <Text style={styles.fullnameBlack}>{name}</Text>
    <Text style={styles.currentJob}> {job_title}</Text>
    <Text style={styles.currentJob}> {currentCompany}</Text>
    
    <Text style={styles.location}>{education} </Text>
                        <PencilBlack onPress={() => switchEditPhoto()}/>
                    </View>    
                </View>
            </View>
            <View style= {styles.rowContainer}>
                <ConnectButton props={props.ConnectButton}/> 
                <MsgMe props={props.MsgMe}>MESSAGE ME</MsgMe>
               
            </View>
            
            <View>
            <PencilBlack onPress={() => switchEditStory()}/>
            <Text style={styles.myStoryHead}>My Story</Text>
    <Text style={{marginHorizontal:20}}>{story}</Text>
            <Text style={styles.more} onPress={() => onPressMore()}>{see}</Text>
            </View>
            
            <Text style={styles.myStoryHead}>I am passionate about</Text>
            <FlatList data ={passions}  renderItem={
  ({item})=> {
     
     return (<TouchableOpacity key={item} style ={styles.passionTags}><Text style={{color:'white'}}>{item}</Text></TouchableOpacity>);
       
  }}
 keyExtractor={item => item}
 horizontal={true}
 />


            <PencilBlack onPress={() => switchEditPassions()}/>
        
             
            <Text style={styles.myStoryHead}>I can help with</Text>
            <PencilBlack onPress={() => switchEditHelpOthers()}/>
            <FlatList data ={helpothers} renderItem={
  ({item})=> {
     
     return (<TouchableOpacity key={item} style ={styles.helpTags}><Text style={{color:'black'}}>{item}</Text></TouchableOpacity>);
       
  }}
 keyExtractor={item => item}
 horizontal={true}
 />
            
            <View style ={{marginHorizontal:20}}>
                <View style={styles.rowContainer}>
                <Text style={{fontSize:14,fontFamily:'Poppins-Bold'}}>Experience</Text>
                <PencilBlack onPress={() => switchEditExperience()}/>
                
                </View>
                <View style={{flexDirection:'row'}}><Text style={{color:Color.pintroYellow}}>{'\u2B24'}</Text><Text style={{marginVertical:4}}> Academic Level: {academic_Level}</Text></View>

                <View style={{flexDirection:'row'}}><Text style={{color:Color.pintroYellow}}>{'\u2B24'}</Text><Text style={{marginVertical:4}}> Years in industry: {years_in_industry} </Text></View>
                <View style={{flexDirection:'row'}}><Text style={{color:Color.pintroYellow}}>{'\u2B24'}</Text><Text style={{marginVertical:4}}> Previous Company: {previous_Company}</Text></View>


            </View>

            <View>
                <Text style={styles.reportUser}>If you wish to report this user, please contact pintro.admn@outlook.com</Text>
            </View>

        </ScrollView>
    );
};
 
const styles = StyleSheet.create({
    reportUser:{
        fontSize: 9,
        color: Colors.pintroBlack,
        paddingLeft: 20,
        paddingTop: 20
    },
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
        alignItems:'flex-end',
        justifyContent:'flex-end'
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
    },
    userImage: {
        height: 100, 
        width: 100, 
        borderRadius: 100
    },
    passionTags:{
        backgroundColor:'black',
       borderWidth: 1,
       padding:10,
       borderRadius:20,
       margin:10,
       },
       helpTags:{
    backgroundColor:Colors.pintroWhite,
       borderWidth: 1,
       padding:10,
       borderRadius:20,
       margin:10,
       }
});

export default UserAccountScreen;