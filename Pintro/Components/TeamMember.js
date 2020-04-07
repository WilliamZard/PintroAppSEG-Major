import React from 'react';
import { TouchableOpacity,StyleSheet,View,Text,Image } from 'react-native';
import { fonts } from '../Constants/Fonts';
import Colors from '../Constants/Colors';

const TeamMember = props => {

    function handleRemoval() {
        props.callback(props.userObj);
    }

    return(
        <TouchableOpacity>
            <View style={styles.teamContainer}>
                <Image source={require('../assets/blankImage.png')} style={styles.circleImage}/>
                <View style={styles.textContainer}>
                    <Text style={fonts.title_black}>{props.userObj.full_name}</Text>
                    <Text style={fonts.story}>{props.userObj.job_title}</Text>
                </View>
                <TouchableOpacity onPress={() => handleRemoval()}>
                    <Image source={require('../assets/cross.png')} style={styles.cross}/>
                </TouchableOpacity>
            </View>
        </TouchableOpacity>
    )
}

const styles = StyleSheet.create({
    teamContainer: {
        flexDirection: 'row',
        backgroundColor: 'white',
        marginBottom: 10,
        borderRadius: 20,
        width: 370,
        height: 75,
    },
    circleImage: {
        width: 40,
        height: 40,
        borderRadius: 20,
        marginBottom: 10,
        marginTop: 17,
        marginHorizontal: 10,
    },
    textContainer: {
        marginTop: 18,
        flex: 1
    },
    cross: {
        height: 20, 
        width: 20, 
        marginTop: 30, 
        marginRight: 20
    }
})

export default TeamMember;