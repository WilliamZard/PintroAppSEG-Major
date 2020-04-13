import React, { useEffect, useRef } from 'react';
import { StyleSheet, Animated, Text, View, Button, Image } from 'react-native';
import * as Animatable from 'react-native-animatable';
import SignInUpButton from '../Components/SignInUpButton';
import Colors from '../Constants/Colors';

/**
 * Empty Screen which shows an error message when something has gone wrong.
 * The screen consists of a message, an image and retry button.
 * @param {} props 
 */
const SomethingWrongScreen = props => {
    return (
        <View style={styles.backGround}>
            <View style={styles.main}>

                <Animatable.View animation="fadeInDownBig">
                <View style={styles.textContainer}>
                    <Text style={styles.messageText}>{'Oops! \n'}</Text>
                    <Text style={styles.subText}>{'Something went wrong, please try again.'}</Text>
                </View>
                </Animatable.View>

                <View style={styles.imageContainer}>
                    <Animatable.View animation="fadeInUpBig">
                    <Image style={styles.imageContainer} source={require('../images/somethingWrong.png')}/>
                    </Animatable.View>   
                </View>

                <View style={styles.imageButtonContainer}>
                <Animatable.View animation="fadeInUpBig">
                    <Image style={styles.imageButtonContainer} source={require('../images/retryButton.png')}/>
                    </Animatable.View>
                </View>

                <View> 
                    
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
        //flex: 1,
        flexDirection: 'column',
        alignItems: 'center',
        paddingTop: 10
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
        //paddingBottom: 100,
        fontSize: 12
    },
    imageContainer: {
        //flex: 1,
        width: 350,
        height: 350,
        paddingBottom: 25,
        resizeMode: 'contain'
    },
    imageButtonContainer: {
        //flex: 1,
        width: 350,
        height: 350,
        paddingBottom: 5,
        resizeMode: 'contain'
    }
});

export default SomethingWrongScreen 
