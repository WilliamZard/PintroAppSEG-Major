import React from 'react';
import { View,Text,StyleSheet,Image } from 'react-native';
import { fonts } from '../Constants/Fonts.js';
import Colors  from '../Constants/Colors.js';

const WorkingSpace = props => {

    return (
        <View style={styles.rowContainer}>
            <Image source={require('../assets/blankImage.png')} style={styles.spaceImage}/>
            <View style={styles.textView}>
                <Text style={fonts.title_black}>{props.name}</Text>
                <View style={styles.textRow}>
                    <Text style={styles.spaceSpecs}>{props.spaces}</Text>
                    <Text style={styles.spaceSpecs}> {props.cost}</Text>
                </View>
                <Text style={styles.story}>{props.story}</Text>
                <Text style={styles.view}>View  --></Text>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    rowContainer:{
        flexDirection: 'row',
        marginLeft: 20,
        marginTop: 10,
    },
    spaceImage: {
        borderRadius: 20,
        height: 110,
        width: 110,
    },
    textView: {
        marginLeft: 10,
        marginTop: 5,
    },
    textRow: {
        flexDirection: 'row',
    },
    view: {
        color: Colors.pintroYellow,
        fontFamily: 'Poppins-Bold',
        fontSize: 10
    },
    story:{
        color: 'grey',
        fontFamily: 'Poppins-Light',
        fontSize: 10,
        marginTop: 10,
        marginBottom: 10,
    },
    spaceSpecs: {
        color: 'grey',
        fontFamily: 'Poppins-Regular',
        fontSize: 10,
    }
});

export default WorkingSpace;