import React from 'react';
import {
    View,
    Text,
    TouchableOpacity,
    StyleSheet
} from 'react-native';

const SettingsButton = props =>{
    return(
        <View style={styles.container}>
            <TouchableOpacity  onPress={props.onPress} style={styles.button}><Text>{props.title}</Text></TouchableOpacity>
        </View>
    )
};

const styles = StyleSheet.create({
button:{
width:'100%',
height:'100%',
alignItems:'flex-start',


},
container:{

    justifyContent:'center',
    alignItems:'flex-start',
    height:40,
    paddingHorizontal:30
}
});

export default SettingsButton;