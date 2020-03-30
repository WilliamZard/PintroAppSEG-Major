import React from 'react';
import {
    Text,
    View,
    StyleSheet,
    TextInput,
    TouchableOpacity,
} from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'

const EditStory = props => {

    return(
        <KeyboardAwareScrollView
        resetScrollToCoords={{ x: 0, y: 0 }}
        contentContainerStyle={styles.container}
        scrollEnabled={false}>
        <View>
            <View style={{marginHorizontal:30,marginTop:30}}>
                <View style={{marginVertical:20}}>
                    <Text style={{fontSize:30,fontFamily:'Poppins-Bold'}}>Edit your story</Text>
                </View>
            <View style={{marginBottom:30}}>
            <Text>Build your profile</Text>
            </View>
            <Text>Name</Text>
            <TextInput style={{marginVertical:25}} placeholder="Name"/>
            <View style={styles.horizintalLineStyle}></View>
            <Text>Current job title</Text>
            <TextInput style={{marginVertical:25}} placeholder="Job title"/>
            <View style={styles.horizintalLineStyle}></View>
            <Text>Current company</Text>
            <TextInput style={{marginVertical:25}} placeholder="Company"/>
            <View style={styles.horizintalLineStyle}></View>
            <Text>Your Story</Text>
            <TextInput style={{marginVertical:25,     height: 110,
        alignItems:'flex-start',
        justifyContent:'flex-start',
        textAlign:'left',
        fontFamily: 'Poppins-Light',
        fontWeight: 'normal',
        color:'black',
        textAlignVertical:'top'}} multiline={true} placeholder="Story"/>
            <View style={styles.horizintalLineStyle}></View>
                    <View style={{marginTop:20}}> 
                        <TouchableOpacity style={{backgroundColor:'black',height:40,borderRadius:30, alignItems:'center',justifyContent:'center'}}><Text style={{color:'white'}}>Done</Text></TouchableOpacity>
            </View>
               </View>
        </View>
        </KeyboardAwareScrollView>
    );
};



const styles = StyleSheet.create({
    horizintalLineStyle:{
        borderBottomColor: 'black',
         borderBottomWidth: StyleSheet.hairlineWidth,
         marginBottom:10
    }
});


export default EditStory;