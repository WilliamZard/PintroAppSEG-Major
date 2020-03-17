import React from 'react';
import {View,Text,StyleSheet,TouchableOpacity} from 'react-native';
import Colors from '../Constants/Colors';
import { fonts } from '../Constants/Fonts';

const HelpMeWith = props => {
    return(

        <TouchableOpacity style={styles.tag} onPress={props.onPress} activeOpacity={0.6}>
                <Text style={fonts.title_black}>Help us with</Text>
                <Text style={fonts.bio}>{props.children}</Text>
        </TouchableOpacity> 

    );
};

const styles = StyleSheet.create({
    tag: {
        borderColor: Colors.pintroBlack,
        color: Colors.pintroWhite,
        borderWidth:0.5,
        width:'15%',
        paddingVertical:12,
        paddingHorizontal:30,
        borderRadius:20,
        marginRight:10,
        marginTop:15,
        marginBottom:10
    },
    tag_text: {
        color: Colors.pintroBlack,
        textAlign: 'center',
        fontFamily:'Poppins-Light',
        fontSize: 10
    }
});

export default HelpMeWith;