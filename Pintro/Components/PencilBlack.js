import React from 'react';
import { StyleSheet,TouchableOpacity,Image } from 'react-native';

const PencilBlack = props => {

    return(
        <TouchableOpacity onPress={props.onPress}>
            <Image source={require('../assets/blackPencil.png')} style={styles.image}/>
        </TouchableOpacity> 
    );
    
};

const styles = StyleSheet.create({
    image: {
        height: 20, 
        width: 20,
        alignSelf: 'flex-end', 
        marginRight: 10
    }
});

export default PencilBlack;