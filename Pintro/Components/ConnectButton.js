import React from 'react';
import { View,Text,TouchableOpacity,StyleSheet } from 'react-native';
import Colors from '../Constants/Colors'; 

const Connect = props => {

    function onPress() {
        console.log("You pressed new post");
    }

    return (
        <TouchableOpacity onPress={() => onPress()} style={styles.button} activeOpacity={0.6}>
            <View>
                <Text style={styles.whiteText}>CONNECT</Text>
            </View>
        </TouchableOpacity>
    )
}

const styles = StyleSheet.create({
    whiteText: {
        color: Colors.pintroWhite,
        textAlign: 'center',
        fontFamily:'Poppins-Regular',
        fontSize: 10
    },
    button: {
        borderColor: Colors.pintroBlack,
        backgroundColor: Colors.pintroBlack,
        borderWidth: 0.5,
        paddingVertical:12,
        paddingHorizontal:40,
        borderRadius:13,
        marginTop:10,
        marginRight:10,
        marginLeft:10,
        marginBottom:15,
    }
})
export default Connect;