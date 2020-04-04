import React from 'react';
import { View,StyleSheet,Text,TouchableOpacity,Image,TextInput,Picker } from 'react-native';
import {fonts} from '../../Constants/Fonts';
import Colors from '../../Constants/Colors';
import BlackTag from '../../Components/BlackTag';

const EditYourTeam = props => {

    function onTextChanged(value){
        "do nothing";
    }

    return (
        <View style={styles.primaryContainer}>
            <Text style={styles.title}>Edit your team</Text>
            <Text style={styles.search}>Search and invite your people</Text>
            <Text style={styles.subtitle}>Team member name</Text>
            <View style={styles.rowContainer}>
                <TextInput 
                style={styles.inputText} 
                onChangeText={value => onTextChanged(value)}>
                    Start typing...
                </TextInput>
                <Picker style={{borderWidth: 1}}></Picker>
            </View>
            <View style={styles.horizintalLineStyle}/>
            <Text style={styles.subtitle}>Current members:</Text>
            <TouchableOpacity>
                <View style={styles.teamContainer}>
                    <Image source={require('../../assets/blankImage.png')} style={styles.circleImage}/>
                    <View style={styles.textContainer}>
                        <Text style={fonts.title_black}>Danielle Dodoo</Text>
                        <Text style={fonts.story}>Founder</Text>
                    </View>
                    <Image source={require('../../assets/cross.png')} style={styles.cross}/>
                </View>
            </TouchableOpacity>
            <TouchableOpacity>
                <View style={styles.teamContainer}>
                    <Image source={require('../../assets/blankImage.png')} style={styles.circleImage}/>
                    <View style={styles.textContainer}>
                        <Text style={fonts.title_black}>Callum Thompson</Text>
                        <Text style={fonts.story}>Graphic Designer</Text>
                    </View>
                    <Image source={require('../../assets/cross.png')} style={styles.cross}/>
                </View>
            </TouchableOpacity>
            <BlackTag props={props.BlackTag}>Done</BlackTag>
        </View>
    )
}

const styles = StyleSheet.create({
    title:  {
        color: 'black',
        fontFamily: 'Poppins-Bold',
        fontSize: 28,
    },
    subtitle: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        marginBottom: 10,
    },
    inputText: {
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        height: 50, 
        width: 370
    },
    rowContainer: {
        flexDirection: 'row'
    },
    horizintalLineStyle:{
        borderBottomColor: 'black',
        borderBottomWidth: StyleSheet.hairlineWidth,
        marginBottom:30,
        marginTop:10,
    },
    primaryContainer: {
        marginHorizontal: 30,
        paddingTop: 70,
        marginBottom: 20,
    },
    search: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        marginBottom: 50,
    },
    teamContainer: {
        flexDirection: 'row',
        backgroundColor: 'white',
        marginBottom: 10,
        borderRadius: 20,
        width: 370,
        height: 75,
    },
    circleImage: {
        width: 40,
        height: 40,
        borderRadius: 20,
        marginBottom: 10,
        marginTop: 17,
        marginHorizontal: 10,
    },
    textContainer: {
        marginTop: 18,
        flex: 1
    },
    cross: {
        height: 20, 
        width: 20, 
        marginTop: 30, 
        marginRight: 20
    }
})

export default EditYourTeam;