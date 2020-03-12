import React, { useState } from 'react';
import { StyleSheet, View } from 'react-native';
import { SearchBar } from 'react-native-elements';
import UsersMap from '../../Components/UsersMap';

const MapScreen = props => {
    const [searchKeyword,setSearchKeyword] = useState();

    return(
        <View style={styles.container}>
            <UsersMap />
            <SearchBar
                platform="default"
                placeholder="Enter a location..."
                placeholderTextColor='black'
                round={true}
                searchIcon={false}
                lightTheme={true}
                containerStyle={{backgroundColor: 'white',width: 345,borderRadius:20,position: 'absolute',top:25}}
                inputContainerStyle={{backgroundColor: 'white',width: 330}}
                onChangeText={searchWord => setSearchKeyword(searchWord)}
                value={searchKeyword}
            />
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    }
  });

  export default MapScreen;