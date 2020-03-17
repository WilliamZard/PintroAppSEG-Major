import React from 'react';
import {View,Text,StyleSheet,TouchableOpacity} from 'react-native';

const BlackTag = props => {
    return(
        <TouchableOpacity onPress={props.onPress} activeOpacity={0.6}>
            <View style={styles.tag}>
                <Text style={stlyes.tag_text}>{props.children}</Text>
            </View>
        </TouchableOpacity> 
    );
};

const styles = StyleSheet.create({
    tag: {
        borderColor: Colors.pintroBlack,
        color: Colors.pintroBlack,
        borderWidth: 0.5,
        paddingVertical:12,
        paddingHorizontal:30,
        borderRadius:13
    },
    tag_text: {
        color: Colors.pintroWhite,
        textAlign: 'center',
        fontFamily:'Poppins-Light',
        fontSize: 10
    }
});

export default BlackTag;