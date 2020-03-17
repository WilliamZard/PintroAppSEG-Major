import React, {useState} from 'react';
import { StyleSheet, Text, View, Button, FlatList,TextInput,ScrollView } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import SignInUpButton from '../Components/SignInUpButton';
import InvertedSignInUpButton from '../Components/InvertedSignInUpButton';
import * as Animatable from 'react-native-animatable';
import GoBack from '../Components/GoBack';
import RNPickerSelect from 'react-native-picker-select';

/**
 * Sign Up Screen to allow the user to sign up. The Screen consists of 5 required input fields,
 * 2 buttons, and the Logo. Furthermore the input fields move up if the keyboard hides them.
 * 
 * @param {} props 
 */




const HistoryScreen = props => {
    const [previousCompanies,addPreviousCompany] = useState([]);
    const addSchool = (school) => {
        addPreviousCompany('test');
    }
    
    return (
        <KeyboardAwareScrollView
            style={{ backgroundColor: '#1a1a1a' }}
            resetScrollToCoords={{ x: 0, y: 0 }}
            contentContainerStyle={styles.container}
            scrollEnabled={false}>
            <View style={styles.backGround}>
                <View style={styles.main}>
                    <View style={styles.inputController}>
                        <Animatable.View animation="fadeIn">

                        <Text style={styles.signInText}>Tell us your history</Text>
                        <View style={styles.BottomMargin}>
                        <Text style={styles.aboveInputText}>Your work experience timeline</Text>
                        </View>
                            <Text style={styles.aboveInputText}>Work experience</Text>
                            <TextInput style={styles.inputBox} placeholder="Enter a number of years" placeholderTextColor='white'/>
 <View style={styles.horizintalLineStyle}></View>
                            <Text style={styles.aboveInputText}>Industry</Text>
                            <TextInput style={styles.inputBox} placeholder="Enter your current Industry" placeholderTextColor='white'/>
 <View style={styles.horizintalLineStyle}></View>
 <Text style={styles.aboveInputText}>Current Companies</Text>
                            <TextInput style={styles.inputBox} placeholder="Enter current company name" placeholderTextColor='white'/>
 <View style={styles.horizintalLineStyle}></View>


 <Text style={styles.aboveInputText}>Past Education</Text>
                            <TextInput style={styles.inputBox} placeholder="Enter college name" placeholderTextColor='white'/>
 <View style={styles.horizintalLineStyle}></View>

 <Text style={styles.aboveInputText}>Academic Level</Text>
                           
                            <RNPickerSelect style={{inputIOS: {
		color: 'white',
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
                           
 <InvertedSignInUpButton onPress={()=>   props.navigation.navigate({routeName:'Passions'}) }>STEP 4 OF 6</InvertedSignInUpButton>
                            
                        </Animatable.View>
                    </View>
                </View>
            </View>

        </KeyboardAwareScrollView>
    );
};


const styles = StyleSheet.create({
    backGround: {
        backgroundColor: '#1a1a1a',
        flex: 1
    },
    main: {
        flex: 1,
        alignItems: 'center',
        paddingTop: 20,
        //justifyContent:'center',
        flexDirection: 'column',
        //backgroundColor:'blue'
    },
    inputController: {
        flex: 1,
        paddingTop: 0,
        justifyContent: 'flex-start',
        alignContent: 'center',
        width: '80%'

    },
    textContainer: {
        flexDirection: 'row'
    },
    inputTexts: {
        color: 'black'
    },

    inputBox: {
        height: 40,
        textAlign:'left',
        fontFamily: 'Poppins-Light',
        fontWeight: 'normal',
        color:'white'

    }, signInText: {
        color: 'white',
        fontFamily: 'Poppins-Bold',
        fontSize: 25
    },
    aboveInputText:{
        color:'grey',
        fontFamily:'Poppins-Regular'
    },
    horizintalLineStyle:{
        borderBottomColor: 'white',
         borderBottomWidth: StyleSheet.hairlineWidth,
         marginBottom:30,
         marginTop:10
    },backButton:{
        width:'80%',
        alignContent:'flex-start',
        alignItems:'flex-start',

    },
    BottomMargin:{
        marginBottom:60
    },

    inputBoxFullStory: {
        height: 110,
        alignItems:'flex-start',
        justifyContent:'flex-start',
        textAlign:'left',
        fontFamily: 'Poppins-Light',
        fontWeight: 'normal',
        color:'white',
        textAlignVertical:'top'

    },textInputCentered:{
        alignItems: 'flex-start',
        textAlignVertical: 'top',

    },list:{
        flexGrow:1,
  justifyContent:'flex-end',
    //  alignItems:'center'  
    },listItem:{
        borderColor:'#ccc',
        borderWidth: 1,
        padding:15,
        marginVertical:10,
        backgroundColor:'white',
        flexDirection:'row',
        justifyContent:'space-between',
        width:'100%'
    }
});

export default HistoryScreen;