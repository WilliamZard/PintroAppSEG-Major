import React from 'react';
import {View,Text,StyleSheet,TouchableOpacity} from 'react-native';

const SignInUpButton = props => {
    return(

        <TouchableOpacity onPress={props.onPress} activeOpacity={0.6}>
            <View style = {styles.button}>
    <Text style={styles.buttonText}>{props.children}</Text>
            </View>
        </TouchableOpacity>
    );
};

const styles = StyleSheet.create({
    button:{
        borderColor: 'white',
        borderWidth: 0.5,
        paddingVertical:12,
        width:'100%',
        paddingHorizontal:30,
        borderRadius:13,
        marginTop:10

    },buttonText:{
        color:'white',
        textAlign: 'center',
        fontFamily:'Poppins-Regular'
    //fontFamily:'open-sans'

    }
});
export default SignInUpButton;