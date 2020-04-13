import React from 'react';
import { StyleSheet, View, TouchableOpacity, Image, Text } from 'react-native';
import { fonts } from '../Constants/Fonts.js';
const UserButton = props => {

    function onUserPress() {
        props.callback(props.email);
    }

    return (
        <TouchableOpacity style={styles.imageContainer} onPress={() => onUserPress()}>
            <Image source={require('../assets/blankImage.png')} style={styles.circleImage}/>
            <Text style={fonts.title_black}>{props.name}</Text>
        </TouchableOpacity>
    );
}

const styles = StyleSheet.create({
    circleImage: {
        width: 110,
        height: 110,
        borderRadius: 55,
        marginBottom: 10,
    },
    imageContainer: {
        marginHorizontal: 12,
        alignItems: 'center',
        justifyContent: 'center',
    }
});

export default UserButton;