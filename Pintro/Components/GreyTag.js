import React, { useState } from 'react';
import { View,Text,TouchableOpacity } from 'react-native';
import Colors from '../Constants/Colors.js';

const GreyTag = props => {
    const greyTag = {
            borderColor: '#c2c2c4',
            backgroundColor: '#c2c2c4',
            borderWidth: 0.5,
            paddingVertical: 10,
            paddingHorizontal: 28,
            borderRadius: 24,
            marginHorizontal: 5,
        };

        const blackTag = {
            borderColor: Colors.pintroBlack,
            backgroundColor: Colors.pintroBlack,
            borderWidth: 0.5,
            paddingVertical: 10,
            paddingHorizontal: 28,
            borderRadius: 24,
            marginHorizontal: 5,
        };

        const blackText = {
            color: Colors.pintroBlack,
            textAlign: 'center',
            fontFamily: 'Poppins-Regular',
            fontSize: 12
        }

        const whiteText = {
            color: Colors.pintroWhite,
            textAlign: 'center',
            fontFamily: 'Poppins-Regular',
            fontSize: 12
        }
    const[selected,select] = useState(props.initial);
    const[tagStyle,setTag] = useState((selected)? blackTag : greyTag);
    const[tagText,setText] = useState((selected)? whiteText : blackText);
    

    

    function onTagPress() {
        if(selected) {
            setTag(greyTag);
            setText(blackText);
            select(false);
            props.callback(props.val);
        } else {
            setTag(blackTag);
            setText(whiteText);
            select(true);
            props.callback(props.val);
        }
    }

    return(
        <TouchableOpacity onPress={() => onTagPress()} activeOpacity={0.6}>
            <View style={tagStyle}>
                <Text style={tagText}>{props.children}</Text>
            </View>
        </TouchableOpacity> 
    );
};


export default GreyTag;