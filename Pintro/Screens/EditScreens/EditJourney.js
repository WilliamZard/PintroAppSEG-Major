import React, { useState } from 'react';
import { View,StyleSheet,Text,TextInput,Picker,ScrollView } from 'react-native';
import Colors from '../../Constants/Colors';
import { fonts } from '../../Constants/Fonts';
import BlackTag from '../../Components/BlackTag.js';

const EditJourney = props => {
    const [companySize, setSize] = useState();
    const [funding, setFunding] = useState();
    const [founded, setDate] = useState();
    const [location, setLocation] = useState();

    function updateDate(newDate) {
        setDate(newDate);
    }

    function updateLocation(newLocation) {
        setLocation(newLocation);
    }
    
    function onSizePress(value) {
        setSize(value);
    }

    function onFundingPress(value) {
        setFunding(value);
    }

    function onPressDone() {
        console.log("Company size: " + companySize);
        console.log("Funding: " + funding);
        console.log("Date: " + founded);
        console.log("Location: " + location);
    }

    const item = {
        Date: "May 2017",
        Location: "Central London"
    }

    return(
        <ScrollView>
            <View style={styles.primaryContainer}>
                <Text style={styles.title}>Edit your details</Text>
                <Text style={styles.subtitle}>Your company journey</Text>
                <Text style={styles.subtitle}>Date Founded</Text>
                <TextInput style={styles.inputText} onChangeText={value => updateDate(value)}>{item.Date}</TextInput>
                <View style={styles.horizintalLineStyle}/>
                <Text style={styles.subtitle}>Location</Text>
                <TextInput style={styles.inputText} onChangeText={value => updateLocation(value)}>{item.Location}</TextInput>
                <View style={styles.horizintalLineStyle}/>
                <Text style={styles.subtitle}>Company Size</Text>
                <Picker
                selectedValue={companySize}
                onValueChange={(value) => onSizePress(value)}
                style={styles.inputText}>
                    <Picker.Item label="" value=""/>
                    <Picker.Item label="5 Team Members" value="five" />
                    <Picker.Item label="4 Team Members" value="four" />
                    <Picker.Item label="3 Team Members" value="three" />
                    <Picker.Item label="2 Team Members" value="two" />
                    <Picker.Item label="1 Team Member" value="one" />
                </Picker>
                <View style={styles.horizintalLineStyle}/>
                <Text style={styles.subtitle}>Funding</Text>
                <Picker
                selectedValue={funding}
                onValueChange={(value) => onFundingPress(value)}
                style={styles.inputText}>
                    <Picker.Item label="" value=""/>
                    <Picker.Item label="Pre-Seed" value="Pre-Seed" />
                    <Picker.Item label="Angel" value="Angel" />
                    <Picker.Item label="Venture" value="Venture" />
                </Picker>
                <View style={styles.horizintalLineStyle}/>
                <BlackTag props={props.BlackTag} onPress={() => onPressDone()}>Done</BlackTag>
            </View>
        </ScrollView>
        
    )
}

const styles = StyleSheet.create({
    primaryContainer: {
        marginHorizontal: 30,
        paddingTop: 70,
        marginBottom: 40,
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
    horizintalLineStyle:{
        borderBottomColor: 'black',
        borderBottomWidth: StyleSheet.hairlineWidth,
        marginBottom:40,
        marginTop:10,
    },
    inputText: {
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
    },
})

export default EditJourney;