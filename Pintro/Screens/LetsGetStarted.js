import React, {useReducer, useCallback,useState,useEffect } from 'react';
import { StyleSheet, Text, View, Button,ActivityIndicator, TextInput,Alert } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import SignInUpButton from '../Components/SignInUpButton';
import InvertedSignInUpButton from '../Components/InvertedSignInUpButton';
import * as Animatable from 'react-native-animatable';
import { useDispatch,useSelector } from 'react-redux';
import * as authActions from '../store/actions/auth';
import Input from '../Components/Input';

/**
 * Sign Up Screen to allow the user to sign up. The Screen consists of 5 required input fields,
 * 2 buttons, and the Logo. Furthermore the input fields move up if the keyboard hides them.
 * 
 * @param {} props 
 */



//SIGN UP STUFF



const LetsGetStarted = props => {

//
 


const [confirmPassword,setConfirmPassword] = useState();
const [userEmail,setUserEmail] = useState();
const [userPassword,setUserPassword]= useState();
const [phoneNumber,setPhoneNumber] = useState();
const [isLoading, setIsLoading] = useState(false);
const [error, setError] = useState();
const [isSignup, setIsSignup] = useState(false);
const dispatch = useDispatch();


const signupHandler = async () => {

setError(null);
setIsLoading(true);
try {
   await dispatch(authActions.signup(userEmail,userPassword));
  console.log(userEmail);

  props.navigation.navigate({routeName:'Camera',params:{
    phoneToPass:phoneNumber,
    emailToPass:userEmail}})

   

} catch (err) {
  setError(err.message);
  setIsLoading(false);
}

};  



    return (
        <KeyboardAwareScrollView
            style={{ backgroundColor: '#1a1a1a' }}
            resetScrollToCoords={{ x: 0, y: 0 }}
            contentContainerStyle={styles.container}
            scrollEnabled={false}>
            <View style={styles.backGround}>
                <View style={styles.main}>
                  
                    <View style={styles.inputController}>
                        <Animatable.View animation="fadeIn">

                        <Text style={styles.signInText}>Let's get started</Text>
                        <View style={styles.BottomMargin}>
                        <Text style={styles.aboveInputText}>Create your account</Text>
                        </View>
                            <Text style={styles.aboveInputText}>Email address</Text>
                            <TextInput onChangeText={setPhoneNumber} style={styles.inputBox} onChangeText={(text)=>setUserEmail(text)} placeholder="Enter your email" placeholderTextColor='white' />
 <View style={styles.horizintalLineStyle}></View>
                            <Text style={styles.aboveInputText}>Phone number</Text>
                            <TextInput onChangeText={setPhoneNumber} style={styles.inputBox} placeholder="Enter your phone number" placeholderTextColor='white' keyboardType='numeric'/>
 <View style={styles.horizintalLineStyle}></View>
                            <Text style={styles.aboveInputText}>Password</Text>
                            <TextInput onChangeText={setPhoneNumber} style={styles.inputBox}onChangeText={(text)=>setUserPassword(text)} placeholder="Enter your password" placeholderTextColor='white' secureTextEntry={true}/>
                            <View style={styles.horizintalLineStyle}></View>
                            <Text style={styles.aboveInputText}>Confirm password</Text>
                            <TextInput  onChangeText={setConfirmPassword} style={styles.inputBox} placeholder="********" placeholderTextColor='white' secureTextEntry={true} />
                            <View style={styles.horizintalLineStyle}></View>

                            {isLoading?  ( <ActivityIndicator size="small" color={'white'} />
                            ):(
                       
                                <InvertedSignInUpButton onPress={signupHandler
                                    //()=>   props.navigation.navigate({routeName:'Camera'}) 
                                }>STEP 1 OF 6</InvertedSignInUpButton>
                             )}
                            
                            
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
        //justifyContent:'center',
        flexDirection: 'column',
        //backgroundColor:'blue'
    },
    inputController: {
        flex: 1,
        paddingTop: 40,
        justifyContent: 'flex-start',
        alignContent: 'center',
        width: '80%'

    },
    textContainer: {
        flexDirection: 'row'
    },
    inputTexts: {
        color: 'black'
    },

    inputBox: {
        height: 40,
        textAlign:'left',
        fontFamily: 'Poppins-Light',
        fontWeight: 'normal',
        color:'white'

    }, signInText: {
        color: 'white',
        fontFamily: 'Poppins-Bold',
        fontSize: 30
    },
    aboveInputText:{
        color:'grey',
        fontFamily:'Poppins-Regular'
    },
    horizintalLineStyle:{
        borderBottomColor: 'white',
         borderBottomWidth: StyleSheet.hairlineWidth,
         marginBottom:10
    },backButton:{
        width:'80%',
        alignContent:'flex-start',
        alignItems:'flex-start',

    },
    BottomMargin:{
        marginBottom:60
    }
});

export default LetsGetStarted;