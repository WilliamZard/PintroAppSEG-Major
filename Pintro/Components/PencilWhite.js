import React from 'react';
import { StyleSheet,TouchableOpacity,Image,Dimensions } from 'react-native';

const PencilWhite = props => {
    
    return(
        <TouchableOpacity style={styles.imageContainer} onPress={props.onPress}>
            <Image source={require('../assets/whitePencil.png')} style={{height: 20, width: 20}}/>
        </TouchableOpacity> 
    );
};

const styles = StyleSheet.create({
    imageContainer: {
        backgroundColor: null,
        position: 'absolute',
        marginTop: 180,
        marginLeft: Dimensions.get('window').width-30,
    }
});

export default PencilWhite;