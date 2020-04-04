import React from 'react';
import {
    View,
    Text,
    StyleSheet,
    TouchableWithoutFeedback,
    ScrollView
} from 'react-native';

import {useDispatch} from 'react-redux';

import SettingsButton from '../Components/SettingsButton';
import * as authActions from '../store/actions/auth';
const Settings = props => {
const dispatch = useDispatch();
return(

<View > 
    <ScrollView>
<View style={{marginTop:100,marginHorizontal:30}}>
   
           <Text style={{fontSize:10}}>Personal</Text>
       </View>
       <SettingsButton 
       onPress={()=>    props.navigation.navigate({routeName:'StoryPage'})}
       title="Edit Story"/>
       <View style={styles.horizintalLineStyle}></View>
       <SettingsButton 
       onPress={()=>    props.navigation.navigate({routeName:'ExperiencePage'})}
       title="Edit History"/>
       <View style={styles.horizintalLineStyle}></View>
       <SettingsButton 
       onPress={()=>    props.navigation.navigate({routeName:'PhotoPage'})}
       title="Edit Picture"/>
       <View style={styles.horizintalLineStyle}></View>
       <SettingsButton 
       onPress={()=>    props.navigation.navigate({routeName:'PassionsPage'})}
       title="Edit Passions"/>
       <View style={styles.horizintalLineStyle}></View>
       <SettingsButton 
       onPress={()=>    props.navigation.navigate({routeName:'HelpOthersPage'})}
       title="Edit Skills"/>
       <View style={styles.horizintalLineStyle}></View>
       
       <SettingsButton title="Push notifiations"/>
       <View style={styles.horizintalLineStyle}></View>
       <SettingsButton title="Set nearby distance"/>
       <View style={styles.horizintalLineStyle}></View>
       <SettingsButton title="Edit communities"/>
       <View style={styles.horizintalLineStyle}></View>
       <View style={{marginTop:20,marginHorizontal:30}}>
           <Text style={{fontSize:10}}>About</Text>
       </View>
       <SettingsButton title="Terms of use"/>
       <View style={styles.horizintalLineStyle}></View>
       <SettingsButton title="Privacy policy"/>
       <View style={styles.horizintalLineStyle}></View>
       <SettingsButton title="FAQ & contact us"/>
       <View style={styles.horizintalLineStyle}></View>
       <View style={{marginTop:20,marginHorizontal:30}}>
           <Text style={{fontSize:10}}>Account</Text>
       </View>
       <SettingsButton title="Update password"/>
       <View style={styles.horizintalLineStyle}></View>
       <SettingsButton title="Update email"/>
       <View style={styles.horizintalLineStyle}></View>
       <SettingsButton title="Update phone number"/>
       <View style={styles.horizintalLineStyle}></View>
       <SettingsButton onPress={()=> 
       {dispatch(authActions.logout())
        props.navigation.navigate({routeName:'routeOne'})}} title="Log out"/>
       <View style={styles.horizintalLineStyle}></View>
       <SettingsButton title="Delete my account"/>
     
       <View style={styles.horizintalLineStyle}></View>
    
       </ScrollView>
</View>)

};
const styles = StyleSheet.create({
screen:{
flex:1
},
horizintalLineStyle:{
        borderBottomColor: 'grey',
         borderBottomWidth: StyleSheet.hairlineWidth,
         marginBottom:10
}});

export default Settings;