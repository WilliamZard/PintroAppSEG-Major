import React from 'react';
import { StyleSheet, View, Text, TouchableOpacity, Image, ScrollView } from 'react-native';
import { SearchBar } from 'react-native-elements';
import { fonts } from '../Constants/Fonts.js';

const SearchPage = () => {

    return(
        <View style={styles.blackContainer}>
            <View>
                <Text style={fonts.name_white}>Browse</Text>
                <Text style={fonts.tag_button_white}>Be inspired!</Text>
                <SearchBar
                    platform="default"
                    placeholder="Type keyword,tag or location"
                    placeholderTextColor='black'
                    round={true}
                    searchIcon={false}
                    lightTheme={true}
                    containerStyle={{backgroundColor: 'white',width: 345,borderRadius:20}}
                    inputContainerStyle={{backgroundColor: 'white',width: 330}}/>
                <Text style={fonts.tag_button_white}>or Choose a Category</Text>
            </View>
            <View>
                <TouchableOpacity>
                    <Image></Image>
                    <Text style={fonts.tag_button_white}>PEOPLE</Text>
                </TouchableOpacity>
                <TouchableOpacity>
                    <Image></Image>
                    <Text style={fonts.tag_button_white}>COMPANIES</Text>
                </TouchableOpacity>
                <TouchableOpacity>
                    <Image></Image>
                    <Text style={fonts.tag_button_white}>CONTENT</Text>
                </TouchableOpacity>
                <TouchableOpacity>
                    <Image></Image>
                    <Text style={fonts.tag_button_white}>COMMUNITIES</Text>
                </TouchableOpacity>
                <TouchableOpacity>
                    <Image></Image>
                    <Text style={fonts.tag_button_white}>SPACES</Text>
                </TouchableOpacity>
                <ScrollView style={styles.whiteContainer}>
                    <Text>Closest to you</Text>
                    <Text style={fonts.tag_button_white}>See all</Text>
                </ScrollView>
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    blackContainer: {
        flex: 1,
        backgroundColor: 'black',
    },
    whiteContainer: {
        flex: 1,
        backgroundColor: 'white',
    }
});

export default SearchPage;