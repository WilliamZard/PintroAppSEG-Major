import React from 'react';
import { StyleSheet, Text, View, Button, TextInput,TouchableOpacity } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import SignInUpButton from '../Components/SignInUpButton';
import InvertedSignInUpButton from '../Components/InvertedSignInUpButton';
import * as Animatable from 'react-native-animatable';
import GoBack from '../Components/GoBack';

/**
 * Sign Up Screen to allow the user to sign up. The Screen consists of 5 required input fields,
 * 2 buttons, and the Logo. Furthermore the input fields move up if the keyboard hides them.
 * 
 * @param {} props 
 */

const ShowUsYourFace = props => {

    const phoneNumber = props.navigation.getParam('phoneToPass');
    const email = props.navigation.getParam('emailToPass');
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

                        <Text style={styles.signInText}>Show us your face</Text>
                        <View style={styles.BottomMargin}>
                        <Text style={styles.aboveInputText}>Upload a profile photo</Text>
                        </View>
                        </Animatable.View>
                    </View>
                    <View style={styles.camera}>
                    <TouchableOpacity style={{
       borderWidth:1,
       borderColor:'white',
       alignItems:'center',
       justifyContent:'center',
       width:280,
       height:280,
       backgroundColor:'grey',
       borderRadius:190,
     }}><Text style={{color:'white',fontSize:60,fontFamily:'Poppins-Thin'}}>+</Text></TouchableOpacity>
                    </View>
                     
                </View>
                <View style={styles.bottomButton}>
                <InvertedSignInUpButton onPress={
  () =>
  props.navigation.navigate({routeName:'WhatsYourStory'},{
    phoneToPass:phoneNumber,
    emailToPass:email,
  })


                            }>STEP 2 OF 6</InvertedSignInUpButton>
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
        paddingTop: 10,
        //justifyContent:'center',
        flexDirection: 'column',
        //backgroundColor:'blue'
    },
    inputController: {
        flex: 1,
        paddingTop: 0,
        justifyContent: 'flex-start',
        alignContent: 'center',
        width: '80%',
//        backgroundColor:'green'

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
        fontWeight: 'normal'

    }, signInText: {
        color: 'white',
        fontFamily: 'Poppins-Bold',
        fontSize: 25
    },
    aboveInputText:{
        color:'grey',
        fontFamily:'Poppins-Regular'
    },
    BottomMargin:{
        marginBottom:60
    },
    bottomButton:{
    //    backgroundColor:'yellow'
    },camera:{
flex:1,
marginTop:70,
marginBottom:100
    }
});

export default ShowUsYourFace;