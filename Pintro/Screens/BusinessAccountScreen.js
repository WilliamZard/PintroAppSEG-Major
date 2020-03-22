import React from 'react';
import { StyleSheet, View, Text, Image, ScrollView, TouchableOpacity } from 'react-native';
import FollowMe from '../Components/FollowMe.js';
import MsgMe from '../Components/MsgMe.js';
import BlackTag from '../Components/BlackTag.js';
import HelpMeWith from '../Components/HelpMeWith.js';
import Edit from '../Components/Edit.js';
import { fonts } from '../Constants/Fonts.js';
import Colors from '../Constants/Colors.js';

const BusinessAccountScreen = props => {
    return(
        <View>
            <View>
                <TouchableOpacity>
                    <Image/>
                </TouchableOpacity>
                <TouchableOpacity>
                    <Image/>
                </TouchableOpacity>
            </View>
            <View>
                <Image />
            </View>
            <View>
                <View>
                    <View>
                        <Text>Connect in Real Life</Text>
                        <Text>Piin App Limited</Text>
                    </View>
                    <TouchableOpacity>
                        <Image/>
                    </TouchableOpacity>
                </View>
                <View>
                    <FollowMe props={props.FollowMe}>+ FOLLOW ME</FollowMe>
                    <MsgMe props={props.MsgMe}>MESSAGE US</MsgMe>
                    <Edit props={props.Edit}>. . .</Edit>
                </View>
                <Text>Our Story</Text>
                <Text style={fonts.story}>
                    Lorem ipsum dolor sit amet, consecteteur adipiscing elit...
                </Text>
                <Text>More</Text>
                <View>
                    <BlackTag props={props.BlackTag}>START-UP</BlackTag>
                    <BlackTag props={props.BlackTag}>PRE-SEED</BlackTag>
                    <BlackTag props={props.BlackTag}>NETWORKING</BlackTag>
                    <BlackTag props={props.BlackTag}>ENTREPRENEUR</BlackTag>
                    <BlackTag props={props.BlackTag}>APP</BlackTag>
                    <BlackTag props={props.BlackTag}>CO-WORKING</BlackTag>
                </View>
                <ScrollView>
                    <HelpMeWith props={props.HelpMeWith}>Business Modelling</HelpMeWith>
                    <HelpMeWith props={props.HelpMeWith}>Crepe Investments</HelpMeWith>
                    <HelpMeWith props={props.HelpMeWith}>Home Workouts</HelpMeWith>
                </ScrollView>
            </View>
        </View>
    );
};

const styles = StyleSheet.create({

});

export default BusinessAccountScreen;