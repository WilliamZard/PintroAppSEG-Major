import React, { useState } from 'react';
import { useSelector,useDispatch } from 'react-redux';
import { Dimensions, StyleSheet, View, Text, Image, ScrollView, TouchableOpacity, Alert } from 'react-native';
import FollowMe from '../Components/FollowMe.js';
import MsgMe from '../Components/MsgMe.js';
import BlackTag from '../Components/BlackTag.js';
import HelpMeWith from '../Components/HelpMeWith.js';
import Edit from '../Components/Edit.js';
import { fonts } from '../Constants/Fonts.js';
import Colors from '../Constants/Colors.js';
import JourneyPoint from '../Components/JourneyPoint.js';
import TimelinePostComponent from '../Components/TimelinePostComponent.js';
import * as RequestActions from '../store/actions/request.js';

const ViewBusinessAccountScreen = props => {
    const dispatch = useDispatch();
    const businessObj = useSelector(state => state.business.businessObj);
    const [lines,setLineNumber] = useState(4);
    const [see,setSee] = useState("More");
    const [more,setMore] = useState(true);
    const currentUser = useSelector(state => state.user.email);
    //console.log(businessObj.email);

    function onPressMore() {
        if(more) {
            setLineNumber(10);
            setSee("See less");
            setMore(false);
        } else {
            setLineNumber(4);
            setSee("More");
            setMore(true);
        }   
    }

    let investText;
    let hiringText;

    if(businessObj.seeking_investment==="True") {
        investText = <Text style={fonts.title_yellow}>SEEKING INVESTMENT</Text>;
    } else {
        investText = null;
    }

    if(businessObj.currently_hiring==="True") {
        hiringText = <Text style={fonts.title_black}>CURRENTLY HIRING</Text>;
    } else {
        hiringText = null;
    }

    function onPressBack() {
        props.navigation.navigate('Results')
    }

    return(
        <ScrollView style={{backgroundColor: '#cacaca'}}>
            <View style={styles.imageContainer}>
                <View style={styles.rowContainer}>
                    <TouchableOpacity style={{flex: 1}} onPress={() => onPressBack()}>
                        <Image source={require('../assets/backWhite.png')} style={styles.back}/>
                    </TouchableOpacity>
                    <TouchableOpacity>
                        <Image source={require('../assets/shareWhite.png')} style={styles.shareImage}/>
                    </TouchableOpacity> 
                </View>
                <Image source={require('../assets/blankImage.png')} style={styles.coverPhoto}/>
            </View>
            <View style={styles.whiteContainer}>
                <View style={styles.topRow}>
                    <Text style={styles.slogan}>{businessObj.short_bio}</Text>    
                </View>
                <Text style={styles.businessName}>{businessObj.full_name}</Text>
                <View style={styles.rowContainer}>
                    <FollowMe 
                        props={props.FollowMe} 
                        initial={false}  
                        choice1={"+ FOLLOW US"}
                        choice2={"REQUESTED"}
                        name={businessObj.full_name}/>
                    <MsgMe props={props.MsgMe}>MESSAGE US</MsgMe>
                    <Edit props={props.Edit}>. . .</Edit>
                </View>
                <View style={styles.rowContainer}>
                    <TouchableOpacity style={styles.thumbsButton}>      
                        {investText}
                    </TouchableOpacity>
                    <TouchableOpacity style={styles.thumbsButton}>
                        {hiringText}
                    </TouchableOpacity>
                </View>
                <Text style={styles.title}>Our Story</Text>
                <Text style={styles.storyContent} numberOfLines={lines}>
                    {businessObj.story}
                </Text>
                <Text style={styles.more} onPress={() => onPressMore()}>{see}</Text>
                <ScrollView style={styles.tagContainer} horizontal={true}>
                    <BlackTag props={props.BlackTag}>{(businessObj.tags[0]!==undefined)? businessObj.tags[0].toUpperCase() : null}</BlackTag>
                    <BlackTag props={props.BlackTag}>{(businessObj.tags[1]!==undefined)? businessObj.tags[1].toUpperCase() : null}</BlackTag>
                    <BlackTag props={props.BlackTag}>{(businessObj.tags[2]!==undefined)? businessObj.tags[2].toUpperCase() : null}</BlackTag>
                </ScrollView>
                <ScrollView style={styles.tagContainer} horizontal={true}>
                    <BlackTag props={props.BlackTag}>{(businessObj.tags[3]!==undefined)? businessObj.tags[3].toUpperCase() : null}</BlackTag>
                    <BlackTag props={props.BlackTag}>{(businessObj.tags[4]!==undefined)? businessObj.tags[4].toUpperCase() : null}</BlackTag>
                    <BlackTag props={props.BlackTag}>{(businessObj.tags[5]!==undefined)? businessObj.tags[5].toUpperCase() : null}</BlackTag>
                </ScrollView>
                <ScrollView style={styles.helpContainer} horizontal={true}>
                    <HelpMeWith props={props.HelpMeWith}>Business Modelling</HelpMeWith>
                    <HelpMeWith props={props.HelpMeWith}>Crepe Investments</HelpMeWith>
                    <HelpMeWith props={props.HelpMeWith}>Home Workouts</HelpMeWith>
                </ScrollView>
                <View>
                    <View style={styles.rowContainer}>
                        <Text style={styles.journey}>Our journey</Text>
                    </View>
                    <JourneyPoint default={"Founded:"} userData={businessObj.date_founded}/>
                    <JourneyPoint default={"Location:"} userData={businessObj.location}/>
                    <JourneyPoint default={"Company Size:"} userData={businessObj.company_size}/>
                    <JourneyPoint default={"Funding:"} userData={businessObj.funding}/>
                </View>
                <View>
                    <View style={styles.rowContainer}>
                        <Text style={styles.title}>Team</Text>                   
                    </View>
                    <View style={styles.pillowContainer}>
                        <Image source={require('../assets/blankImage.png')} style={styles.pillows}/>
                        <Image source={require('../assets/blankImage.png')} style={styles.pillows}/>
                        <Image source={require('../assets/blankImage.png')} style={styles.pillows}/>
                        <Image source={require('../assets/blankImage.png')} style={styles.pillows}/>
                    </View>
                </View>
                <View>
                    <View style={styles.rowContainer}>
                        <Text style={styles.title}>Posts</Text>
                        <Text style={styles.seeAll}>See all</Text>
                    </View>
                    <View style={styles.postContainer}>
                        <TimelinePostComponent 
                            uuid={"id1"}
                            content={"Looking forward to our next \n UX design conference, it's \n going to be awesome!"}
                            modified={""}
                            email={""}
                            name={"Piin App Limited"}
                        />
                        <TimelinePostComponent 
                            uuid={"id2"}
                            content={"Piin App is undergoing some \n maintenance at the moment, \n it will be back soon online soon!"}
                            modified={""}
                            email={""}
                            name={"Piin App Limited"}
                        />
                    </View>
                </View>
                <View>
                    <View style={styles.rowContainer}>
                        <Text style={styles.title}>Followers</Text>
                        <Text style={styles.seeAll}>See all(45)</Text>
                    </View>
                    <View style={styles.circleContainer}>
                        <Image source={require('../assets/blankImage.png')} style={styles.circle}/>
                        <Image source={require('../assets/blankImage.png')} style={styles.circle}/>
                        <Image source={require('../assets/blankImage.png')} style={styles.circle}/>
                        <Image source={require('../assets/blankImage.png')} style={styles.circle}/>
                        <Image source={require('../assets/blankImage.png')} style={styles.circle}/>
                        <Image source={require('../assets/blankImage.png')} style={styles.circle}/>
                        <Image source={require('../assets/blankImage.png')} style={styles.circle}/>
                    </View>
                    
                </View>
            </View>
        </ScrollView>
    );
}

const styles = StyleSheet.create({
    whiteContainer: {
        flex: 1,
        backgroundColor: Colors.pintroWhite,
        borderTopLeftRadius: 15,
        borderTopRightRadius: 15,
        paddingTop: 10
    },
    rowContainer: {
        flexDirection: 'row',
    },
    thumbsButton: {
        flexDirection: 'row',
        marginHorizontal: 5,
        marginLeft: 25,
        marginVertical: 20
    },
    imageContainer: {
        marginBottom: 0,
        marginTop: 30,
    },
    shareImage: {
        height: 20, 
        width: 20, 
        alignSelf: 'flex-end', 
        marginRight: 10
    },
    coverPhoto: {
        height: 200, 
        width: Dimensions.get('window').width, 
        resizeMode: 'cover'
    },
    slogan: {
        marginLeft: 30,
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        marginTop: 10,
        flex: 1
    },
    businessName: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        fontSize: 32,
        marginLeft: 30,
    },
    storyContent: {
        marginLeft: 30,
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize:12,
        marginRight: 20,
    },
    more: {
        marginLeft: 30,
        color: Colors.pintroYellow,
        fontFamily: 'Poppins-Bold',
        fontSize:12
    },
    tagContainer: {
        flexDirection: 'row',
        marginTop: 10,
        marginHorizontal: 10
    },
    helpContainer: {
        flexDirection: 'row',
        paddingLeft: 30,
        marginRight: 20,
    },
    journey: {
        marginLeft: 30,
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        fontSize: 14,
        marginBottom: 10,
        marginTop: 10,
        flex: 1
    },
    pillows: {
        height: 80, 
        width: 80, 
        marginRight: 10, 
        borderRadius: 15
    },
    pillowContainer: {
        marginLeft: 30,
        flexDirection: 'row',
        marginBottom: 20,
    },
    title:  {
        marginLeft: 30,
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        fontSize: 14,
        flex: 1
    },
    circle: {
        height: 40, 
        width: 40, 
        marginRight: 10,
        borderRadius: 20
    },
    circleContainer: {
        marginBottom: 20,
        flexDirection: 'row',
        marginLeft: 30
    },
    seeAll: {
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        alignSelf: 'flex-end',
        marginRight: 20
    },
    topRow: {
        flexDirection: 'row',
        marginTop: 30
    },
    postContainer: {
        flexDirection: 'row',
        marginVertical: 10
    },
    back: {
        height: 20, 
        width: 20, 
        marginLeft: 10,
    }
});

export default ViewBusinessAccountScreen;