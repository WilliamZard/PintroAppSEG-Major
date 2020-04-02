import React from 'react';
import {
    Text,
    View,
    StyleSheet,
    TextInput,
    TouchableOpacity,
} from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import RNPickerSelect from 'react-native-picker-select';
const EditExperience = props => {

    return(
        <KeyboardAwareScrollView
        resetScrollToCoords={{ x: 0, y: 0 }}
        contentContainerStyle={styles.container}
        scrollEnabled={false}>
        <View>
            <View style={{marginHorizontal:30,marginTop:30}}>
                <View style={{marginVertical:20}}>
                    <Text style={{fontSize:30,fontFamily:'Poppins-Bold'}}>Edit your experience</Text>
                </View>
            <View style={{marginBottom:30}}>
            <Text>Your work experience timeline</Text>
            </View>
            <Text>Work experience</Text>
            <TextInput style={{marginVertical:25}} placeholder="69 years"/>
            <View style={styles.horizintalLineStyle}></View>
            <Text>Industry</Text>
            <TextInput style={{marginVertical:25}} placeholder="industry"/>
            <View style={styles.horizintalLineStyle}></View>
            <Text>Previous company</Text>
            <TextInput style={{marginVertical:25}} placeholder="company"/>
            <View style={styles.horizintalLineStyle}></View>
            <Text>Education</Text>
            <TextInput style={{marginVertical:25}} placeholder="education"/>
            <View style={styles.horizintalLineStyle}></View>
            <Text>Academic Level</Text>
            <RNPickerSelect style={{inputIOS: {
		color: 'black',
		paddingTop: 13,
		paddingHorizontal: 10,
		paddingBottom: 12,
	}}}
            onValueChange={(value) => console.log(value)}
            items={[
                { label: 'PHD', value: 'PHD',},
                { label: 'Master', value: 'Master' },
                { label: 'Bachelor', value: 'Bachelor' },
                { label: 'A-Levels', value: 'Levels' },
            ]}
        />
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


export default EditExperience;