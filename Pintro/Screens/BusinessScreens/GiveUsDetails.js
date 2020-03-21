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

const GiveUsDetails = props => {
const [seekingInvestments,setSeekingInvestments] = useState(false);
const [currentlyHiring,setCurrentlyHiring] = useState(false);
return ( 
    <KeyboardAwareScrollView
    style={{ backgroundColor: '#1a1a1a' }}
    resetScrollToCoords={{ x: 0, y: 0 }}
    contentContainerStyle={styles.container}
    scrollEnabled={false}>
<View style={styles.screen}>
    <View style = {styles.header}>
    <View style = {styles.headerBigText}>
    <Text style={styles.headerText}>Give us the details</Text>
    </View>
    <View style = {styles.headerSmallText}>
    <Text style={styles.smallHeader}>Your company journey</Text>
    </View>
    </View>
    <View style={styles.main}>
    <Text>Date Founded</Text>
    <TextInput style={styles.inputBox} placeholder="Enter number of years" placeholderTextColor='grey' secureTextEntry={false} />
    <View style={styles.horizintalLineStyle}></View>
    <Text>Location</Text>
    <TextInput style={styles.inputBox} placeholder="Enter your company location" placeholderTextColor='grey' secureTextEntry={false} />
    <View style={styles.horizintalLineStyle}></View>
    <Text>Company Size</Text>
    <TextInput style={styles.inputBox} placeholder="How big is your team?" placeholderTextColor='grey' secureTextEntry={false} />
    <View style={styles.horizintalLineStyle}></View>
    <Text>Funding</Text>
    <TextInput style={styles.inputBox} placeholder="Have you received funding?" placeholderTextColor='grey' secureTextEntry={false} />
    <View style={styles.horizintalLineStyle}></View>
  
    <TouchableOpacity style={styles.Button} onPress={
  () =>
  props.navigation.navigate({routeName:'BrandLogo'})
  

                            }><Text style={styles.TextButton}>Step 3 of 5</Text></TouchableOpacity>
    </View>
</View>

</KeyboardAwareScrollView>)

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
        marginHorizontal:30,
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
        marginTop:30,
        marginBottom:300
    },TextButton:{
        color:'white'
    }


});

export default GiveUsDetails;