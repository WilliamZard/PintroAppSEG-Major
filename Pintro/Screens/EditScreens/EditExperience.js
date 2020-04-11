import React,{useState} from 'react';
import {
    Text,
    View,
    StyleSheet,
    TextInput,
    TouchableOpacity,
} from 'react-native';
import {useSelector, useDispatch} from 'react-redux';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import RNPickerSelect from 'react-native-picker-select';
import * as UserActions from '../../store/actions/user';
const EditExperience = props => {

    const dispatch = useDispatch();
    const [workExperience,setWorkExperience] = useState(useSelector(state => state.user.years_in_industry));
    const [industry,setIndustry] = useState(useSelector(state => state.user.Industry));
    const [previousCompany,setPreviousCompany] = useState(useSelector(state => state.user.previous_Company));
    const [education,setEducation] = useState(useSelector(state => state.user.education));
    const [academicLevel,setAcademicLevel] = useState(useSelector(state => state.user.academic_Level));
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
            <TextInput 
            style={{marginVertical:25}} 
            value={workExperience}
            onChangeText={(text)=>setWorkExperience(text)}
            />
            <View style={styles.horizintalLineStyle}></View>
            <Text>Industry</Text>
            <TextInput 
            style={{marginVertical:25}} 
            value={industry}
            onChangeText={(text)=>setIndustry(text)}
            />
            <View style={styles.horizintalLineStyle}></View>
            <Text>Previous company</Text>
            <TextInput
             style={{marginVertical:25}} 
            value={previousCompany}
            onChangeText={(text)=>setPreviousCompany(text)}
             />
            <View style={styles.horizintalLineStyle}></View>
            <Text>Education</Text>
            <TextInput
             style={{marginVertical:25}}
              value={education}
              onChangeText={(text)=>setEducation(text)}
              />
            <View style={styles.horizintalLineStyle}></View>
            <Text>Academic Level</Text>
            <RNPickerSelect style={{inputIOS: {
		color: 'black',
		paddingTop: 13,
		paddingHorizontal: 10,
		paddingBottom: 12,
    }}}
    value={academicLevel}
            onValueChange={(value) => setAcademicLevel(value)}
            items={[
                { label: 'PHD', value: 'PHD',},
                { label: 'Master', value: 'Master' },
                { label: 'Bachelor', value: 'Bachelor' },
                { label: 'A-Levels', value: 'Levels' },
            ]}
        />
            <View style={styles.horizintalLineStyle}></View>
                    <View style={{marginTop:20}}> 
                        <TouchableOpacity
                         style={{backgroundColor:'black',height:40,borderRadius:30, alignItems:'center',justifyContent:'center'}}
                         onPress={()=>{
                            dispatch(UserActions.update_experience(workExperience,industry,previousCompany,education,academicLevel))
                            props.navigation.navigate({routeName:'SettingsPage'})
                         }}
                         ><Text style={{color:'white'}}>Done</Text></TouchableOpacity>
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