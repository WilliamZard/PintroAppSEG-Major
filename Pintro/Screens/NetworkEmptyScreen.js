import React, { useEffect, useRef } from 'react';
import { StyleSheet, Animated, Text, View, Button, Image } from 'react-native';
import * as Animatable from 'react-native-animatable';
import SignInUpButton from '../Components/SignInUpButton';
import Colors from '../Constants/Colors';

/**
 * Empty Screen which shows a message when there is no internet connection.
 * The screen consists of a message, a WiFi image and button to internet settings.
 * 
 * @param {} props 
 */
const NetworkEmptyScreen = props => {
    return (
        <View style={styles.backGround}>
            <View style={styles.main}>

                <Animatable.View animation="fadeInDownBig">
                <View style={styles.textContainer}>
                    <Text style={styles.messageText}>{'No internet connection \n'}</Text>
                    <Text style={styles.subText}>{'Please check your connection settings.'}</Text>
                </View>
                </Animatable.View>

                <View style={styles.imageContainer}>
                    <Animatable.View animation="fadeInUpBig">
                    <Image style={styles.imageContainer} source={require('../images/noInternet.png')}/>
                    </Animatable.View>
                    
                </View>
                

                <View style={styles.imageButtonContainer}>
                <Animatable.View animation="fadeInUpBig">
                    <Image style={styles.imageButtonContainer} source={require('../images/intSettingsButton.png')}/>
                    </Animatable.View>
                </View>

            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    backGround: {
        backgroundColor: '#E5E5E5',
        flex: 1
    },
    main: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        flexDirection: 'column',
    }, 
    pintroText: {
        color: 'white',
        fontFamily: 'Poppins-Bold',
        fontSize: 30
    },
    yellowAccent: {
        color: Colors.pintroYellow,
        fontSize: 30
    },
    buttonContainer: {
        paddingTop: 20,
        width: '70%',
        fontFamily:'Poppins-Regular'
    },
    textContainer: {

        flexDirection: 'column',
        alignItems: 'center',
        paddingTop: 30
    },
    messageText : {
        color: 'black',
        fontFamily: 'Poppins-Bold',
        textAlign: 'center',
        paddingTop: 20,
        fontSize: 30
    },
    subText : {
        color: 'black',
        fontFamily: 'Poppins-Regular',
        textAlign: 'center',
        paddingBottom: 20,
        fontSize: 12
    },
    imageContainer: {

        width: 350,
        height: 350,
        paddingBottom: 5,
        resizeMode: 'contain'
    },
    imageButtonContainer: {

        width: 350,
        height: 350,
        paddingBottom: 5,
        resizeMode: 'contain'
    }
});

export default NetworkEmptyScreen 
