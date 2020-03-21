import React,{useState} from 'react';
import {
    View,
    StyleSheet,
    Text,
    TextInput
} from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import { CheckBox } from 'react-native-elements'
import { TouchableOpacity } from 'react-native-gesture-handler';
import SignInUpButton from '../../Components/SignInUpButton';

const WhatsYourBrand = props => {
return ( 
    
    
<View style={styles.screen}>
    <View style = {styles.header}>
    <View style = {styles.headerBigText}>
    <Text style={styles.headerText}>What's your brand</Text>
    </View>
    <View style = {styles.headerSmallText}>
    <Text style={styles.smallHeader}>Upload a team photo or logo</Text>
    </View>
    </View>
    <View style={styles.main}>
    <View style={{alignItems:'center',justifyContent:'center'}}>
    
    <TouchableOpacity style={{
       borderWidth:1,
       borderColor:'white',
       alignItems:'center',
       justifyContent:'center',
       width:280,
       height:280,
       backgroundColor:'black',
       borderRadius:190,
     }}><Text style={{color:'white',fontSize:60,fontFamily:'Poppins-Thin'}}>+</Text></TouchableOpacity>

</View>
    <TouchableOpacity style={styles.Button} onPress={
  () =>
  props.navigation.navigate({routeName:'BTeam'})
  

                            }><Text style={styles.TextButton}>Step 4 of 5</Text></TouchableOpacity>
    </View>
</View>


);
};

const styles= StyleSheet.create({
    screen:{
        flex:1,
        backgroundColor:'white'
    },header:{
        marginTop:0,
        alignItems:'flex-start',
       
    },headerText:{
        fontSize:35
    },headerBigText:{
        marginHorizontal:30,
        marginBottom:20
    },smallHeader:{
        fontSize:14
    },headerSmallText:{
        marginHorizontal:30
    },
    horizintalLineStyle:{
        borderBottomColor: 'black',
         borderBottomWidth: StyleSheet.hairlineWidth,
         marginBottom:30,
         marginTop:10
    },main:{

        marginTop:50
    },inputBox:{
marginTop:20
    },inputBoxFullStory: {
        height: 110,
        alignItems:'flex-start',
        justifyContent:'flex-start',
        textAlign:'left',
        fontFamily: 'Poppins-Light',
        fontWeight: 'normal',
        color:'black',
        textAlignVertical:'top'

    },checkBoxes:{
        flexDirection:'row',
      marginVertical:30
    },Button:{
        backgroundColor:'black',
        height:40,
        borderRadius:27,
        alignItems:'center',
        justifyContent:'center',
        marginTop:160,
        marginBottom:300,
        marginHorizontal:30
    },TextButton:{
        color:'white'
    }


});

export default WhatsYourBrand;