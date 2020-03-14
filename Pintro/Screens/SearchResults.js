import React, { useState } from 'react';
import { StyleSheet, View, TouchableOpacity, Image, Text, ScrollView } from 'react-native';
import { SearchBar } from 'react-native-elements';
import { fonts } from '../Constants/Fonts.js';
import Colors from '../Constants/Colors.js';
import Company from '../Components/Company.js';
import Group from '../Components/Groups.js';

const SearchResults = props => {
    const [searchKeyword,setSearchKeyword] = useState();
    
    return (
        <View style={styles.pageContainer}>
            <ScrollView style={styles.scrollContainer}>
                <View style={styles.topContainer}>
                    <Text style={styles.results}>Results (87)</Text>
                    <Text style={styles.found}>Found what you're looking for?</Text>
                    <SearchBar 
                        platform="default"
                        placeholder="Type keyword,tag or location"
                        placeholderTextColor='grey'
                        round={true}
                        searchIcon={false}
                        lightTheme={true}
                        inputStyle={styles.searchText}
                        containerStyle={{backgroundColor: 'white',width: 345,borderRadius:30}}
                        inputContainerStyle={{backgroundColor: 'white',width: 330}}
                        onChangeText={searchWord => setSearchKeyword(searchWord)}
                        value={searchKeyword}/>
                </View>  
                <View style={styles.peopleRow}>
                    <Text style={styles.sectionTitle}>People</Text>
                    <Text style={styles.seeAll}>See all</Text>
                </View>
                <View style={styles.imageRow}>
                    <TouchableOpacity style={styles.imageContainer}>
                        <Image source={require('../assets/blankImage.png')} style={styles.circleImage}/>
                        <Text>Danielle Dodoo</Text>
                    </TouchableOpacity>
                    <TouchableOpacity style={styles.imageContainer}>
                        <Image source={require('../assets/blankImage.png')} style={styles.circleImage}/>
                        <Text>Callum Thompson</Text>
                    </TouchableOpacity>
                    <TouchableOpacity style={styles.imageContainer}>
                        <Image source={require('../assets/blankImage.png')} style={styles.circleImage}/>
                        <Text>Jane Doe</Text>
                    </TouchableOpacity>
                </View>
                <View>
                    <View style={styles.rowContainer}>
                        <Text style={styles.sectionTitle}>Companies</Text>
                        <Text style={styles.seeAll}>See all</Text>
                    </View>
                    <Company style={styles.companies}/>
                    <Company/>
                </View>
                <View>
                    <View style={styles.rowContainer}>
                        <Text style={styles.sectionTitle}>Groups</Text>
                        <Text style={styles.seeAll}>See all</Text>
                    </View>
                    <Group style={styles.groups}/>
                    <Group/>
                </View>       
            </ScrollView>   
        </View>
    );
}

const styles = StyleSheet.create({
    pageContainer: {
        backgroundColor: '#f1f1f2'
    },
    circleImage: {
        width: 110,
        height: 110,
        borderRadius: 55,
        marginBottom: 10,
    },
    sectionTitle: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        fontSize: 12,
        marginLeft: 20,
        marginBottom: 10,
    },
    rowContainer: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center',
    },
    seeAll: {
        color: 'grey',
        fontFamily: 'Poppins-Bold',
        fontSize: 10,
        marginLeft: 250,
    },
    imageRow: {
        flexDirection: 'row',
        marginBottom: 20,
        alignItems: 'center',
        justifyContent: 'center',
    },
    imageContainer: {
        marginRight: 10,
        alignItems: 'center',
        justifyContent: 'center',
    },
    scrollContainer: {
        marginTop: 80,
    },
    searchText: {
        color: 'grey',
        fontFamily: 'Poppins-Light',
        fontSize: 12,
    },
    topContainer: {
        alignItems: 'center',
        justifyContent: 'center',
        marginTop: 60,
    },
    results: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        fontSize: 24,
        marginBottom: 10,
    },
    found: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Light',
        fontSize: 12,
        marginBottom: 25,
    },
    peopleRow: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center',
        marginTop: 20,
    },
});

export default SearchResults;