import React, { useState, Component } from 'react';
import { StyleSheet, View, Dimensions,Text } from 'react-native';
import MapView, { Marker,PROVIDER_GOOGLE } from 'react-native-maps';
import mapStyle from '../assets/mapStyle';
import * as Permissions from 'expo-permissions';
import * as Location from 'expo-location';
import { Overlay } from 'react-native-elements';

const usersMap = props => {
  const [selectedMarkerIndex,setSelectedMarkerIndex] = useState(0);
  const [userLocation,setUserLocation] = useState();
  const [errorMsg,setErrorMsg] = useState('');
  const [userMarker,setUserMarker] = useState(null);
  const [overlayVisible,setVisible] = useState(false);
  //const markerRef=React.createRef();

  const markerImage = require('../assets/marker.png');
  const selectedMarkerImage = require('../assets/selectedMarker(flip).png');
  const profileMarker = require('../assets/profileMarker.png');
  const userMarkerImage = require('../assets/userMarker.png');
  const selectedUserMarkerImage = require('../assets/selectedUserMarker.png');

  async function getLocation() {
    const { status } = await Permissions.askAsync(Permissions.LOCATION);
    if(status !== 'granted') {
      console.log('PERMISSION NOT GRANTED!');

      setErrorMsg('PERMISSION NOT GRANTED!');
    } else {
      setUserLocation(await Location.getCurrentPositionAsync());

      if(typeof userLocation === 'object'){
        //console.log(userLocation);
        setUserMarker(<Marker coordinate={{latitude: userLocation.coords.latitude,longitude: userLocation.coords.longitude}} image={profileMarker} />);
      }
    }
  };

  const Markers = [

    {
      key:'Bush House',
      title: 'Bush House',
      description: 'Where this dumb app was made',
      latlong: {
        latitude: 51.51263,
        longitude: -0.11721,
      },
      user: 0,
      story: '',
    },
    {
      key:'Waterloo Campus',
      title: 'Waterloo Campus',
      description: 'Where we decided to make this dumb app',
      latlong: {
        latitude: 51.50574,
        longitude: -0.11232,
      },
      user: 0,
      story: '',
    },
    {
      key:'Billiam Bobbert',
      title: 'Billiam Bobbert',
      description: '3rd Year Law Student',
      latlong: {
        latitude: 51.50389,
        longitude: -0.08796,
      },
      user: 1,
      story: '',
      help: 'Memes',
    }
  ];

  const mapMarkers = Markers.map((m,i) => {
    if(m.user === 0) {
      return <Marker
      //ref={markerRef}
      coordinate={m.latlong}
      title={m.title}
      description={m.description}
      key={`marker-${i}`}
      onPress={e => onPressMarker(e, i)}
      image={selectedMarkerIndex === i ? selectedMarkerImage : markerImage}
      />
    } else {
      return <Marker
      //ref={markerRef}
      coordinate={m.latlong}
      title={m.title}
      description={m.description}
      key={`marker-${i}`}
      onPress={e => onPressMarker(e, i)}
      image={selectedMarkerIndex === i ? selectedUserMarkerImage : userMarkerImage}
      />
    }  
  })

  function onPressMarker(e, index){
    setSelectedMarkerIndex(index);
    setVisible(true);
    //markerRef.current.hideCallout();
  }  

  function onPressMap(e) {
    setSelectedMarkerIndex(-1);
    getLocation();
    setVisible(false);
    //console.log(mapMarkers);
  }

  return (
    <View style={styles.container}>
      <MapView
        provider={PROVIDER_GOOGLE} 
        style={styles.mapStyle} 
        initialRegion={{
            latitude: 51.50853,
            longitude: -0.12574,
            latitudeDelta: 0.0922,
            longitudeDelta: 0.0421,
        }} 
        customMapStyle={mapStyle}
        showsCompass={false}
        onPress={e => onPressMap(e)}
      > 
        {mapMarkers}
        {userMarker}
      </MapView>
      <View>
      <Overlay 
        isVisible={overlayVisible}
        onBackdropPress={e => onPressMap(e)}
        width={370}
        height={150}
        borderRadius={20}
        overlayStyle={{position: 'absolute',bottom: 25}}
        windowBackgroundColor={"0"}
      >
         
        <View> 
          <Text>{selectedMarkerIndex === -1 ? null : Markers[selectedMarkerIndex].title}</Text>
          <Text>{selectedMarkerIndex === -1 ? null : Markers[selectedMarkerIndex].description}</Text>
          <Text>{selectedMarkerIndex === -1 ? null :  Markers[selectedMarkerIndex].story}</Text>
          {selectedMarkerIndex === -1 || Markers[selectedMarkerIndex].user === 0 ? null :
            <View>
              <Text>Help me with</Text>
              <Text>{Markers[selectedMarkerIndex].help}</Text>
            </View>}           
        </View>
      </Overlay>
       </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  mapStyle: {
    //...StyleSheet.absoluteFillObject,
    width: Dimensions.get('window').width,
    height: Dimensions.get('window').height,
  }

});

export default usersMap;