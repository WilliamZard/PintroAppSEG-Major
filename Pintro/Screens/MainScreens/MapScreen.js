import React, { useState } from 'react';
import {
View,
Text,
StyleSheet,
TouchableOpacity
} from 'react-native';
import MapView from 'react-native-maps';
import { SearchBar } from 'react-native-elements';
import UsersMap from '../../Components/UsersMap';
import Colors from '../../Constants/Colors';
const MapScreen = props => {
    const [searchKeyword,setSearchKeyword] = useState();
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
            

            <View style={styles.container}>
            <UsersMap />
            <SearchBar
                platform="default"
                placeholder="Enter a location..."
                placeholderTextColor='black'
                round={true}
                searchIcon={false}
                lightTheme={true}
                containerStyle={{backgroundColor: 'white',width: 345,borderRadius:20,position: 'absolute',top:-60}}
                inputContainerStyle={{backgroundColor: 'white',width: 330}}
                onChangeText={searchWord => setSearchKeyword(searchWord)}
                value={searchKeyword}
            />
      
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
        marginTop:100,
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
    container: {
        marginTop:90,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
      }

});

export default MapScreen;