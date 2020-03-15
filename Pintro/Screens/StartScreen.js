import React, { useEffect, useRef } from 'react';
import { StyleSheet, Animated, Text, View, Button,TouchableHighlight } from 'react-native';
import * as Animatable from 'react-native-animatable';
import SignInUpButton from '../Components/SignInUpButton';
import InvertedSignInUpButton from '../Components/InvertedSignInUpButton';
import Colors from '../Constants/Colors';
import * as tagsActions from '../store/actions/tags';
import {useSelector, useDispatch} from 'react-redux';
/**
 * Start Screen which allows the user to decide whether he wants to sign in
 * or sign up. The screen consists of two custom buttons and the logo.
 * @param {} props 
 */
const StartScreen = props => {
const dispatch = useDispatch();

useEffect(()=> {
    dispatch(tagsActions.getTags("Tag"));
},[dispatch]);
   

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
                        <View style = {styles.additionalText}>
                        <Text style={styles.helloThereText}>Hello there!</Text>
                        </View>
                       
                    <InvertedSignInUpButton >Sign up with LinkedIn</InvertedSignInUpButton>
                    <SignInUpButton onPress={
                        () =>
                        props.navigation.navigate({routeName:'LetsGetStarted'})

                    }>Sign up with email or phone</SignInUpButton>
                    <SignInUpButton onPress={
                        () =>
                     props.navigation.navigate({routeName:'routeTwo'})

                    }>Dummy Login</SignInUpButton>
                    <View style = {styles.additionalText}>
                        <View style={styles.footerText}>
                        <Text style={styles.LoginText}>Already have an account? </Text>

                     
                        <TouchableHighlight onPress={
                                 () =>
                                 props.navigation.navigate({routeName:'SignIn'}) 
                        }><Text style={{ fontSize:18, color:Colors.pintroYellow}}>Login</Text></TouchableHighlight>
                        </View>
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
        //backgroundColor:'blue'
    }, pintroText: {
        color: 'white',
        fontFamily: 'Poppins-Bold',
        fontSize: 50
    },
    yellowAccent: {
        color: Colors.pintroYellow,
        fontSize: 50
    },
    buttonContainer: {
        //backgroundColor:'green',
        paddingTop: 150,
        width: '80%',
        fontFamily:'Poppins-Regular'
    },
    textContainer: {
        flexDirection: 'row',
        //backgroundColor:'blue',
        marginTop:0
    },additionalText:{
        alignItems:'center',
        justifyContent:'center',
        padding:20,
        //backgroundColor:'green'
    },
    helloThereText:{
        color:'white',
        fontSize:30,
        fontFamily:'Poppins-Regular'
    },LoginText:{
        color:'white',
        fontFamily:'Poppins-Regular',
        fontSize:15
    },
    footerText:{
        flexDirection:'row'
    },LogInColored:{
        color:Colors.pintroYellow,
        fontFamily:'Poppins-Regular',
        fontSize:15,
        textDecorationLine:'underline'
    },
      lineStyle:{
        borderWidth: 0.5,
        borderColor:'white',
        margin:10,
   }

});

export default StartScreen;
