import React from 'react';
import { StyleSheet,TouchableOpacity,Image } from 'react-native';
import Colors from '../Constants/Colors'; 

const PencilBlack = props => {
    <TouchableOpacity>
        <Image source={require('../assets/blackPencil.png')}/>
    </TouchableOpacity>
};

const styles = StyleSheet.create({

});

export default PencilBlack;