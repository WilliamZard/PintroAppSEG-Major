import React, { useState } from 'react';
import { View,StyleSheet,Text,TextInput,ScrollView,TouchableOpacity,Image,Picker } from 'react-native';
import BlackTag from '../../Components/BlackTag.js';
import Colors from '../../Constants/Colors.js';

const EditIntro = props => {
    const [selectedValue1, setSelectedValue1] = useState();
    const [selectedValue2, setSelectedValue2] = useState();
    const [selectedValue3, setSelectedValue3] = useState();
    const [selectedValue4, setSelectedValue4] = useState();
    const [seekingInvest, setInvest] = useState(true);
    const [hiring, setHiring] = useState(false);
    const [investPic, setInvestPic] = useState(tick);
    const [hiringPic, setHiringPic] = useState(circle);
    const tick = require('../../assets/tickBlack.png');
    const circle = require('../../assets/blankCircle.png');

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
        setInvest(true);
        setHiring(false);
        if(!seekingInvest) {
            setInvestPic(tick);
            setHiringPic(circle); 
        }
    }

    function onPressHiring() {
        setHiring(true);
        setInvest(false);
        if(!hiring) {
            setHiringPic(tick);
            setInvestPic(circle);
        }
    }

    const item = {
        "email": "piing@pong.com",
        "password": "piin",
        "full_name": "Piin App Limited",
        "profile_image": "profile",
        "phone": "69",
        "location": "Central London",
        "short_bio": "Connect in Real Life",
        "story": "Lorem ipsum dolor sit amet, consecteteur adipiscing elit, sed do eiusmod tempor incididunt utt labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut  aliquip ex ea commod consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum."
    }

    return(
        <ScrollView>
            <View style={styles.primaryContainer}>
                <Text style={styles.title}>Edit your intro</Text>
                <Text style={styles.build}>Build your company profile</Text>
                <Text style={styles.subtitle}>Company Name</Text>
                <TextInput style={styles.inputText}>{item.full_name}</TextInput>
                <View style={styles.horizintalLineStyle}/>
                <Text style={styles.subtitle}>Tagline</Text>
                <TextInput style={styles.inputText}>{item.short_bio}</TextInput>
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
                <TextInput style={styles.inputText} multiline={true}>{item.story}</TextInput>
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
            <BlackTag props={props.BlackTag}>Done</BlackTag>
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