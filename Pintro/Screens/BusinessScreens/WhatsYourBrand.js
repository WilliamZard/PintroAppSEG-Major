import React,{useState} from 'react';
import {
    View,
    StyleSheet,
    Text,
    TextInput,
    Image,Alert
} from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import { CheckBox } from 'react-native-elements'
import { TouchableOpacity } from 'react-native-gesture-handler';
import SignInUpButton from '../../Components/SignInUpButton';
import * as ImagePicker from 'expo-image-picker';
import * as ImageManipulator from "expo-image-manipulator";



const WhatsYourBrand = props => {

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

 

    const[imageUri,setImage] = useState("null");
    const [imageEncoding,setImageEncoding] = useState("");
    async function pickImage() {
        const permission = await ImagePicker.requestCameraRollPermissionsAsync();
        if(permission !== 'granted'){
            getPermission();
        }
        let result = await ImagePicker.launchImageLibraryAsync({
          mediaTypes: ImagePicker.MediaTypeOptions.All,
          allowsEditing: true,
          aspect: [4, 3],
          quality: 1
        });
    
        
    
        if(!result.cancelled) {
            setImage(result.uri);
            setImageEncoding("chosen");
        }
    }
    
    async function getPermission() {
        const status = await ImagePicker.requestCameraRollPermissionsAsync();
        if(status !== 'granted') {
            Alert.alert('Permission needed','We need permission to access your camera roll');
        }
    }
    const verification = () =>{
        console.log(imageEncoding);
        if(imageEncoding.length ===0){
        
            Alert.alert("Error","Please choose a picture");
            return false;
        }
     return true;
        };
    async function onPressDone() {
        console.log("Done was pressed");
        if(!verification()===false){
        const result = await ImageManipulator.manipulateAsync(imageUri, [], {base64: true});
        const imageCode = await result.base64
        const formattedImage = "b'" + imageCode+"'";
       
        setImageEncoding(formattedImage);
    
        props.navigation.navigate({routeName:'BusinessTeam',params:{
            seekingInvestmentsToPass:seekingInvestments,
            currentlyHiringToPass:currentlyHiring,
            companyNameToPass:companyName,
            tagLineToPass:tagLine,
            companyStoryToPass:companyStory,
            BusinessTagsToPass:businessTags,
            dateFoundedToPass:dateFounded,
            locationToPass:location,
            companySizeToPass:companySize,
            fundingToPass:funding,
            dateFoundedToPass:dateFounded,
            locationToPass:location,
            companySizeToPass:companySize,
            fundingToPass:funding
            }})
        }else{
            return
        }
    }
 

return ( 
    
    
    <View style={styles.backGround}>
<View style = {styles.header}>
    <View style = {styles.headerBigText}>
    <Text style={styles.headerText}>What's your brand</Text>
    </View>
    <View style = {styles.headerSmallText}>
    <Text style={styles.smallHeader}>Upload a team photo or logo</Text>
    </View>
    </View>
    <View style={styles.main}>

    <View style={styles.camera}>
                    <TouchableOpacity style={styles.pictureButton} onPress={() => pickImage()}>
                        <Image source={(imageUri===null)? require('../../assets/placeholderFace.png') : {uri: imageUri}} style={styles.userImage}/>
                        <Text style={styles.add}>+</Text>
                    </TouchableOpacity>

                    <Image source={{uri:
      `data:image/png;base64,${imageEncoding}`,
  }} style={styles.userImage}/>
           
                   
</View>

    </View>
    <View style={{alignItems:'center',justifyContent:'baseline'}}> 
    <TouchableOpacity style={styles.Button} onPress={
  () =>
  props.navigation.navigate({routeName:'BTeam'})}><Text style={styles.TextButton}>Step 4 of 5</Text></TouchableOpacity>
    </View>
</View>


);
};

const styles= StyleSheet.create({
    main: {
        flex: 1,
        alignItems: 'center',
        paddingTop: 10,
        //justifyContent:'center',
        flexDirection: 'column',
        //backgroundColor:'blue'
    },
    backGround: {
        backgroundColor: 'white',
        flex: 1
    },
    camera:{
    flex:1,
    marginTop:70,
    marginBottom:100,
        },
    pictureButton: {
        borderWidth: 5,
        borderColor: 'black',
        alignItems: 'center',
        justifyContent: 'center',
        width: 250,
        height: 250,
        backgroundColor: 'white',
        alignSelf: 'center',
        borderRadius: 10,
    },    add: {
        color:'black',
        fontSize:60,
        fontFamily:'Poppins-Thin',
        position:'absolute'
    },
    userImage: {
        height: 230, 
        width: 230, 
        borderRadius: 5
    },   camera:{
        flex:1,
        marginTop:70,
        marginBottom:0,
    },
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
        height:50,
        width:130,
        borderRadius:27,
        alignItems:'center',
        justifyContent:'center',
        marginTop:0,
        marginBottom:30,
 
    },TextButton:{
        color:'white'
    }


});

export default WhatsYourBrand;