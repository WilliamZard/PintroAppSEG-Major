import React from 'react';
import { StyleSheet, View, Text, Image, ScrollView, TouchableOpacity, FlatList } from 'react-native';
import FollowMe from '../Components/FollowMe.js';
import MsgMe from '../Components/MsgMe.js';
import BlackTag from '../Components/BlackTag.js';
import HelpMeWith from '../Components/HelpMeWith.js';
import Edit from '../Components/Edit.js';
import { fonts } from '../Constants/Fonts.js';
import PencilBlack from '../Components/PencilBlack.js';
import PencilWhite from '../Components/PencilWhite.js';
import Colors from '../Constants/Colors.js';

const BusinessAccountScreen = props => {
    return(
        <ScrollView>
            <View>
                <TouchableOpacity>
                    <Image/>
                </TouchableOpacity>
                <TouchableOpacity>
                    <Image/>
                </TouchableOpacity>
            </View>
            <View>
                <PencilWhite />
                <Image source={require('../assets/blankImage.png')}/>
            </View>
            <View>
                <View>
                    <View>
                        <Text>Connect in Real Life</Text>
                        <Text>Piin App Limited</Text>
                    </View>
                    <PencilBlack />
                </View>
                <View>
                    <FollowMe props={props.FollowMe}>NEW POST</FollowMe>
                    <MsgMe props={props.MsgMe}>EDIT PROFILE</MsgMe>
                    <Edit props={props.Edit}>. . .</Edit>
                </View>
                <View>
                    <TouchableOpacity>
                        <Image source={require('../assets/yellowThumbsUp.png')}/>
                        <Text>SEEKING INVESTMENT</Text>
                    </TouchableOpacity>
                    <TouchableOpacity>
                        <Image source={require('../assets/blackThumbsDown.png')}/>
                        <Text>CURRENTLY HIRING</Text>
                    </TouchableOpacity>
                </View>
                <Text>Our Story</Text>
                <Text style={fonts.story}>
                    Lorem ipsum dolor sit amet, consecteteur adipiscing elit...
                </Text>
                <Text>More</Text>
                <PencilBlack />
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
                <View>
                    <Text>Our journey</Text>
                    <PencilBlack />
                    <Image source={require('../assets/yellowCircle.png')}/><Text>Founded:</Text><Text></Text>
                    <Image source={require('../assets/yellowCircle.png')}/><Text>Location:</Text><Text></Text>
                    <Image source={require('../assets/yellowCircle.png')}/><Text>Company Size:</Text><Text></Text>
                    <Image source={require('../assets/yellowCircle.png')}/><Text>Funding:</Text><Text></Text>
                </View>
                <View>
                    <Text>Team</Text>
                    <PencilBlack />
                    <View>
                        <Image source={require('../assets/blankImage.png')}/>
                        <Image source={require('../assets/blankImage.png')}/>
                        <Image source={require('../assets/blankImage.png')}/>
                        <Image source={require('../assets/blankImage.png')}/>
                        <Image source={require('../assets/blankImage.png')}/>
                    </View>
                </View>
                <View>
                    <Text>Posts</Text>
                    <Text>See all</Text>
                </View>
                <View>
                    <Text>Followers</Text>
                    <Text>See all(45)</Text>
                </View>
            </View>
        </ScrollView>
    );
}

const styles = StyleSheet.create({
    whiteContainer: {
        backgroundColor: Colors.pintroWhite
    }
});

export default BusinessAccountScreen;