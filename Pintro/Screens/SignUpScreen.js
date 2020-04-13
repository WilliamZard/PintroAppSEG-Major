import React from 'react';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import SignInUpButton from '../Components/SignInUpButton';
import * as Animatable from 'react-native-animatable';
import GoBack from '../Components/GoBack';

/**
 * Sign Up Screen to allow the user to sign up. The Screen consists of 5 required input fields,
 * 2 buttons, and the Logo. Furthermore the input fields move up if the keyboard hides them.
 * 
 * @param {} props 
 */

const SignUpScreen = props => {
    return (
        <KeyboardAwareScrollView
            style={{ backgroundColor: '#1a1a1a' }}
            resetScrollToCoords={{ x: 0, y: 0 }}
            contentContainerStyle={styles.container}
            scrollEnabled={false}>
            <View style={styles.backGround}>
                <View style={styles.main}>
                    <View style={styles.textContainer}>
                        <Text style={styles.pintroText}>pintro</Text>
                        <Text style={styles.yellowAccent}>.</Text>
                    </View>
                    <View style={styles.headerContainer}>
                        <Text style={styles.signInText}>Sign Up:</Text>
                    </View>
                    <View style={styles.inputController}>
                        <Animatable.View animation="fadeIn">
                            <TextInput style={styles.inputBox} placeholder="First Name" />
                            <TextInput style={styles.inputBox} placeholder="Last Name" />
                            <TextInput style={styles.inputBox} placeholder="Email" />
                            <TextInput style={styles.inputBox} placeholder="Password" secureTextEntry={true} />
                            <TextInput style={styles.inputBox} placeholder="Confirm Password" secureTextEntry={true} />
                            <SignInUpButton>Sign Up</SignInUpButton>
                            <GoBack onPress={props.onPressGoBack} >Back</GoBack>
                        </Animatable.View>
                    </View>
                </View>
            </View>

        </KeyboardAwareScrollView>
    );
};


const styles = StyleSheet.create({
    backGround: {
        backgroundColor: '#1a1a1a',
        flex: 1
    },
    main: {
        flex: 1,
        alignItems: 'center',
        paddingTop: 60,
        flexDirection: 'column',

    },
    inputController: {
        flex: 1,
        paddingTop: 40,
        justifyContent: 'flex-start',
        alignContent: 'center',
        width: '80%'

    },
    pintroText: {
        color: 'white',
        fontFamily: 'Poppins-Bold',
        fontSize: 50,


    },
    yellowAccent: {
        color: '#f6ab48',
        fontSize: 50
    },
    textContainer: {
        flexDirection: 'row'
    },
    inputTexts: {
        color: 'black'
    },

    inputBox: {
        height: 40,
        textAlign: 'center',
        backgroundColor: 'white',
        marginBottom: 20,
        borderRadius: 10,
        fontFamily: 'Poppins-Light',
        fontWeight: 'normal'

    }, signInText: {
        color: 'white',
        fontFamily: 'Poppins-Regular',
        fontSize: 30
    },
    headerContainer: {
        marginTop: 80,
        width: '100%',
        alignItems: 'center',

    },
});

export default SignUpScreen;