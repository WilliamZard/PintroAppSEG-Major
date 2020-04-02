import React from 'react';
import {
    Text,
    View,
    StyleSheet,
    TextInput,
    TouchableOpacity,
    Button,

} from 'react-native';
import Colors from '../../Constants/Colors';
import InvertedSignInUpButton from '../../Components/InvertedSignInUpButton';


const EditPhoto = props => {

    return (
 
            <View style={styles.backGround}>
                <View style={styles.main}>

                    <View style={styles.inputController}>
                       

                        <Text style={styles.signInText}>Edit your photo</Text>
                        <View style={styles.BottomMargin}>
                        <Text style={styles.aboveInputText}>Upload a profile photo</Text>
                        </View>
                        
                    </View>
                    <View style={styles.camera}>
                    <TouchableOpacity style={{
       borderWidth:1,
       borderColor:'white',
       alignItems:'center',
       justifyContent:'center',
       width:280,
       height:280,
       backgroundColor:'black',
       borderRadius:190,
     }}><Text style={{color:'white',fontSize:60,fontFamily:'Poppins-Thin'}}>+</Text></TouchableOpacity>
                    </View>
                     
                </View>
                <View style={styles.bottomButton}>
                <InvertedSignInUpButton onPress={
  () =>
  props.navigation.navigate({routeName:'Account'})


                            }>Done</InvertedSignInUpButton>
            </View>
            </View>
 
    );
};


const styles = StyleSheet.create({
    backGround: {
        backgroundColor: 'white',
        flex: 1
    },
    main: {
        flex: 1,
        alignItems: 'center',
        paddingTop: 10,
        //justifyContent:'center',
        flexDirection: 'column',
        //backgroundColor:'blue'
    },
    inputController: {
        flex: 1,
        paddingTop: 0,
        justifyContent: 'flex-start',
        alignContent: 'center',
        width: '80%',
//        backgroundColor:'green'

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
        fontWeight: 'normal'

    }, signInText: {
        color: 'black',
        fontFamily: 'Poppins-Bold',
        fontSize: 25
    },
    aboveInputText:{
        color:'grey',
        fontFamily:'Poppins-Regular'
    },
    BottomMargin:{
        marginBottom:60
    },
    bottomButton:{
    marginBottom:30
    },camera:{
flex:1,
marginBottom:100
    }
});

export default EditPhoto;