import React from 'react';
import { Text, StyleSheet, TouchableOpacity, Image, View } from 'react-native';
import Colors from '../Constants/Colors';
import { fonts } from '../Constants/Fonts';

const HelpMeWith = props => {
    return(

        <TouchableOpacity style={styles.tag} onPress={props.onPress} activeOpacity={0.6}>
                <View>
                    <Text style={fonts.title_black}>Help us with</Text>
                    <Text style={fonts.bio}>{props.children}</Text>
                </View>
                <Image source={require('../assets/helpMeMsg.png')} style={{height: 50, width: 50, marginLeft: 70}}/> 
        </TouchableOpacity> 

    );
};

const styles = StyleSheet.create({
    tag: {
        borderColor: 'grey',
        color: Colors.pintroWhite,
        borderWidth:0.5,
        paddingVertical:12,
        paddingHorizontal:30,
        borderRadius:20,
        marginRight:10,
        marginTop:15,
        marginBottom:10,
        height: 80,
        width: 250,
        flexDirection: 'row'
    },
    tag_text: {
        color: Colors.pintroBlack,
        textAlign: 'center',
        fontFamily:'Poppins-Light',
        fontSize: 10
    }
});

export default HelpMeWith;