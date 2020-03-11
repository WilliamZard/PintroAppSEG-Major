import React from 'react';
import { StyleSheet, View, Text, TouchableOpacity, Image, ScrollView } from 'react-native';
import { SearchBar } from 'react-native-elements';
import { fonts } from '../Constants/Fonts.js';
import Colors  from '../Constants/Colors.js';

const SearchPage = () => {

    return(
        <View style={styles.blackContainer}>
            <View style={styles.topContainer}>
                <Text style={styles.browse}>Browse</Text>
                <Text style={styles.inspire}>Be inspired!</Text>
                <SearchBar
                    platform="default"
                    placeholder="Type keyword,tag or location"
                    placeholderTextColor='black'
                    round={true}
                    searchIcon={false}
                    lightTheme={true}
                    containerStyle={{backgroundColor: 'white',width: 345,borderRadius:30}}
                    inputContainerStyle={{backgroundColor: 'white',width: 330}}/>
                <Text style={styles.category}>or Choose a Category</Text>
            </View>
            <View style={styles.rowContainer}>
                <TouchableOpacity style={styles.imageContainer}>
                    <Image source={require('../assets/blankImage.png')} style={styles.circleImage}/>
                    <Text style={fonts.tag_button_white}>PEOPLE</Text>
                </TouchableOpacity>
                <TouchableOpacity style={styles.imageContainer}>
                    <Image source={require('../assets/blankImage.png')} style={styles.circleImage}/>
                    <Text style={fonts.tag_button_white}>COMPANIES</Text>
                </TouchableOpacity>
                <TouchableOpacity style={styles.imageContainer}>
                    <Image source={require('../assets/blankImage.png')} style={styles.circleImage}/>
                    <Text style={fonts.tag_button_white}>CONTENT</Text>
                </TouchableOpacity>
                <TouchableOpacity style={styles.imageContainer}>
                    <Image source={require('../assets/blankImage.png')} style={styles.circleImage}/>
                    <Text style={fonts.tag_button_white}>COMMUNITIES</Text>
                </TouchableOpacity>
                <TouchableOpacity style={styles.imageContainer}>
                    <Image source={require('../assets/blankImage.png')} style={styles.circleImage}/>
                    <Text style={fonts.tag_button_white}>SPACES</Text>
                </TouchableOpacity>
            </View>
            <ScrollView style={styles.whiteContainer}>
                <View style={styles.textContainer}>
                    <Text style={styles.spaces}>Spaces</Text>
                </View>
                <View style={styles.textRow}>
                    <Text style={styles.closest}>Closest to you</Text>
                    <Text style={styles.seeAll}>See all</Text>
                </View>
            </ScrollView>
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
    },
    circleImage: {
        width: 50,
        height: 50,
        borderRadius: 24,
        marginBottom: 10,
    },
    rowContainer: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center',
        marginBottom: 40,
    },
    imageContainer: {
        paddingRight: 5,
        alignItems: 'center',
        justifyContent: 'center',
    },
    topContainer: {
        alignItems: 'center',
        justifyContent: 'center',
        marginTop: 80,
    },
    browse: {
        color: Colors.pintroWhite,
        fontFamily: 'Poppins-Bold',
        fontSize: 32,
        marginBottom: 20,
    },
    inspire: {
        color: Colors.pintroWhite,
        fontFamily: 'Poppins-Light',
        fontSize: 10,
        marginBottom: 25,
    },
    category: {
        color: Colors.pintroWhite,
        fontFamily: 'Poppins-Light',
        fontSize: 10,
        marginTop: 40,
        marginBottom: 10,
    },
    spaces: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        fontSize: 16,
        marginBottom: 15,
        marginTop: 30,
    },
    textRow: {
        flexDirection: 'row',
    },
    textContainer: {
        alignItems: 'center',
        justifyContent: 'center',
    },
    closest: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        fontSize: 12,
        marginLeft: 10,
    },
    seeAll: {
        color: 'grey',
        fontFamily: 'Poppins-Bold',
        fontSize: 10,
        marginLeft: 250,
    }
});

export default SearchPage;