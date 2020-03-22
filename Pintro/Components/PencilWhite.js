import React from 'react';
import { StyleSheet,TouchableOpacity,Image } from 'react-native';
import Colors from '../Constants/Colors'; 

const PencilWhite = props => {
    <TouchableOpacity>
        <Image source={require('../assets/whitePencil.png')}/>
    </TouchableOpacity>
};

const styles = StyleSheet.create({

});

export default PencilWhite;