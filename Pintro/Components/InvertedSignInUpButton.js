import React from 'react';
import {View,Text,StyleSheet,TouchableOpacity} from 'react-native';

const InvertedSignInUpButton = props => {
    return(

        <TouchableOpacity style = {{...styles.button, ...props.style}} onPress={props.onPress} activeOpacity={0.6}>

    <Text style={styles.buttonText}>{props.children}</Text>

        </TouchableOpacity>
    );
};

const styles = StyleSheet.create({
    button:{
        borderColor: 'black',
        borderWidth: 0.5,
        paddingVertical:12,
        width:'100%',
        paddingHorizontal:30,
        borderRadius:30,
        marginTop:10,
        backgroundColor:'white'

    },buttonText:{
        color:'black',
        textAlign: 'center',
        fontFamily:'Poppins-Regular'
    //fontFamily:'open-sans'

    }
});
export default InvertedSignInUpButton;