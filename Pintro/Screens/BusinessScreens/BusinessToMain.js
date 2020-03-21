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

const BusinessToMain = props => {
return ( 
    
    
<View style={styles.screen}>
    <Text style={{fontSize:30,fontFamily:'Poppins-Bold'}}>Thank you</Text>
    <Text style={{fontSize:15,fontFamily:'Poppins-Light'}}>You're now ready to use Pintro</Text>
    <TouchableOpacity style={styles.Button} onPress={() =>props.navigation.navigate({routeName:'routeTwo'})}><Text style={styles.TextButton}>Go To Company Profile</Text></TouchableOpacity>
    <TouchableOpacity style={styles.Button2} onPress={() =>props.navigation.navigate({routeName:'routeTwo'})}><Text style={{color:'black'}}>Invite Connections</Text></TouchableOpacity>
    
    </View>


);
};

const styles= StyleSheet.create({
    screen:{
        flex:1,
        backgroundColor:'white',
        alignItems:'center',
        justifyContent:'center'
    
    },Button:{
        backgroundColor:'black',
        height:40,
        borderRadius:27,
        alignItems:'center',
        justifyContent:'center',
        margin:10,
        width:300
    },TextButton:{
        color:'white'
    },Button2:{
        backgroundColor:'white',
        height:40,
        borderWidth:1,
        borderColor:'black',
        borderRadius:27,
        alignItems:'center',
        justifyContent:'center',
        margin:10,
        width:300
    }


});

export default BusinessToMain;