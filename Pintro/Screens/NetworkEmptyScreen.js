import React, { useEffect, useRef } from 'react';
import { StyleSheet, Animated, Text, View, Button, Image } from 'react-native';
import * as Animatable from 'react-native-animatable';
import SignInUpButton from '../Components/SignInUpButton';
import Colors from '../Constants/Colors';

/**
 * Empty Screen which shows a message when there is no internet connection.
 * The screen consists of a message, a WiFi image and the logo.
 * @param {} props 
 */
const NetworkEmptyScreen = props => {
    return (
        <View style={styles.backGround}>
            <View style={styles.main}>
                <Animatable.View animation="fadeInDownBig">
                <View style={styles.textContainer}>
                    <Text style={styles.pintroText}>pintro</Text>
                    <Text style={styles.yellowAccent}>.</Text>
                </View>
                </Animatable.View>
                <View style={styles.imageContainer}>
                    <Animatable.View animation="fadeInUpBig">
                    <Image style={styles.imageContainer} source={require('../images/wifi2.png')}/>
                    <View style={styles.textContainer}>
                    <Text style={styles.messageText}>{'No Connection. \n Please Check Your Network.'}</Text>
                </View>
                    </Animatable.View>
                    
                </View>
            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    backGround: {
        backgroundColor: Colors.pintroBlack,
        flex: 1
    },
    main: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        flexDirection: 'column',
    }, pintroText: {
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
        flexDirection: 'row',
        alignItems: 'center',
        paddingTop: 100
    },
    messageText : {
        color: 'white',
        fontFamily: 'Poppins-Bold',
        textAlign: 'center',
        paddingBottom: 100,
        fontSize: 30
    },
    imageContainer: {
        flex: 1,
        width: null,
        height: null,
        paddingBottom: 25,
        resizeMode: 'contain'
    }
});

export default NetworkEmptyScreen 
