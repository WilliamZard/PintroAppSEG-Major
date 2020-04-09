import React, { useState } from 'react';
import { View,Text,StyleSheet,TouchableOpacity } from 'react-native';
import Colors from '../Constants/Colors'; 

const FollowMe = props => {
    const whiteText = {
        color: Colors.pintroWhite,
        textAlign: 'center',
        fontFamily:'Poppins-Regular',
        fontSize: 10
    }

    const blackText = {
        color: Colors.pintroBlack,
        textAlign: 'center',
        fontFamily:'Poppins-Regular',
        fontSize: 10
    }
    
    const[following,setFollow] = useState(props.initial);
    const[textStyle,setTextStyle] = useState((following)? blackText : blackText);
    const[color,setColor] = useState((following)? Colors.pintroWhite : Colors.pintroBlack);
    const[buttonText,setText] = useState((following)? "+ FOLLOW US" : "UNFOLLOW")
    
    const button = {
        borderColor: Colors.pintroBlack,
        backgroundColor: color,
        borderWidth: 0.5,
        paddingVertical:12,
        paddingHorizontal:50,
        borderRadius:13,
        marginTop:10,
        marginRight:10,
        marginLeft:10,
        marginBottom:15,
    }


    function onPress() {
        if(following) {
            setColor(Colors.pintroBlack);
            setTextStyle(whiteText);
            setText("+ FOLLOW US")
            setFollow(false);
        } else {
            setColor(Colors.pintroWhite);
            setTextStyle(blackText);
            setText("UNFOLLOW")
            setFollow(true);
        }
        props.callback();
    }

    return (
        <TouchableOpacity onPress={() => onPress()} style={button} activeOpacity={0.6}>
            <View>
                <Text style={textStyle}>{buttonText}</Text>
            </View>
        </TouchableOpacity>
    )
}

const styles = StyleSheet.create({
    button:{
        borderColor: Colors.pintroBlack,
        backgroundColor: Colors.pintroBlack,
        borderWidth: 0.5,
        paddingVertical:12,
        paddingHorizontal:50,
        borderRadius:13,
        marginTop:10,
        marginRight:10,
        marginLeft:10,
        marginBottom:15,
    },
    buttonText:{
        color: Colors.pintroWhite,
        textAlign: 'center',
        fontFamily:'Poppins-Regular',
        fontSize: 10
    }
});

export default FollowMe;