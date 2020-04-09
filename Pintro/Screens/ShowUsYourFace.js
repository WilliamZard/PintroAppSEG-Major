import React,{useState} from 'react';
import { StyleSheet,Image,Alert, Text, View, Button, TextInput,TouchableOpacity } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import SignInUpButton from '../Components/SignInUpButton';
import InvertedSignInUpButton from '../Components/InvertedSignInUpButton';
import * as Animatable from 'react-native-animatable';
import GoBack from '../Components/GoBack';
import * as ImagePicker from 'expo-image-picker';
import * as ImageManipulator from "expo-image-manipulator";


/**
 * Sign Up Screen to allow the user to sign up. The Screen consists of 5 required input fields,
 * 2 buttons, and the Logo. Furthermore the input fields move up if the keyboard hides them.
 * 
 * @param {} props 
 */

const ShowUsYourFace = props => {

    const phoneNumber = props.navigation.getParam('phoneToPass');
    const email = props.navigation.getParam('emailToPass');
    const[imageUri,setImage] = useState("null");
    const [imageEncoding,setImageEncoding] = useState("");



//Camera functions

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

    props.navigation.navigate({routeName:'WhatsYourStory',params:{
        phoneToPass:phoneNumber,
        emailToPass:email,
        photoToPass:formattedImage
      }})
    }else{
        return
    }
}


    return (

            <View style={styles.backGround}>
                <View style={styles.main}>

                <View style={styles.camera}>
                    <TouchableOpacity style={styles.pictureButton} onPress={() => pickImage()}>
                        <Image source={(imageUri===null)? require('../assets/blankImage.png') : {uri: imageUri}} style={styles.userImage}/>
                        <Text style={styles.add}>+</Text>
                    </TouchableOpacity>

                    <Image source={{uri:
      `data:image/png;base64,${imageEncoding}`,
  }} style={styles.userImage}/>
                </View>
                   
                     
                </View>
                <View style={styles.bottomButton}>
                <InvertedSignInUpButton onPress={
 /* () =>
  props.navigation.navigate({routeName:'WhatsYourStory',params:{
    phoneToPass:phoneNumber,
    emailToPass:email,
  }})*/

  ()=>onPressDone()


                            }>STEP 2 OF 6</InvertedSignInUpButton>
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
    marginBottom:60
    },camera:{
flex:1,
marginTop:70,
marginBottom:100
    },
    pictureButton: {
        borderWidth: 5,
        borderColor: 'grey',
        alignItems: 'center',
        justifyContent: 'center',
        width: 250,
        height: 250,
        backgroundColor: 'white',
        alignSelf: 'center',
        borderRadius: 10,
    },    add: {
        color:'white',
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
    }
});

export default ShowUsYourFace;