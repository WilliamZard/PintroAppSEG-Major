import React, { useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import SignInScreen from './SignInScreen';
import SignUpScreen from './SignUpScreen';
import StartScreen from './StartScreen';

const LogInOverView = props => {

    /**
     * State to keep track on whether the user is trying to sign in or
     * sign up. This is done with a React hook.
     */
    const [currentLogInState, setCurrentLogInState] = useState("notLoggedIn");

    const userWantsToSignIn = () => {
        setCurrentLogInState("wantsToSignIn");
    }

    const userWantsToSignUp = () => {
        setCurrentLogInState("wantsToSignUp");
    }

    const userWantsToGoBack = () => {
        setCurrentLogInState("notLoggedIn");
    }


    /**
     * The content variable is either the sign up, sign in or the basic start screen.
     * Depending on the state, we switch. This if else block is executed 
     * every time this file is rendered.
     */
    let content = <StartScreen onSignUp={userWantsToSignUp} onLogIn={userWantsToSignIn} />
    if (currentLogInState === "wantsToSignIn") {
        content = <SignInScreen onPressGoBack={userWantsToGoBack} />
    } else if (currentLogInState === "wantsToSignUp") {
        content = <SignUpScreen onPressGoBack={userWantsToGoBack} />
    } else {
        content = <StartScreen onSignUp={userWantsToSignUp} onLogIn={userWantsToSignIn} />
    }

    return (
        <View style={styles.screen}>
            {content}
        </View>
    );
};



const styles = StyleSheet.create({
    screen: {
        flex: 1
    }

});

export default LogInOverView;