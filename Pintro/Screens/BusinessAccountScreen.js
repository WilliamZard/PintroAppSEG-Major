import React from 'react';
import { Dimensions, StyleSheet, View, Text, Image, ScrollView, TouchableOpacity, FlatList } from 'react-native';
import FollowMe from '../Components/FollowMe.js';
import MsgMe from '../Components/MsgMe.js';
import BlackTag from '../Components/BlackTag.js';
import HelpMeWith from '../Components/HelpMeWith.js';
import Edit from '../Components/Edit.js';
import { fonts } from '../Constants/Fonts.js';
import PencilBlack from '../Components/PencilBlack.js';
import PencilWhite from '../Components/PencilWhite.js';
import Colors from '../Constants/Colors.js';
import JourneyPoint from '../Components/JourneyPoint.js';

const BusinessAccountScreen = props => {
    return(
        <ScrollView style={{backgroundColor: '#cacaca'}}>
            <View style={styles.imageContainer}>
                <TouchableOpacity>
                    <Image source={require('../assets/shareWhite.png')} style={styles.shareImage}/>
                </TouchableOpacity>
                <Image source={require('../assets/blankImage.png')} style={styles.coverPhoto}/>
                <PencilWhite />
            </View>
            <View style={styles.whiteContainer}>
                <View style={styles.topRow}>
                    <Text style={styles.slogan}>Connect in Real Life</Text>
                    <PencilBlack style={{marginTop: 10}}/>    
                </View>
                <Text style={styles.businessName}>Piin App Limited</Text>
                <View style={styles.rowContainer}>
                    <FollowMe props={props.FollowMe}>NEW POST</FollowMe>
                    <MsgMe props={props.MsgMe}>EDIT PROFILE</MsgMe>
                    <Edit props={props.Edit}>. . .</Edit>
                </View>
                <View style={styles.rowContainer}>
                    <TouchableOpacity style={styles.thumbsButton}>
                        <Image source={require('../assets/yellowThumbsUp.png')} style={{height: 20, width: 20, marginHorizontal: 5}}/>
                        <Text style={fonts.title_yellow}>SEEKING INVESTMENT</Text>
                    </TouchableOpacity>
                    <TouchableOpacity style={styles.thumbsButton}>
                        <Image source={require('../assets/blackThumbsDown.png')} style={{height: 20, width: 20, marginHorizontal: 5}}/>
                        <Text style={fonts.title_black}>CURRENTLY HIRING</Text>
                    </TouchableOpacity>
                </View>
                <Text style={styles.title}>Our Story</Text>
                <Text style={styles.storyContent}>
                    Lorem ipsum dolor sit amet, consecteteur adipiscing elit...
                </Text>
                <Text style={styles.more}>More</Text>
                <PencilBlack />
                <View style={styles.tagContainer}>
                    <BlackTag props={props.BlackTag}>START-UP</BlackTag>
                    <BlackTag props={props.BlackTag}>PRE-SEED</BlackTag>
                    <BlackTag props={props.BlackTag}>NETWORKING</BlackTag>
                </View>
                <View style={styles.tagContainer}>
                    <BlackTag props={props.BlackTag}>ENTREPRENEUR</BlackTag>
                    <BlackTag props={props.BlackTag}>APP</BlackTag>
                    <BlackTag props={props.BlackTag}>CO-WORKING</BlackTag>
                </View>
                <ScrollView style={styles.helpContainer} horizontal={true}>
                    <HelpMeWith props={props.HelpMeWith}>Business Modelling</HelpMeWith>
                    <HelpMeWith props={props.HelpMeWith}>Crepe Investments</HelpMeWith>
                    <HelpMeWith props={props.HelpMeWith}>Home Workouts</HelpMeWith>
                </ScrollView>
                <View>
                    <View style={styles.rowContainer}>
                        <Text style={styles.journey}>Our journey</Text>
                        <PencilBlack />
                    </View>
                    <JourneyPoint default={"Founded:"} userData={"May 2017"}/>
                    <JourneyPoint default={"Location:"} userData={"Central London"}/>
                    <JourneyPoint default={"Company Size:"} userData={"5 Team Members"}/>
                    <JourneyPoint default={"Funding:"} userData={"Pre-Seed"}/>
                </View>
                <View>
                    <View style={styles.rowContainer}>
                        <Text style={styles.title}>Team</Text>
                        <PencilBlack />                    
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
        marginTop: 50,
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
        fontSize:12
    },
    more: {
        marginLeft: 30,
        color: Colors.pintroYellow,
        fontFamily: 'Poppins-Bold',
        fontSize:12
    },
    tagContainer: {
        flexDirection: 'row',
        marginTop: 10
    },
    helpContainer: {
        flexDirection: 'row',
        marginLeft: 30,
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
        marginBottom: 20
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
    }
});

export default BusinessAccountScreen;