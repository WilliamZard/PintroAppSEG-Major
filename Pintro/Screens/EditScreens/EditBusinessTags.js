import React, { useState } from 'react';
import { View,StyleSheet,Text,Picker } from 'react-native';
import Colors from '../../Constants/Colors.js';
import BlackTag from '../../Components/BlackTag.js';
import GreyTag from '../../Components/GreyTag.js';
import { TextInput, ScrollView } from 'react-native-gesture-handler';

const EditBusinessTag = props => {
    const [chosenTags,setChosenTags] = useState([]);
    
    return(
        <ScrollView>
            <View style={styles.primaryContainer}>
                <Text style={styles.title}>Edit your Tags</Text>
                <Text style={styles.categorise}>Categorise your business (3 minimum)</Text>
                <Text style={styles.subtitle}>Choose from the full list</Text>
                <View style={styles.rowContainer}>
                    <TextInput style={styles.inputText} onChangeText={value => value}>Start typing...</TextInput>
                    <Picker style={{borderWidth: 1}}></Picker>
                </View>
                <View style={styles.horizintalLineStyle}/>
                <Text style={styles.subtitle}>Or choose from the most popular</Text>
                <View style={styles.tagContainer}>
                    <GreyTag props={props.GreyTag}>FEMINISIM</GreyTag>
                    <GreyTag props={props.GreyTag}>START-UP</GreyTag>
                    <GreyTag props={props.GreyTag}>MINDFULNESS</GreyTag>
                </View>
                <View style={styles.tagContainer}>
                    <GreyTag props={props.GreyTag}>PERSONAL GROWTH</GreyTag>
                    <GreyTag props={props.GreyTag}>APP</GreyTag>
                    <GreyTag props={props.GreyTag}>NETWORKING</GreyTag>
                </View>
                <View style={styles.tagContainer}>
                    <GreyTag props={props.GreyTag}>NEUROSCIENCE</GreyTag>
                    <GreyTag props={props.GreyTag}>NUTRITION</GreyTag>
                    <GreyTag props={props.GreyTag}>INNOVATION</GreyTag>
                </View>
                <View style={styles.tagContainer}>
                    <GreyTag props={props.GreyTag}>PRE-SEED</GreyTag>
                    <GreyTag props={props.GreyTag}>DIVERSITY</GreyTag>
                    <GreyTag props={props.GreyTag}>CO-WORKING</GreyTag>
                </View>
                <View style={{marginVertical: 20}}/>
                <BlackTag props={props.BlackTag}>Done</BlackTag>
            </View>
        </ScrollView>
        
    )
}

const styles = {
    horizintalLineStyle:{
        borderBottomColor: 'black',
        borderBottomWidth: StyleSheet.hairlineWidth,
        marginBottom:30,
        marginTop:10,
    },
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
    primaryContainer: {
        marginHorizontal: 30,
        paddingTop: 70,
        marginBottom: 20,
    },
    categorise: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        marginTop: 10,
        marginBottom: 50,
    },
    rowContainer: {
        flexDirection: 'row',
    },
    inputText: {
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
    },
    inputText: {
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        height: 50, 
        width: 370
    },
    tagContainer: {
        flexDirection: 'row',
        marginLeft: -35,
        marginBottom: 10,
    },
}

export default EditBusinessTag;