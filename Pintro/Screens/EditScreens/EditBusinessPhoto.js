import React from 'react';
import { View,TouchableOpacity,Text,Image,StyleSheet } from 'react-native';
import BlackTag from '../../Components/BlackTag';
import Colors from '../../Constants/Colors';

const EditBusinessPhoto = props => {
    return(
        <View>
            <View style={styles.primaryContainer}>
                <Text style={styles.title}>Change your photo</Text>
                <Text style={styles.subtitle}>Upload a team photo or logo</Text>
                <View style={styles.camera}>
                    <TouchableOpacity style={styles.pictureButton}>
                        <Image source={require('../../assets/blankImage.png')} style={styles.userImage}/>
                        <Text style={styles.add}>+</Text>
                    </TouchableOpacity>
                </View>
                <View style={{marginBottom: 200}}/>
                <BlackTag props={props.BlackTag}>Done</BlackTag>   
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