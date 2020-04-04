import React from 'react';
import { View,StyleSheet,Image,Text } from 'react-native';
import { fonts } from '../Constants/Fonts.js';

const JourneyPoint = props => {
    return(
        <View style={styles.rowContainer}>
            <Image source={require('../assets/yellowCircle.png')} style={{height: 15, width: 15, marginLeft: 30, marginRight: 15}}/>
            <Text style={fonts.title_black}>{props.default}</Text>
            <Text style={styles.info}>{props.userData}</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    rowContainer: {
        flexDirection: 'row',
        marginBottom: 10,
    },
    info: {
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize:12,
        marginLeft: 5,
    }
})

export default JourneyPoint;