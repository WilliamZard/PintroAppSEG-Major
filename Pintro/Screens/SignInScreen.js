import React, {useReducer, useCallback,useState,useEffect } from 'react';
import { StyleSheet, Text, View, Button, TextInput,ActivityIndicator,Alert } from 'react-native';
import SignInUpButton from '../Components/SignInUpButton';
import * as Animatable from 'react-native-animatable';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import Colors from '../Constants/Colors';
import * as tagsActions from '../store/actions/tags';
import InvertedSignInUpButton from '../Components/InvertedSignInUpButton';

import { useDispatch } from 'react-redux';
import * as authActions from '../store/actions/auth';
import * as userActions from '../store/actions/user';
/**
 * 
 * The Sign in screen consisting of the Logo, a header (Text),
 * 2 input fields and 2 buttons. One button takes you to the Main screen after Logging
 * in sucessfully and the other one takes you back to the start screen.
 * @param {*} props 
 */


const SignInScreen = props => {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState();
    const [isSignup, setIsSignup] = useState(false);
    const dispatch = useDispatch();
    
    useEffect(() => {
      if (error) {
        Alert.alert('An Error Occurred!', error, [{ text: 'Okay' }]);
      }
    }, [error]);
  
    
    const signupHandler = async () => {

    setError(null);
    setIsLoading(true);
    try {
    await dispatch(authActions.login(email,password));
      console.log("Worked");
     await dispatch(userActions.get_User_To_Load());
     console.log("Worked2");
     await dispatch(tagsActions.getTags());
     console.log("GO");
     props.navigation.navigate({routeName:'routeTwo'});
    } catch (err) {
      setError(err.message);
      setIsLoading(false);
    }
    
    };  


    const PasswordResetHandler = async () =>{
        if(email===""){
            Alert.alert("Reset Password","Enter your email in the Email address field and press again");
        return;
        }
      Alert.alert("Reset Password","We sent a reset link to the email in the Email address field");
        dispatch(userActions.resetPassword(email));
        return;
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

                        <Text style={styles.signInText}>Welcome back!</Text>
                        <View style={styles.BottomMargin}>
                        <Text style={styles.aboveInputText}>Login to your account</Text>
                        </View>
                            <Text style={styles.aboveInputText}>Email address</Text>
                            <TextInput onChangeText={setEmail} style={styles.inputBox}  placeholder="Enter your email" placeholderTextColor='white' />
 <View style={styles.horizintalLineStyle}></View>
                          
 
                            <Text style={styles.aboveInputText}>Password</Text>
                            <TextInput onChangeText={setPassword} style={styles.inputBox} placeholder="Enter your password" placeholderTextColor='white' secureTextEntry={true} />
                            <View style={styles.horizintalLineStyle}></View>
                           

                            {isLoading?  ( <ActivityIndicator size="small" color={'white'} />
                            ):(
                                <InvertedSignInUpButton onPress={()=>{
                                  signupHandler()
                                 } 
                                }>Login</InvertedSignInUpButton>
                             )}
                            
                            <SignInUpButton onPress={()=>PasswordResetHandler()}>Forgot password</SignInUpButton>
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

export default SignInScreen;
