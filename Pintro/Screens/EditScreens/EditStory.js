import React,{useState} from 'react';
import {useSelector, useDispatch} from 'react-redux';
import {
    Text,
    View,
    StyleSheet,
    TextInput,
    TouchableOpacity,
} from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import * as userActions from '../../store/actions/user';
const EditStory = props => {
const dispatch = useDispatch();

const [name,setName]=useState(useSelector(state => state.user.full_name));
const [jobTitle,setJobTitle]=useState(useSelector(state => state.user.job_title));
const [currentCompany,setCurrentCompany]=useState(useSelector(state => state.user.current_Company));
const [story,setStory]=useState(useSelector(state => state.user.story));


const doneHandler = async () => {
    console.log(name,jobTitle,currentCompany,story);
    await dispatch(userActions.update_story(name,jobTitle,currentCompany,story))
    props.navigation.navigate({routeName:'SettingsPage'})
}
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
            <TextInput
             style={{marginVertical:25}}
              value={name}
              onChangeText={(text)=>setName(text)}
              />
            <View style={styles.horizintalLineStyle}></View>
            <Text>Current job title</Text>
            <TextInput 
            style={{marginVertical:25}} 
            value={jobTitle}
            onChangeText={(text)=>setJobTitle(text)}
            />
            <View style={styles.horizintalLineStyle}></View>
            <Text>Current company</Text>
            <TextInput 
            style={{marginVertical:25}} 
        
            value={currentCompany}
            onChangeText={(text)=>setCurrentCompany(text)}
            />
            <View style={styles.horizintalLineStyle}></View>
            <Text>Your Story</Text>
            <TextInput style={{marginVertical:0,     height: 60,
        alignItems:'flex-start',
        justifyContent:'flex-start',
        textAlign:'left',
        fontFamily: 'Poppins-Light',
        fontWeight: 'normal',
        color:'black',
        textAlignVertical:'top'}} 
        multiline={true} 
    
        value={story}
        onChangeText={(text)=>setStory(text)}
        />
            <View style={styles.horizintalLineStyle}></View>
                    <View style={{marginTop:20}}> 
                        <TouchableOpacity onPress={()=>{
                            doneHandler()
                        }
                            } style={{backgroundColor:'black',height:40,borderRadius:30, alignItems:'center',justifyContent:'center'}}><Text style={{color:'white'}}>Done</Text></TouchableOpacity>
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