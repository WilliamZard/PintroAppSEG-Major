import React from 'react';
import { Text, StyleSheet, TouchableOpacity, Image, View } from 'react-native';
import Colors from '../Constants/Colors';


const HelpUsWith = props => {
    return(

        <TouchableOpacity style={styles.tag} onPress={props.onPress} activeOpacity={0.6}>
                <View style={styles.textContainer}>
                    <Text style={styles.tag_text}>Help us with</Text>
                    <Text style={styles.userHelp}>{props.children}</Text>
                </View>
                <Image source={require('../assets/helpMeMsg.png')} style={styles.msgImage}/> 
        </TouchableOpacity> 

    );
};

const styles = StyleSheet.create({
    tag: {
        borderColor: 'grey',
        color: Colors.pintroWhite,
        borderWidth: 0.5,
        paddingVertical: 12,
        paddingHorizontal: 30,
        borderRadius: 20,
        marginRight: 10,
        marginTop: 15,
        marginBottom: 10,
        height: 80,
        width: 250,
        flexDirection: 'row'
    },
    tag_text: {
        color: Colors.pintroBlack,
        textAlign: 'center',
        fontFamily:'Poppins-Bold',
        fontSize: 16,
        marginTop: 5,
        alignSelf: 'flex-start',
    },
    userHelp: {
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize: 12
    },
    msgImage: {
        height: 50, 
        width: 50, 
        marginLeft: 30,
        marginBottom: 40
    },
    textContainer: {
        width: 125
    }
});

export default HelpUsWith;