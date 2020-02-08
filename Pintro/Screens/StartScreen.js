import React, { useEffect, useRef } from 'react';
import { StyleSheet, Animated, Text, View, Button } from 'react-native';
import * as Animatable from 'react-native-animatable';
import SignInUpButton from '../Components/SignInUpButton';
import Colors from '../Constants/Colors';

/**
 * Start Screen which allows the user to decide whether he wants to sign in
 * or sign up. The screen consists of two custom buttons and the logo.
 * @param {} props 
 */
const StartScreen = props => {
    return (
        <View style={styles.backGround}>
            <View style={styles.main}>
                <Animatable.View animation="fadeInDownBig">
                <View style={styles.textContainer}>
                    <Text style={styles.pintroText}>pintro</Text>
                    <Text style={styles.yellowAccent}>.</Text>
                </View>
                </Animatable.View>
                <View style={styles.buttonContainer}>
                    <Animatable.View animation="fadeInUpBig">
                    <SignInUpButton onPress={props.onLogIn}>Sign In</SignInUpButton>
                    <SignInUpButton onPress={props.onSignUp}>Sign Up</SignInUpButton>
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
        //backgroundColor:'blue'
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
        //backgroundColor:'green',
        paddingTop: 20,
        width: '70%',
        fontFamily:'Poppins-Regular'
    },
    textContainer: {
        flexDirection: 'row'
    }
});

export default StartScreen;
