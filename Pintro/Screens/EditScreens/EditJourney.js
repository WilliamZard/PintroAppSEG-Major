import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { View,StyleSheet,Text,TextInput,Picker,ScrollView } from 'react-native';
import Colors from '../../Constants/Colors';
import BlackTag from '../../Components/BlackTag.js';
import * as BusinessActions from '../../store/actions/business.js';

const EditJourney = props => {
    const dispatch = useDispatch();
    const [companySize, setSize] = useState(props.navigation.state.params.business.company_size);
    const [funding, setFunding] = useState(props.navigation.state.params.business.funding);
    const [founded, setDate] = useState(props.navigation.state.params.business.date_founded);
    const [location, setLocation] = useState(props.navigation.state.params.business.location);

    function updateDate(newDate) {
        setDate(newDate);
    }

    function updateLocation(newLocation) {
        setLocation(newLocation.replace(/'/g,"\\'"));
    }
    
    function onSizePress(value) {
        setSize(value);
    }

    function onFundingPress(value) {
        setFunding(value);
    }

    async function onPressDone() {
        const busObj = {
            email: props.navigation.state.params.business.email,
            password: props.navigation.state.params.business.password,
            full_name: props.navigation.state.params.business.full_name.replace(/'/g,"\\'"),
            profile_image: props.navigation.state.params.business.profile_image,
            phone: props.navigation.state.params.business.phone,
            location: location,
            short_bio: props.navigation.state.params.business.short_bio.replace(/'/g,"\\'"),
            story: props.navigation.state.params.business.story.replace(/'/g,"\\'"),
            tags: props.navigation.state.params.business.tags,
            date_founded: founded,
            company_size: companySize,
            funding: funding,
            team_members: props.navigation.state.params.business.team_members,
            seeking_investment: props.navigation.state.params.business.seeking_investment,
            currently_hiring: props.navigation.state.params.business.currently_hiring
        }
        dispatch(BusinessActions.putBusiness(busObj));
        dispatch(BusinessActions.getBusiness(props.navigation.state.params.business.email));
    }

    return(
        <ScrollView>
            <View style={styles.primaryContainer}>
                <Text style={styles.title}>Edit your details</Text>
                <Text style={styles.subtitle}>Your company journey</Text>
                <Text style={styles.subtitle}>Date Founded</Text>
                <TextInput style={styles.inputText} onChangeText={value => updateDate(value)}>{props.navigation.state.params.business.date_founded}</TextInput>
                <View style={styles.horizintalLineStyle}/>
                <Text style={styles.subtitle}>Location</Text>
                <TextInput style={styles.inputText} onChangeText={value => updateLocation(value)}>{props.navigation.state.params.business.location}</TextInput>
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