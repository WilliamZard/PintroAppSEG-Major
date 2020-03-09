import React from 'react';
import {
View,
Text,
StyleSheet,
TouchableOpacity
} from 'react-native';

import Colors from '../../Constants/Colors';
const MapScreen = props => {

return (
    <View style={styles.background}>
    <View style={styles.header}>
            <Text style={styles.pintroText}>pintro<Text style={styles.yellowAccent}>.</Text></Text>
            <View style={{flexDirection:'row',marginTop:5}}>
                <View style={{width:'50%',alignItems:'center',borderColor:'orange',borderBottomWidth:4}}><TouchableOpacity style={{height:40}} ><Text>Map</Text></TouchableOpacity></View>
                <View style={{width:'50%',alignItems:'center'}}><TouchableOpacity style={{height:40}} onPress={
                   ()=> props.navigation.navigate({routeName:'Feed'})
                }><Text>Feed</Text></TouchableOpacity></View>
            </View>
            
    </View>
    </View>

);

};

const styles = StyleSheet.create({
    backGround: {
        flex:1,
  
    },
    body: {
        //backgroundColor: Colors.pintroWhite,

        paddingBottom: 1000,
        //flex: 1
    },
    searchView: {
        //backgroundColor: Colors.pintroWhite,

        paddingBottom: 90,
        //flex: 1
    },
    header: {
        alignItems: 'center',
        justifyContent: 'center',
        flexDirection: 'column',
        marginTop:30,
        paddingBottom: 0
    },
    pintroText: {
        color: 'black',
        //fontFamily: 'Poppins-Bold',
        fontSize: 40
    },
    yellowAccent: {
        color: Colors.pintroYellow,
        fontSize: 40
    },
    buttonContainer: {
        paddingTop: 20,
        width: '70%',
        fontFamily:'Poppins-Regular'
    },
    textContainer: {
        flexDirection: 'row',
        alignItems: 'center',
        paddingTop: 100
    },
    touchableText: {
        textAlign: 'left',
        color: 'black',
        fontFamily: 'Poppins-Regular',
        fontSize: 10,
        paddingBottom: 0
    },
    touchableContainer: {
        paddingBottom: 0,
        textAlign: 'left',
        flexDirection: 'row',
        justifyContent: 'space-around'
    },
    messageText : {
        color: 'white',
        fontFamily: 'Poppins-Bold',
        textAlign: 'center',
        paddingBottom: 100,
        fontSize: 30
    }

});

export default MapScreen;