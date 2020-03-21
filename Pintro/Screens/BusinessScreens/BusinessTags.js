import React from 'react';
import {
    View,
    Text,
    StyleSheet,
    TextInput,TouchableOpacity,
    ScrollView
} from 'react-native';
import Color from '../../Constants/Colors';

const BusinessTags = props => {
    return(<View style={styles.screen}>
        <View style = {styles.header}>
        <View style = {styles.headerBigText}>
        <Text style={styles.headerText}>Your business tags</Text>
        </View>
        <View style = {styles.headerSmallText}>
        <Text style={styles.smallHeader}>Categorise your business (3 minimum)</Text>
        </View>
        </View>
        <View style={styles.main}>
        <Text>Choose from the full list</Text>
        <TextInput style={styles.inputBox} placeholder="Enter your company name" placeholderTextColor='grey' secureTextEntry={false} />
        <View style={styles.horizintalLineStyle}></View>
        <Text>Or choose from the most popular</Text>
        <TextInput style={styles.inputBox} placeholder="Enter your tagline" placeholderTextColor='grey' secureTextEntry={false} />


        <View style={styles.horizintalLineStyle}></View>
        </View>
        <ScrollView horizontal={true}>
    <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Feminism</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.choosenButton} ><Text style={{color:'white'}}>Coaching</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Mindfulness</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>

 <ScrollView horizontal={true}>
    <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Feminism</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.choosenButton} ><Text style={{color:'white'}}>Coaching</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Mindfulness</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>

 <ScrollView horizontal={true}>
    <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Feminism</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.choosenButton} ><Text style={{color:'white'}}>Coaching</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Mindfulness</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>

 <ScrollView horizontal={true}>
    <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Feminism</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.choosenButton} ><Text style={{color:'white'}}>Coaching</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton} ><Text style={{color:'white'}}>Mindfulness</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Skill Swap</Text></TouchableOpacity> 
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>Diversity</Text></TouchableOpacity>
   <TouchableOpacity style ={styles.tagButton}><Text style={{color:'white'}}>User Experience</Text></TouchableOpacity>
 </ScrollView>
 <View style={{marginHorizontal:30}}>
        <TouchableOpacity style={styles.Button} onPress={() =>props.navigation.navigate({routeName:'DetailsBusiness'})}><Text style={styles.TextButton}>Step 2 of 5</Text></TouchableOpacity>
      </View>
    </View>
    );    
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
        marginBottom:50,
    },TextButton:{
        color:'white'
    },
    tagButton:{
        backgroundColor:'grey',
        padding:10,
        borderRadius:20,
        margin:10,
        color:'black',
        height:45
        },
        choosenButton:{
        backgroundColor:'black',
        borderWidth: 1,
        padding:10,
        borderRadius:20,
        margin:10,
        color:'white',
        height:45
            },


});

export default BusinessTags;