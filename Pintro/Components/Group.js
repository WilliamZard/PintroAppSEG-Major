import React from 'react';
import {View,Text,StyleSheet,TouchableOpacity, Group} from 'react-native';
import Colors from '../Constants/Colors';
import { fonts } from '../Constants/Fonts';

const Group = props => {
    return(

        <TouchableOpacity style={styles.tag} onPress={props.onPress} activeOpacity={0.6}>
                <Text style={fonts.title_black}>Group Name {this.props.name}</Text>
                <Text style={fonts.bio}>{this.props.members} members</Text>
        </TouchableOpacity> 

    );
};

const styles = StyleSheet.create({
    tag: {
        borderColor: Colors.pintroBlack,
        color: Colors.pintroWhite,
        borderWidth:0.5,
        width:'15%',
        paddingVertical:12,
        paddingHorizontal:30,
        borderRadius:20,
        marginRight:10,
        marginTop:15,
        marginBottom:10
    },
    tag_text: {
        color: Colors.pintroBlack,
        textAlign: 'center',
        fontFamily:'Poppins-Light',
        fontSize: 10
    }
});

export default Group;