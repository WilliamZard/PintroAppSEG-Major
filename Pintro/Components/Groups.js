import React from 'react';
import { View, Text, Image, StyleSheet } from 'react-native';
import Colors from '../Constants/Colors.js';
import { fonts } from '../Constants/Fonts.js';
const Groups = props => {
    
    return (
        <View style={styles.rowContainer}>
            <Image source={require('../assets/blankImage.png')} style={styles.circleImage}/>
            <View style={styles.textContainer}>
                <Text style={styles.title}>{props.name}</Text>
                <Text style={styles.subtitle}>{props.members}</Text> 
            </View>
            <Image source={require('../assets/thumbnail.png')} style={styles.thumbnail}/>
        </View>
    )
}

const styles = StyleSheet.create({
    rowContainer: {
        flexDirection: 'row',
        marginLeft: 20,
        backgroundColor: 'white',
        marginBottom: 10,
        borderRadius: 20,
        width: 375,
        height: 75,
    },
    circleImage: {
        width: 40,
        height: 40,
        borderRadius: 20,
        marginBottom: 10,
        marginTop: 17,
        marginLeft: 10,
    },
    title: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        fontSize: 12,
        marginLeft: 10,
    },
    subtitle: {
        color: 'grey',
        fontFamily: 'Poppins-Light',
        fontSize: 10,
        marginLeft: 10,
    },
    textContainer: {
        marginTop: 18,
    },
    thumbnail: {
        flex: 1,
        width: 40,
        height: 30,
        resizeMode: 'contain',
        marginTop: 20,
        marginLeft: 110,
    }
});

export default Groups;