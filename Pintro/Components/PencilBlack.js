import React from 'react';
import { StyleSheet,TouchableOpacity,Image } from 'react-native';

const PencilBlack = props => {

    return(
        <TouchableOpacity>
            <Image source={require('../assets/blackPencil.png')}/>
        </TouchableOpacity> 
    );
    
};

const styles = StyleSheet.create({

});

export default PencilBlack;