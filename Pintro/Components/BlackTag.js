import React from 'react';
import { View,Text,StyleSheet,TouchableOpacity } from 'react-native';
import Colors from '../Constants/Colors';

const BlackTag = props => {
    return(
        <TouchableOpacity style={styles.tag} onPress={props.onPress} activeOpacity={0.6}>
                <Text style={styles.tag_text}>{props.children}</Text>
        </TouchableOpacity> 
    );
};

const styles = StyleSheet.create({
    tag: {
        borderColor: Colors.pintroBlack,
        backgroundColor: Colors.pintroBlack,
        borderWidth:0.5,
        width:'10%',
        paddingVertical:12,
        paddingHorizontal:30,
        borderRadius:20,
        marginRight:10,
        marginTop:15,
        marginBottom:10
    },
    tag_text: {
        color: Colors.pintroWhite,
        textAlign: 'center',
        fontFamily:'Poppins-Light',
        fontSize: 10
    }
});

export default BlackTag;