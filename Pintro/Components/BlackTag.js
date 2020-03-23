import React from 'react';
import {View,Text,StyleSheet,TouchableOpacity} from 'react-native';
import Colors from '../Constants/Colors.js';

const BlackTag = props => {
    return(
        <TouchableOpacity onPress={props.onPress} activeOpacity={0.6}>
            <View style={styles.tag}>
                <Text style={styles.tag_text}>{props.children}</Text>
            </View>
        </TouchableOpacity> 
    );
};

const styles = StyleSheet.create({
    tag: {
        borderColor: Colors.pintroBlack,
        backgroundColor: 'black',
        borderWidth: 0.5,
        paddingVertical: 12,
        paddingHorizontal: 30,
        borderRadius: 24,
        marginHorizontal: 5,
    },
    tag_text: {
        color: Colors.pintroWhite,
        textAlign: 'center',
        fontFamily:'Poppins-Regular',
        fontSize: 12
    }
});

export default BlackTag;