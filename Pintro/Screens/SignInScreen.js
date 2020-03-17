import React, {useReducer, useCallback,useState,useEffect } from 'react';
import { StyleSheet, Text, View, Button, TextInput,ActivityIndicator,Alert } from 'react-native';
import SignInUpButton from '../Components/SignInUpButton';
import * as Animatable from 'react-native-animatable';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import Colors from '../Constants/Colors';
import Input from '../Components/Input';
import InvertedSignInUpButton from '../Components/InvertedSignInUpButton';

import { useDispatch } from 'react-redux';
import * as authActions from '../store/actions/auth';
/**
 * The Sign in screen consisting of the Logo, a header (Text),
 * 2 input fields and 2 buttons. One button takes you to the Main screen after Logging
 * in sucessfully and the other one takes you back to the start screen.
 * @param {*} props 
 */



const FORM_INPUT_UPDATE = 'FORM_INPUT_UPDATE';

const formReducer = (state, action) => {
  if (action.type === FORM_INPUT_UPDATE) {
    const updatedValues = {
      ...state.inputValues,
      [action.input]: action.value
    };
    const updatedValidities = {
      ...state.inputValidities,
      [action.input]: action.isValid
    };
    let updatedFormIsValid = true;
    for (const key in updatedValidities) {
      updatedFormIsValid = updatedFormIsValid && updatedValidities[key];
    }
    return {
      formIsValid: updatedFormIsValid,
      inputValidities: updatedValidities,
      inputValues: updatedValues
    };
  }
  return state;
};

//




const SignInScreen = props => {


    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState();
    const [isSignup, setIsSignup] = useState(false);
    const dispatch = useDispatch();
    
    const [formState, dispatchFormState] = useReducer(formReducer, {
      inputValues: {
        email: '',
        password: ''
      },
      inputValidities: {
        email: false,
        password: false
      },
      formIsValid: false
    });
    useEffect(() => {
    if (error) {
      Alert.alert('An Error Occurred!', error, [{ text: 'Okay' }]);
    }
    }, [error]);
    
    const signupHandler = async () => {
    let action;
       action =  authActions.login(
          formState.inputValues.email,
          formState.inputValues.password
    
      );
    
    setError(null);
    setIsLoading(true);
    try {
      await dispatch(action);
      console.log("Worked");
      props.navigation.navigate({routeName:'MainScreen'});
    } catch (err) {
      setError(err.message);
      setIsLoading(false);
    }
    
    };  
    
    const inputChangeHandler = useCallback(
      (inputIdentifier, inputValue, inputValidity) => {
        dispatchFormState({
          type: FORM_INPUT_UPDATE,
          value: inputValue,
          isValid: inputValidity,
          input: inputIdentifier
        });
      },
      [dispatchFormState]
    );

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
                            <Input
              id="email"
              label=""
              placeholder=""
              keyboardType="email-address"
              required
              email
              autoCapitalize="none"
              errorText="Please enter a valid email address."
              onInputChange={inputChangeHandler}
              initialValue=""
            />
 <View style={styles.horizintalLineStyle}></View>
                          
 
                            <Text style={styles.aboveInputText}>Password</Text>
                            <Input
              id="password"
              label=""
              keyboardType="default"
              secureTextEntry
              required
              minLength={5}
              autoCapitalize="none"
              errorText="Please enter a valid password."
              onInputChange={inputChangeHandler}
              initialValue=""
              style={styles.inputBox}
            />
                            <View style={styles.horizintalLineStyle}></View>
                           

                            {isLoading?  ( <ActivityIndicator size="small" color={'white'} />
                            ):(
                                <InvertedSignInUpButton onPress={()=>{
                                  signupHandler();
                                  props.navigation.navigate({routeName:'routeTwo'})} 
                                }>Login</InvertedSignInUpButton>
                             )}
                            
                            <SignInUpButton>Login with LinkedIn</SignInUpButton>
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