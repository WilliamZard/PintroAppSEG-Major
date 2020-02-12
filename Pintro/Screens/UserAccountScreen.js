import React from 'react';
import { StyleSheet, Text, View, Button, TextInput, Image, ScrollView } from 'react-native';

/**
 * The account page for a personal account
 *  being viewed by another user consisting 
 * of a view for: there name and profile picture and location,
 * a follow and message me and edit button, there story, what they can help you with
 * what they need help with and there experience
 * @param {*} props
 */
const UserAccountScreen = props => {
    return(
        <ScrollView style={styles.background}>
            <View style={styles.name_title}>
                <Image source={'../images/blank-profile-picture.png'}/>
                <Text>John Doe</Text>
                <Text>Founder of John Doe industries</Text>
                <Text>Upon visualising tig bits I made my glorious snacc company</Text>
            </View>
            <View>
                <View><Button>+ FOLLOW ME</Button></View>
                <View><Image source={'../images/message-icon.png'}/><Button>MESSAGE ME</Button></View>
            </View>
        </ScrollView>
    );
};

const styles = StyleSheet.create({
    background: {
        backgroundColor: Colors.pintroWhite,
        flex: 1
    },
    name_title: {
        flex: 1,
        alignContent: 'left',
    }
});

export default UserAccountScreen;