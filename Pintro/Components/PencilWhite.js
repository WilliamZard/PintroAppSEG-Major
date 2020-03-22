import React from 'react';
import { StyleSheet,TouchableOpacity,Image } from 'react-native';

const PencilWhite = props => {
    
    return(
        <TouchableOpacity>
            <Image source={require('../assets/whitePencil.png')}/>
        </TouchableOpacity> 
    );
};

const styles = StyleSheet.create({

});

export default PencilWhite;