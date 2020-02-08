import React from 'react';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
import SignInUpButton from '../Components/SignInUpButton';
import GoBack from '../Components/GoBack';
import * as Animatable from 'react-native-animatable';
import Colors from '../Constants/Colors';


/**
 * The Sign in screen consisting of the Logo, a header (Text),
 * 2 input fields and 2 buttons. One button takes you to the Main screen after Logging
 * in sucessfully and the other one takes you back to the start screen.
 * @param {*} props 
 */
const SignInScreen = props => {
    return (
        <View style={styles.backGround}>
            <View style={styles.main}>
                <View style={styles.textContainer}>
                    <Text style={styles.pintroText}>pintro</Text>
                    <Text style={styles.yellowAccent}>.</Text>
                </View>
                <View style={styles.headerContainer}>
                    <Text style={styles.signInText}>Sign In :</Text>
                </View>
                <View style={styles.inputController}>
                    <Animatable.View animation="fadeIn">
                        <TextInput style={styles.inputBox} placeholder="Email" />
                        <TextInput style={styles.inputBox} placeholder="Password" secureTextEntry={true} />
                        <SignInUpButton>Sign in</SignInUpButton>
                        <GoBack onPress={props.onPressGoBack} >Back</GoBack>
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
        paddingTop: 90,
        //justifyContent:'center',
        flexDirection: 'column',
        //backgroundColor:'blue'
    },
    inputController: {
        flex: 1,
        paddingTop: 20,
        justifyContent: 'flex-start',
        alignContent: 'center',
        width: '80%',

    },
    pintroText: {
        color: 'white',
        fontFamily: 'Poppins-Bold',
        fontSize: 50,

    },
    yellowAccent: {
        color: Colors.pintroYellow,
        fontSize: 50
    },
    textContainer: {
        flexDirection: 'row'
    },
    inputTexts: {
        color: 'black'
    },
    textBackGround: {
        backgroundColor: 'white',
        height: 19,
        borderRadius: 20
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

    inputBox: {
        height: 40,
        textAlign: 'center',
        backgroundColor: 'white',
        marginBottom: 20,
        borderRadius: 10
    }
});

export default SignInScreen;