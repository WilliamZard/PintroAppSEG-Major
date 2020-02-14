import React from 'react';
import {View,Text,StyleSheet,TouchableOpacity} from 'react-native';
import Colors from '../Constants/Colors';

const WhiteTag = props => {
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
        color: Colors.pintroWhite,
        borderWidth: 0.5,
        paddingVertical:12,
        paddingHorizontal:30,
        borderRadius:13
    },
    tag_text: {
        color: Colors.pintroBlack,
        textAlign: 'center',
        fontFamily:'Poppins-Light',
        fontSize: 10
    }
});

export default WhiteTag;