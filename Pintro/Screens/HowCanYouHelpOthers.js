import React, {useState} from 'react';
import { StyleSheet, Text, View, Button, FlatList,TextInput,ScrollView,TouchableOpacity, ColorPropType } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import SignInUpButton from '../Components/SignInUpButton';
import InvertedSignInUpButton from '../Components/InvertedSignInUpButton';
import * as Animatable from 'react-native-animatable';
import GoBack from '../Components/GoBack';
import RNPickerSelect from 'react-native-picker-select';
import Color from '../Constants/Colors';
/**
 * Sign Up Screen to allow the user to sign up. The Screen consists of 5 required input fields,
 * 2 buttons, and the Logo. Furthermore the input fields move up if the keyboard hides them.
 * 
 * @param {} props 
 */




const WhatAreYourPassions = props => {

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

                        <Text style={styles.signInText}>How can you help others?</Text>
                        <View style={styles.BottomMargin}>
                        <Text style={styles.aboveInputText}>Choose your superpowers(6 minimum)</Text>
                        </View>
         
                        <Text style={styles.aboveInputText}>Choose from the full list</Text>
                        <Text style={{color:'white'}}>Start Typing</Text>
                        <View style={styles.horizintalLineStyle}></View>
                        </Animatable.View>
                        </View>
 <View style={styles.horizintalLineStyle}></View>
 <Text style={styles.aboveInputText}>or choose from the most popular</Text>
 <ScrollView horizontal={true}>
    <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Feminism</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.choosenButton} ><Text style={{color:Color.pintroYellow}}>Coaching</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Mindfulness</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>
 <ScrollView horizontal={true}>
 <TouchableOpacity style ={styles.choosenButton}><Text style={{color:Color.pintroYellow}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Personal Growth</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>EdTech</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Inclusivity</Text></TouchableOpacity>

   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>
 <ScrollView horizontal={true}>
 <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Wireframing</Text></TouchableOpacity>
 <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Social Media</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.choosenButton} ><Text style={{color:Color.pintroYellow}}>SEO</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>
 <ScrollView horizontal={true}>
 <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.choosenButton}><Text style={{color:Color.pintroYellow}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>
                            <InvertedSignInUpButton style={{width:'80%'}} 
                         onPress={()=>   props.navigation.navigate({routeName:'Passions'}) }>Finish</InvertedSignInUpButton>
                            
                       
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
        paddingTop: 20,
        //justifyContent:'center',
        flexDirection: 'column',
        //backgroundColor:'blue'
    },tagButton:{
    borderColor:'white',
      borderWidth: 1,
    padding:10,
    borderRadius:20,
    margin:10,
    color:'white'
    },choosenButton:{
        borderColor:Color.pintroYellow,
          borderWidth: 1,
        padding:10,
        borderRadius:20,
        margin:10,
        color:Color.pintroYellow
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
        fontWeight: 'normal',
        color:'white'

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

    },list:{
        flexGrow:1,
  justifyContent:'flex-end',
    //  alignItems:'center'  
    },listItem:{
        borderColor:'#ccc',
        borderWidth: 1,
        padding:15,
        marginVertical:10,
        backgroundColor:'white',
        flexDirection:'row',
        justifyContent:'space-between',
        width:'100%'
    }
});

export default WhatAreYourPassions;