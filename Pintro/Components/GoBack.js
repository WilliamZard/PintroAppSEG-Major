import React from 'react';
import {View,Text,StyleSheet,TouchableOpacity} from 'react-native';
import {Ionicons} from '@expo/vector-icons';

const GoBack = props => {
    return(

        <TouchableOpacity onPress={props.onPress} activeOpacity={0.6}>
            <View style={styles.container}>
    <Ionicons  name="md-arrow-round-back" size = {24} color ="white"/> 
            </View>
        </TouchableOpacity>
    );
};

const styles = StyleSheet.create({
   container:{
       paddingTop:10,
       alignItems:'center',
 

   }

    
});
export default GoBack;