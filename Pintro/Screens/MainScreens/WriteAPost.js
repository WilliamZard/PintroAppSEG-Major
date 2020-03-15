import React, {useState} from 'react';
import {
    View,
    Text,
    Button,
    StyleSheet,
    TextInput,TouchableHighlight
} from 'react-native';
import { useSelector, useDispatch } from 'react-redux';
import * as productsActions from '../../store/actions/timeline';
import TimelinePost from '../../Model/TimelinePost';

const WriteAPost = props => {
const [usedChars,setUsedChars]  = useState(0);
const [postContent,setPostContent] = useState(0);
const dispatch = useDispatch();
    return (
        <View>
            <View style={styles.titleContainer}>
                <View style={styles.BackContainer}><TouchableHighlight onPress={()=>props.onBack()}><Text>Back</Text></TouchableHighlight></View>
            <Text style={styles.title}>
               Danielle Dodoo
            </Text>
            </View>
            <View style={{justifyContent:'center',alignItems:'center',marginTop:50}}>
            <View style={styles.textContainer}>
            <TextInput placeholder='Talk to me about' placeholderTextColor='white' style={{color:'white',margin:20}}
            onChangeText={(word) =>{
                setUsedChars(word.length);
                setPostContent(word);
            }}
            multiline={true}
            blurOnSubmit={true}
            returnKeyType={'done'}
            />
            <View style={{flex: 1,
            justifyContent: 'flex-end',
            alignItems:'flex-end',
            marginBottom: 20, marginHorizontal:10}}><Text style={{color:'white'}}>{usedChars}/300 Characters</Text></View>
            </View>
            <View style={styles.postButtonContainer}>
            <TouchableHighlight onPress={()=>{
                console.log("creating a post");
                
                dispatch(productsActions.uploadPost(postContent));
                props.onBack();
            }} style={styles.buttonLayout} ><Text style={{color:'white'}}>Post</Text></TouchableHighlight>
            </View>
            </View>
        </View>
    );

};


const styles = StyleSheet.create({

    screen:{
        flex:1,
        justifyContent:'center',
        alignItems:'center'
    },
    titleContainer:{
        marginTop:100,
        justifyContent:'center',
        alignItems:'center'
    },title:{
    fontSize:30
    },
    textContainer:{
    height:230,
    width:'90%',
    backgroundColor:'black',
    borderRadius:20,
    },textInput:{

    },tagsSelector:{

    },postButtonContainer:{
        marginTop:40,
        width:'100%',
        alignItems:'center',
        justifyContent:'center'
    },buttonLayout:{
        height:50,
        width:'90%',
        backgroundColor:'black',
        borderRadius:20,
        alignItems:'center',
        justifyContent:'center'
    },BackContainer:{
        width:'90%',
        marginHorizontal:20
    }

});

export default WriteAPost;