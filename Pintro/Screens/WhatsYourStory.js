import React from 'react';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
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

const WhatsYourStory = props => {
    const phoneNumber = props.navigation.getParam('phoneToPass');
    const email = props.navigation.getParam('emailToPass');
    

    const [name,setName] = useState();
    const [currentJobTitle,setCurrentJobTitle] = useState();
    const [currentCompany,setCurrentCompany] = useState();
    const [story,setStory] = useState();

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

                        <Text style={styles.signInText}>What's your story</Text>
                        <View style={styles.BottomMargin}>
                        <Text style={styles.aboveInputText}>Build your profile</Text>
                        </View>
                            <Text style={styles.aboveInputText}>Name</Text>
                            <TextInput 
                            style={styles.inputBox} 
                            placeholder="Enter your full name"
                             placeholderTextColor='white'
                             onChangeText={setName}
                             />
 <View style={styles.horizintalLineStyle}></View>
                            <Text style={styles.aboveInputText}>Current job title</Text>
                            <TextInput
                             style={styles.inputBox}
                              placeholder="Enter your job title"
                               placeholderTextColor='white'
                               onChangeText={setCurrentJobTitle}
                               />
 <View style={styles.horizintalLineStyle}></View>
 <Text style={styles.aboveInputText}>Current company</Text>
                            <TextInput
                             style={styles.inputBox} 
                             placeholder="Enter current company name"
                              placeholderTextColor='white'
                              onChangeText={setCurrentCompany}
                              />
 <View style={styles.horizintalLineStyle}></View>
 <Text style={styles.aboveInputText}>Your story</Text>
 <View style={styles.textInputCentered}>
<TextInput 
style={styles.inputBoxFullStory}
  multiline={true} 
  placeholder="Tell is about yourself"
   placeholderTextColor='white'
   onChangeText={setStory}
   />
</View>
 <View style={styles.horizintalLineStyle}></View>
                           
                            <InvertedSignInUpButton onPress={
  () =>
  props.navigation.navigate({routeName:'TellUsHistory'},{
    phoneToPass:phoneNumber,
    emailToPass:email,
    nameToPass:name,
    currentJobTitleToPass:currentJobTitle,
    currentCompanyToPass:currentCompany,
    storyToPass:story
  })

                            }>STEP 3 OF 6</InvertedSignInUpButton>
                            
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
    horizintalLineStyle:{
        borderBottomColor: 'white',
         borderBottomWidth: StyleSheet.hairlineWidth,
         marginBottom:30,
         marginTop:10
    },backButton:{
        width:'80%',
        alignContent:'flex-start',
        alignItems:'flex-start',

    },
    BottomMargin:{
        marginBottom:60
    },

    inputBoxFullStory: {
        height: 110,
        alignItems:'flex-start',
        justifyContent:'flex-start',
        textAlign:'left',
        fontFamily: 'Poppins-Light',
        fontWeight: 'normal',
        color:'white',
        textAlignVertical:'top'

    },textInputCentered:{
        alignItems: 'flex-start',
        textAlignVertical: 'top',

    }
});

export default WhatsYourStory;