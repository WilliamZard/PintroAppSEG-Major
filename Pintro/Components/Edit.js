import React from 'react';
import { View,Text,StyleSheet,TouchableOpacity } from 'react-native';
import Colors from '../Constants/Colors';

const Edit = props => {
    return(

        <TouchableOpacity style={styles.button} onPress={props.onPress} activeOpacity={0.6}>
            <Text style={styles.buttonText}>{props.children}</Text>
        </TouchableOpacity>

    );
};

const styles = StyleSheet.create({
    button:{
        borderColor: Colors.pintroBlack,
        borderWidth: 0.5,
        paddingVertical:12,
        width:'7%',
        paddingHorizontal:30,
        borderRadius:13,
        marginTop:10
    },
    buttonText:{
        color: Colors.pintroBlack,
        textAlign: 'center',
        fontFamily:'Poppins-Light'

    }
});

export default Edit;