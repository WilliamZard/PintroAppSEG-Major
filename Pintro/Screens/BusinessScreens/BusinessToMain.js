import React,{useState} from 'react';
import {
    View,
    StyleSheet,
    Text,
    TextInput
} from 'react-native';
import { useDispatch,useSelector } from 'react-redux';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import { CheckBox } from 'react-native-elements'
import { TouchableOpacity } from 'react-native-gesture-handler';
import SignInUpButton from '../../Components/SignInUpButton';
import * as BusinessActions from '../../store/actions/business';
const BusinessToMain = props => {
    const dispatch = useDispatch();
    const email = useSelector(state => state.user.email);
    const seekingInvestments = props.navigation.getParam('seekingInvestmentsToPass');
    const currentlyHiring = props.navigation.getParam('currentlyHiringToPass');
    const companyName = props.navigation.getParam('companyNameToPass');
    const tagLine = props.navigation.getParam('tagLineToPass');
    const companyStory = props.navigation.getParam('companyStoryToPass');
    const businessTags = props.navigation.getParam('BusinessTagsToPass');
    const dateFounded = props.navigation.getParam('dateFoundedToPass');
    const location = props.navigation.getParam('locationToPass');
    const companySize = props.navigation.getParam('companySizeToPass');
    const funding = props.navigation.getParam('fundingToPass');
    const photo = props.navigation.getParam('photoToGet');
return ( 
    
    
<View style={styles.screen}>
    <Text style={{fontSize:30,fontFamily:'Poppins-Bold'}}>Thank you</Text>
    <Text style={{fontSize:15,fontFamily:'Poppins-Light'}}>You're now ready to use Pintro</Text>
    <TouchableOpacity style={styles.Button} 
    onPress={() =>{
        console.log(email);
        dispatch(BusinessActions.create_business(photo,location,companyStory,businessTags,dateFounded,companySize,funding,"",seekingInvestments,currentlyHiring))
        props.navigation.navigate({routeName:'routeTwo'})}}><Text style={styles.TextButton}>Go To Company Profile</Text></TouchableOpacity>
    
    
    
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