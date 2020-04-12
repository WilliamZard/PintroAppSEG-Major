import React, { useState } from 'react';
import { View,Text,TouchableOpacity,Alert } from 'react-native';
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
    const[buttonText,setText] = useState((following)? props.choice2 : props.choice1)
    
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
            Alert.alert(
                'Unfollow request',
                'Are you sure you want to delete your request to follow ' + props.name,
                [
                    {text: 'Delete', onPress: () => (
                        setColor(Colors.pintroBlack),
                        setTextStyle(whiteText),
                        setText(props.choice1),
                        setFollow(false)
                        //dispatch(RequestActions.requestFol(currentUser,businessObj.email));
                    )},
                    {text: 'Cancel', onPress: () => console.log("Cancel was pressed"), style: 'cancel'}
                ] 
            )
        } else {
            Alert.alert(
                'Follow request',
                'Are you sure you want to request to follow ' + props.name,
                [
                    {text: 'Request', onPress: () => (
                        setColor(Colors.pintroWhite),
                        setTextStyle(blackText),
                        setText(props.choice2),
                        setFollow(true)
                        //dispatch(RequestActions.requestFol(currentUser,businessObj.email));
                    )},
                    {text: 'Cancel', onPress: () => console.log("Request was pressed"), style: 'cancel'}
                ] 
            );
        }
    }

    return (
        <TouchableOpacity onPress={() => onPress()} style={button} activeOpacity={0.6}>
            <View>
                <Text style={textStyle}>{buttonText}</Text>
            </View>
        </TouchableOpacity>
    )
}

export default FollowMe;