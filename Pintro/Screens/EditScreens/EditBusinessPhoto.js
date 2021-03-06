import React, { useState } from 'react';
import { View,TouchableOpacity,Text,Image,StyleSheet,Alert } from 'react-native';
import BlackTag from '../../Components/BlackTag';
import Colors from '../../Constants/Colors';
import * as ImagePicker from 'expo-image-picker';
import * as ImageManipulator from "expo-image-manipulator";
import { BearerToken } from '../../Constants/BearerToken';
import { useDispatch } from 'react-redux';
import * as BusinessActions from '../../store/actions/business';

const EditBusinessPhoto = props => {
    const dispatch = useDispatch();
    const[imageUri,setImage] = useState(null);

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

        console.log(result);

        if(!result.cancelled) {
        await setImage(result.uri);
        }
    }

    async function getPermission() {
        const status = await ImagePicker.requestCameraRollPermissionsAsync();
        if(status !== 'granted') {
            Alert.alert('Permission needed','We need permission to access your camera roll');
        }
    }

    async function onPressDone() {
        console.log("Done was pressed");
        const result = await ImageManipulator.manipulateAsync(imageUri, [], {base64: true});
        const imageCode = await result.base64;
        console.log(imageCode.length);
        if(imageCode.length===0) {
            Alert.alert('No image selected','Please choose an image');
        } else {
            const busObj = { 
                email: props.navigation.state.params.business.email,
                password: props.navigation.state.params.business.password,
                full_name: props.navigation.state.params.business.full_name,
                profile_image: "b'" + imageCode + "'",
                phone: props.navigation.state.params.business.phone,
                location: props.navigation.state.params.business.location.replace(/'/g,"\\'"),
                short_bio: props.navigation.state.params.business.short_bio.replace(/'/g,"\\'"),
                story: props.navigation.state.params.business.story.replace(/'/g,"\\'"),
                tags: props.navigation.state.params.business.tags,
                date_founded: props.navigation.state.params.business.date_founded,
                company_size: props.navigation.state.params.business.company_size,
                funding: props.navigation.state.params.business.funding,
                seeking_investment: props.navigation.state.params.business.seeking_investment,
                currently_hiring: props.navigation.state.params.business.currently_hiring
            }
            await dispatch(BusinessActions.putBusiness(busObj));
            await dispatch(BusinessActions.getBusiness(props.navigation.state.params.business.email));
            }
    }

    return(
        <View>
            <View style={styles.primaryContainer}>
                <Text style={styles.title}>Change your photo</Text>
                <Text style={styles.subtitle}>Upload a team photo or logo</Text>
                <View style={styles.camera}>
                    <TouchableOpacity style={styles.pictureButton} onPress={() => pickImage()}>
                        <Image source={(imageUri===null)? require('../../assets/blankImage.png') : {uri: imageUri}} style={styles.userImage}/>
                        <Text style={styles.add}>+</Text>
                    </TouchableOpacity>
                </View>
                <View style={{marginBottom: 200}}/>
                <BlackTag props={props.BlackTag} onPress={() => onPressDone()}>Done</BlackTag>   
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    title:  {
        color: 'black',
        fontFamily: 'Poppins-Bold',
        fontSize: 28,
        marginBottom: 20
    },
    subtitle: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        marginBottom: 10,
    },
    camera:{
        flex:1,
        marginTop:70,
        marginBottom:100,
    },
    primaryContainer: {
        marginHorizontal: 30,
        paddingTop: 70,
        marginBottom: 20,
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
    },
    userImage: {
        height: 230, 
        width: 230, 
        borderRadius: 5
    },
    add: {
        color:'white',
        fontSize:60,
        fontFamily:'Poppins-Thin',
        position:'absolute'
    }
})
export default EditBusinessPhoto;