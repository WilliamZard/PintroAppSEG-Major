import React from 'react';
import { StyleSheet, Text, View, Button, Image, ScrollView } from 'react-native';
import { fonts } from '../Constants/Fonts.js';
import BlackTag from '../Components/BlackTag.js';
import WhiteTag from '../Components/WhiteTag.js';
import Colors from '../Constants/Colors';
import FollowMe from '../Components/FollowMe.js';
import MsgMe from '../Components/MsgMe.js';
import Edit from '../Components/Edit.js';

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
                <Image source={require('../images/blank-profile-picture.png')} style={{ width: 60, height: 60}}/>
                <Text style={fonts.name_black}>John Doe</Text>
                <Text style={fonts.title_black}>Founder of John Doe industries</Text>
                <Text style={fonts.bio}>"Upon visualising tig bits I made my glorious snacc company"</Text>
                <Text style={fonts.location}>King's College London</Text>
            </View>
            <View style={styles.rowContainer}>
                <FollowMe props={props.FollowMe}>+ FOLLOW ME</FollowMe>
                <MsgMe props={props.MsgMe}>MESSAGE ME</MsgMe>
                <Edit props={props.Edit}>. . .</Edit>
            </View>
            <View>
                <ScrollView>
                    <View style={styles.name_title}>
                        <Button>
                            <Text style={fonts.title_black}>Help me with</Text>
                            <Text style={fonts.story}>interdimensional travel</Text>
                        </Button>
                        <Image source={require('../images/message-icon.png')}/>
                    </View>
                    <View>
                        <Button>
                            <Text style={fonts.title_black}>Help me with</Text>
                            <Text style={fonts.story}>find the szechuan sauce</Text>
                        </Button>
                        <Image source={require('../images/message-icon.png')}/>
                    </View>
                    <View>
                        <Button>
                            <Text style={fonts.title_black}>Help me with</Text>
                            <Text style={fonts.story}>Heists</Text>
                        </Button>
                        <Image source={require('../images/message-icon.png')}/>
                    </View>
                </ScrollView>
            </View>
            <View>
                <Text style={fonts.title_black}>My Story</Text>
                <Text style={fonts.story}>
                Some really really really long text in latin that 
                sounds really fancy.
                </Text>
                <Text style={fonts.more_yellow}>More</Text>
            </View>
            <View>
                <Text style={fonts.title_black}>Talk to me about</Text>
                <View>
                    <BlackTag>Rick and Morty</BlackTag>
                    <BlackTag>Comedy</BlackTag>
                    <BlackTag>Memes</BlackTag>
                </View>
            </View>
            <View>
                <Text style={fonts.title_black}>Help me with</Text>
                <View>
                    <WhiteTag>Cooking</WhiteTag>
                    <WhiteTag>2 shots off my golf game</WhiteTag>
                    <WhiteTag>Oooweee</WhiteTag>
                </View>
            </View> 
            <View>
                <Text style={fonts.title_black}>Experience</Text>
                <View>
                    <Text style={fonts.title_black}>Work Experience:</Text><Text style={fonts.story}>DC</Text>
                    <Text style={fonts.title_black}>Industry:</Text><Text style={fonts.story}>Sending VKs</Text>
                </View>
            </View>
            <View>
                <Text style={fonts.title_black}>Groups</Text><Text style={fonts.more_white}>See all</Text>
                <View style={styles.name_title}>
                    <Image source={require('../images/blank-profile-picture.png')} />
                    <Text style={fonts.title_black}>Group 1</Text>
                    <Text style={fonts.story}>69 members</Text>
                </View>
                <View style={styles.name_title}>
                    <Image source={require('../images/blank-profile-picture.png')} />
                    <Text style={fonts.title_black}>Group 2</Text>
                    <Text style={fonts.story}>42 members</Text>
                </View>
            </View>
            <View>
                <Text style={fonts.title_black}>Community</Text><Text style={fonts.more_white}>See all</Text>
                <View>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 30, width: 30}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 30, width: 30}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 30, width: 30}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 30, width: 30}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 30, width: 30}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 30, width: 30}}/></Button>
                </View>
            </View>
            <View>
                <Text style={fonts.name_title}>Recommendations</Text>
                <View>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 70, width: 70}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 70, width: 70}}/></Button>
                    <Button><Image source={require('../images/blank-profile-picture.png')} style={{ width: 70, width: 70}}/></Button>
                </View>
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
    },
    helpUs_button: {
        color: Colors.pintroWhite
    },
    rowContainer: {
        flexDirection: 'row'
    }
});

export default UserAccountScreen;