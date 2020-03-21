import React , {useState} from 'react';
import { StyleSheet, Text, View, Button, TextInput,TouchableOpacity } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import SignInUpButton from '../Components/SignInUpButton';
import InvertedSignInUpButton from '../Components/InvertedSignInUpButton';
import * as Animatable from 'react-native-animatable';
import GoBack from '../Components/GoBack';
import Modal from 'react-native-modal';
import LetsGetIntoIt from '../Screens/BusinessScreens/LetsGetIntoIt';
/**
 * Sign Up Screen to allow the user to sign up. The Screen consists of 5 required input fields,
 * 2 buttons, and the Logo. Furthermore the input fields move up if the keyboard hides them.
 * 
 * @param {} props 
 */


const FinalSignUp = props => {
    const [visibility,setVisible] = useState(false);
    return (
            <View style={styles.backGround}>
                <View style={styles.main}>

                    <View style={styles.inputController}>
                     
                        <Text style={styles.signInText}>Thank you</Text>
                        <View style={styles.BottomMargin}>
                        <Text style={styles.aboveInputText}>You're now ready to use Pintro</Text>
                        </View>
                     
                    </View>
                   
                </View>
                <View style={styles.bottomButton}>
                <InvertedSignInUpButton onPress={
  () =>
  props.navigation.navigate({routeName:'WhatsYourStory'})


                            }>GO TO YOUR PROFIL</InvertedSignInUpButton>
                                            <SignInUpButton onPress={
  () =>
  props.navigation.navigate({routeName:'WhatsYourStory'})


                            }>GO TO YOUR PROFIL</SignInUpButton>
 <TouchableOpacity
 style={{marginTop:100,height:'100%',width:'100%',backgroundColor:'white' ,borderRadius:20}}
 onPress={()=>props.navigation.navigate({routeName:'LetsStartBusimess'})}><Text style={{fontSize:30,textAlign:'center',marginTop:30}}>Do you have a business?</Text><Text style={{fontSize:10,textAlign:'center',marginTop:30}}>Swipe up to build a business profile</Text></TouchableOpacity>
            </View> 
           <View>
        
        </View>
            </View>
       
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
        justifyContent: 'center',
        alignItems: 'center',

 
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
        marginBottom:60,

    },
    bottomButton:{
        marginTop:200
    //    backgroundColor:'yellow'
    },camera:{
flex:1,
marginTop:70,
marginBottom:100
    },
    
});

export default FinalSignUp;