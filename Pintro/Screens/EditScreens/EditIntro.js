import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { View,StyleSheet,Text,TextInput,ScrollView,TouchableOpacity,Image,Picker } from 'react-native';
import BlackTag from '../../Components/BlackTag.js';
import Colors from '../../Constants/Colors.js';
import * as BusinessActions from '../../store/actions/business.js';

const EditIntro = props => {
    const dispatch = useDispatch();
    const [selectedValue1, setSelectedValue1] = useState();
    const [selectedValue2, setSelectedValue2] = useState();
    const [selectedValue3, setSelectedValue3] = useState();
    const [selectedValue4, setSelectedValue4] = useState();
    const [seekingInvest, setInvest] = useState(props.navigation.state.params.business.seeking_investment);
    const [hiring, setHiring] = useState(props.navigation.state.params.business.currently_hiring);
    const tick = require('../../assets/tickBlack.png');
    const circle = require('../../assets/blankCircle.png');
    const [investPic, setInvestPic] = useState((seekingInvest==="True") ? tick : circle);
    const [hiringPic, setHiringPic] = useState((hiring==="True") ? tick : circle);

    const [name,setName] = useState(props.navigation.state.params.business.full_name);
    const [bio,setBio] = useState(props.navigation.state.params.business.short_bio);
    const [story,setStory] = useState(props.navigation.state.params.business.story);

    function onItemPress1(value) {
        setSelectedValue1(value);
    }

    function onItemPress2(value) {
        setSelectedValue2(value);
    }

    function onItemPress3(value) {
        setSelectedValue3(value);
    }

    function onItemPress4(value) {
        setSelectedValue4(value);
    }

    function onPressInvest() {
        if(seekingInvest === true) {
            setInvest(false);
            setInvestPic(circle);
        } else {
            setInvest(true);
            setInvestPic(tick);
        }
    }

    async function onPressDone() {
        const busObj = {
            email: props.navigation.state.params.business.email,
            password: props.navigation.state.params.business.password,
            full_name: name,
            profile_image: props.navigation.state.params.business.profile_image,
            phone: props.navigation.state.params.business.phone,
            location: props.navigation.state.params.business.location.replace(/'/g,"\\'"),
            short_bio: bio,
            story: story,
            tags: props.navigation.state.params.business.tags,
            date_founded: props.navigation.state.params.business.date_founded,
            company_size: props.navigation.state.params.business.company_size,
            funding: props.navigation.state.params.business.funding,
            seeking_investment: seekingInvest,
            currently_hiring: hiring
        };
        await dispatch(BusinessActions.putBusiness(busObj));
        await dispatch(BusinessActions.getBusiness(props.navigation.state.params.business.email));       
    }

    function updateName(newName) {
        setName(newName.replace(/'/g,"\\'"));
    }

    function updateBio(newBio) {
        setBio(newBio.replace(/'/g,"\\'"));
    }

    function updateStory(newStory) {
        setStory(newStory.replace(/'/g,"\\'"));
    }

    function onPressHiring() {
        if(hiring === true) {
            setHiring(false);
            setHiringPic(circle);
        } else {
            setHiring(true);
            setHiringPic(tick);
        }
    }

    return(
        <ScrollView>
            <View style={styles.primaryContainer}>
                <Text style={styles.title}>Edit your intro</Text>
                <Text style={styles.build}>Build your company profile</Text>
                <Text style={styles.subtitle}>Company Name</Text>
                <TextInput style={styles.inputText} onChangeText={value => updateName(value)}>{props.navigation.state.params.business.full_name}</TextInput>
                <View style={styles.horizintalLineStyle}/>
                <Text style={styles.subtitle}>Tagline</Text>
                <TextInput style={styles.inputText} onChangeText={value => updateBio(value)}>{props.navigation.state.params.business.short_bio}</TextInput>
                <View style={styles.horizintalLineStyle}/>
                <Text style={styles.subtitle}>Are you..?</Text>
                <View style={styles.buttonContainer}>
                    <TouchableOpacity onPress={() => onPressInvest()}>
                        <View style={styles.tag}>
                            <Image source={investPic} style={{width: 20, height: 20, marginLeft: 5, marginRight: 20}}/>
                            <Text>Seeking Investment</Text>
                        </View>
                    </TouchableOpacity>
                    <TouchableOpacity onPress={() => onPressHiring()}>
                        <View style={styles.tag}>
                            <Image source={hiringPic} style={{width: 20, height: 20, marginLeft: 5, marginRight: 20}}/>
                            <Text>Currently Hiring</Text>
                        </View>
                    </TouchableOpacity>
                </View>                
                <Text style={styles.subtitle}>Company Story</Text>
                <TextInput style={styles.inputText} multiline={true} onChangeText={value => updateStory(value)}>{props.navigation.state.params.business.story}</TextInput>
                <View style={styles.horizintalLineStyle}></View>
                <Text style={styles.subtitle}>Social Media</Text>
                <View style={styles.rowContainer}>
                    <View style={{flex: 1}}>
                        <Picker 
                        selectedValue={selectedValue1} 
                        onValueChange={(value) => onItemPress1(value)}
                        style={styles.inputText}>
                            <Picker.Item label="" value=""/>
                            <Picker.Item label="Instagram" value="ig" />
                            <Picker.Item label="Facebook" value="fb" />
                            <Picker.Item label="LinkedIn" value="li" />
                            <Picker.Item label="Website" value="web" />
                        </Picker>
                        <View />
                        <View style={styles.horizintalLineStyle}/>
                    </View>
                    <View style={{marginLeft: 30}}>
                        <TextInput style={{height: 50, width: 180}}></TextInput>
                        <View style={styles.horizintalLineStyle}/>
                    </View> 
                </View>
                <View style={styles.rowContainer}>
                    <View style={{flex: 1}}>
                        <Picker
                        selectedValue={selectedValue2} 
                        onValueChange={(value) => onItemPress2(value)}
                        style={styles.inputText}>
                            <Picker.Item label="" value=""/>
                            <Picker.Item label="Instagram" value="ig" />
                            <Picker.Item label="Facebook" value="fb" />
                            <Picker.Item label="LinkedIn" value="li" />
                            <Picker.Item label="Website" value="web" />
                        </Picker>
                        <View />
                        <View style={styles.horizintalLineStyle}/>
                    </View>
                    <View style={{marginLeft: 30}}>
                        <TextInput style={{height: 50, width: 180}}></TextInput>
                        <View style={styles.horizintalLineStyle}/>
                    </View> 
                </View>
                <View style={styles.rowContainer}>
                    <View style={{flex: 1}}>
                        <Picker
                        selectedValue={selectedValue3} 
                        onValueChange={(value) => onItemPress3(value)}
                        style={styles.inputText}>
                            <Picker.Item label="" value=""/>
                            <Picker.Item label="Instagram" value="ig" />
                            <Picker.Item label="Facebook" value="fb" />
                            <Picker.Item label="LinkedIn" value="li" />
                            <Picker.Item label="Website" value="web" />
                        </Picker>
                        <View />
                        <View style={styles.horizintalLineStyle}/>
                    </View>
                    <View style={{marginLeft: 30}}>
                        <TextInput style={{height: 50, width: 180}}></TextInput>
                        <View style={styles.horizintalLineStyle}/>
                    </View> 
                </View>
                <View style={styles.rowContainer}>
                    <View style={{flex: 1}}>
                        <Picker
                        selectedValue={selectedValue4} 
                        onValueChange={(value) => onItemPress4(value)}
                        style={styles.inputText}>
                            <Picker.Item label="" value=""/>
                            <Picker.Item label="Instagram" value="ig" />
                            <Picker.Item label="Facebook" value="fb" />
                            <Picker.Item label="LinkedIn" value="li" />
                            <Picker.Item label="Website" value="web" />
                        </Picker>
                        <View />
                        <View style={styles.horizintalLineStyle}/>
                    </View>
                    <View style={{marginLeft: 30}}>
                        <TextInput style={{height: 50, width: 180}}></TextInput>
                        <View style={styles.horizintalLineStyle}/>
                    </View> 
                </View>
            </View> 
            <BlackTag props={props.BlackTag} onPress={() => onPressDone()}>Done</BlackTag>
        </ScrollView>
    );
}

const styles = StyleSheet.create({
    horizintalLineStyle:{
        borderBottomColor: 'black',
        borderBottomWidth: StyleSheet.hairlineWidth,
        marginBottom:30,
        marginTop:10,
    },
    title:  {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        fontSize: 28,
        flex: 1, 
    },
    primaryContainer: {
        marginHorizontal: 30,
        marginTop: 70,
    },
    subtitle: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        marginBottom: 10,
    },
    build: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
        marginTop: 10,
        marginBottom: 40,
    },
    tag: {
        borderColor: Colors.pintroBlack,
        color: Colors.pintroWhite,
        borderWidth: 0.5,
        paddingVertical: 10,
        paddingRight: 15,
        borderRadius: 19,
        flexDirection: 'row',
        marginRight: 10,
    },
    buttonContainer: {
        flexDirection: 'row',
        marginBottom: 40,
    },
    rowContainer: {
        flexDirection: 'row',
        flex: 1
    },
    inputText: {
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize: 12,
    }
})
export default EditIntro;