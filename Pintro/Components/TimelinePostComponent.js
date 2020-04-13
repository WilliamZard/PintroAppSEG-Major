import React from 'react';
import { View,
Text,
StyleSheet,
Image
} from 'react-native';


const TimelinePostComponent = props => {

return(
    <View style = {styles.Box}>

        <View style={{flexDirection:'row'}}>
<View style={{width:40, alignItems:'center',overflow:'hidden',height:40,alignItems: "center", justifyContent: "center",borderRadius:20}}>


<Image
        style={styles.userImage}
        resizeMode="contain"
        source={{
          uri:
            'data:image/png;base64,'+props.photo,
        }}
      />
</View>
<View style={{width:'70%',alignItems:'center',justifyContent:'center',height:40}}>
<Text style={{color:'white'}}>{props.name}</Text>
</View>
        </View>
        <View style={{marginTop:5}}>
    <Text style={{color:'orange'}}></Text>
            <Text style = {{color:'white'}}> {props.content}</Text>
            </View>
    </View>
);

};

const styles = StyleSheet.create({
    Box:{
        flex:0.5,
        backgroundColor:"black",
        width:50,
        padding:10,
        borderRadius:10,
        margin:5
    },
    userImage: {
        height: 50, 
        width: 50, 
        borderRadius: 5
    }
});

export default TimelinePostComponent;


//<Image  resizeMode="contain" source={require('../assets/placeholderFace.png')}/>