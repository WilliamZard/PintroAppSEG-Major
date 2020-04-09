import React,{useState} from 'react';
import {
    View,
    StyleSheet,
    Text,
    TextInput
} from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import { CheckBox } from 'react-native-elements'
import { TouchableOpacity } from 'react-native-gesture-handler';
import SignInUpButton from '../../Components/SignInUpButton';

const LetsGetIntoIt = props => {
const [seekingInvestments,setSeekingInvestments] = useState(false);
const [currentlyHiring,setCurrentlyHiring] = useState(false);
const [companyName,setCompanyName] = useState("");
const [tagLine,setTagLine] = useState("");
const [companyStory,setCompanyStory] = useState("");



return ( 
    <KeyboardAwareScrollView
    style={{ backgroundColor: '#1a1a1a' }}
    resetScrollToCoords={{ x: 0, y: 0 }}
    contentContainerStyle={styles.container}
    scrollEnabled={false}>
<View style={styles.screen}>
    <View style = {styles.header}>
    <View style = {styles.headerBigText}>
    <Text style={styles.headerText}>Let's get into it</Text>
    </View>
    <View style = {styles.headerSmallText}>
    <Text style={styles.smallHeader}>Build your company profile</Text>
    </View>
    </View>
    <View style={styles.main}>
    <Text>Comanpy Name</Text>
    <TextInput 
    style={styles.inputBox}
     placeholder="Enter your company name" 
     placeholderTextColor='grey' 
     secureTextEntry={false} 
     onChangeText={(text)=>setCompanyName(text)}
     />
    <View style={styles.horizintalLineStyle}></View>
    <Text>Tagline</Text>
    <TextInput style={styles.inputBox}
     placeholder="Enter your tagline" 
     placeholderTextColor='grey' 
     secureTextEntry={false} 
     onChangeText={(text)=>setTagLine(text)}
     />
    <View style={styles.horizintalLineStyle}></View>
    <Text>Are you..?</Text>
    <View style={styles.checkBoxes}>
    <CheckBox
  center
  title='Seeking Investments'
  checkedIcon='dot-circle-o'
  uncheckedIcon='circle-o'
  checkedColor='black'
  checked={seekingInvestments}
  containerStyle={{backgroundColor:'white',borderRadius:30,width:150}}
  onPress={()=>setSeekingInvestments(!seekingInvestments)}
/>
<CheckBox
  center
  title='Currently hiring'
  checkedIcon='dot-circle-o'
  uncheckedIcon='circle-o'
  checkedColor='black'
  checked={currentlyHiring}
  containerStyle={{backgroundColor:'white',borderRadius:30,width:150}}
  onPress={()=>setCurrentlyHiring(!currentlyHiring)}
/>
</View>
    <Text>Company Story</Text>
    <TextInput 
    style={styles.inputBoxFullStory}  
    multiline={true} 
    placeholder="Tell is about your company" 
    placeholderTextColor='black'
    returnKeyType={'done'}
    onChangeText={(text)=>setCompanyStory(text)}
    />
    <View style={styles.horizintalLineStyle}></View>
    <TouchableOpacity style={styles.Button} onPress={
  () =>
  props.navigation.navigate({routeName:'BusinessTags', params:{

    seekingInvestmentsToPass:seekingInvestments,
    currentlyHiringToPass:currentlyHiring,
    companyNameToPass:companyName,
    tagLineToPass:tagLine,
    companyStoryToPass:companyStory
  }})


                            }><Text style={styles.TextButton}>Step 1 of 5</Text></TouchableOpacity>
    </View>
</View>

</KeyboardAwareScrollView>)

};

const styles= StyleSheet.create({
    screen:{
        flex:1,
        backgroundColor:'white'
    },header:{
        marginTop:0,
        alignItems:'flex-start',
       
    },headerText:{
        fontSize:35
    },headerBigText:{
        marginHorizontal:30,
        marginBottom:20
    },smallHeader:{
        fontSize:14
    },headerSmallText:{
        marginHorizontal:30
    },
    horizintalLineStyle:{
        borderBottomColor: 'black',
         borderBottomWidth: StyleSheet.hairlineWidth,
         marginBottom:30,
         marginTop:10
    },main:{
        marginHorizontal:30,
        marginTop:50
    },inputBox:{
marginTop:20
    },inputBoxFullStory: {
        height: 110,
        alignItems:'flex-start',
        justifyContent:'flex-start',
        textAlign:'left',
        fontFamily: 'Poppins-Light',
        fontWeight: 'normal',
        color:'black',
        textAlignVertical:'top'

    },checkBoxes:{
        flexDirection:'row',
      marginVertical:30
    },Button:{
        backgroundColor:'black',
        height:40,
        borderRadius:27,
        alignItems:'center',
        justifyContent:'center',
        marginBottom:50
    },TextButton:{
        color:'white'
    }


});

export default LetsGetIntoIt;