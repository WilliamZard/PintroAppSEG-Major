import React,{useEffect,useState,useCallback} from 'react';
import {useSelector, useDispatch} from 'react-redux';
import { StyleSheet, View, Text, TouchableOpacity, Image, ScrollView } from 'react-native';
import { SearchBar, ListItem } from 'react-native-elements';
import { fonts } from '../../Constants/Fonts.js';
import Colors from '../../Constants/Colors.js';
import WorkingSpace from '../../Components/WorkingSpace.js';
import * as SearchActions from "../../store/actions/search";
const SearchScreen = props => {
    const dispatch = useDispatch();
    const [searchKeyword,setSearchKeyword] = useState();
    const [suggestions,setSuggestions] = useState([]);
    const [suggestedItems,setItems] = useState([])

    const loadedTags = useSelector(state => state.tags.tagsArray);
    var tagNames = loadedTags.map(function(item) {
        return item['name'];
      });

    const tagList = [
        'Abicus','Business', 'Comics', 'Abicoids', 'Buseans', 'Comiaracus', 'Post Man2'
    ];
    
    function onTextChanged(searchWord) {
        setSearchKeyword(searchWord);
        if (searchWord.length > 2) {
            
            const regex = new RegExp(`^${searchWord}`,'i');
            //console.log(tagList.sort().filter(v => regex.test(v)));
            setSuggestions(tagList.sort().filter(v => regex.test(v))); 
        }
        renderSuggestions();
    }

    function onListItemPress(item) {
        //console.log(item);
        setSearchKeyword(item);
        setItems(null);
        dispatch(SearchActions.getResults(item));
        props.navigation.navigate('Results', {searchParam: item});
    }
    
    function renderSuggestions() {
        if(suggestions.length === 0 || searchKeyword.length < 3) {
            setItems(null);
        } else {
            setItems(suggestions.map((item) => 
                <ListItem 
                    key={item}
                    containerStyle={{width: 300, height: 50}} 
                    titleStyle={fonts.story} 
                    title={item}
                    button
                    onPress={() => onListItemPress(item)}
                />)
            );
        }
    }

    

    return(
        <View style={styles.blackContainer}>
            <View style={styles.topContainer}>
                <Text style={styles.browse}>Browse</Text>
                <Text style={styles.inspire}>Be inspired!</Text>
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
                    onChangeText={searchWord => onTextChanged(searchWord)}
                    value={searchKeyword}
                    clearIcon={null}/>
                {suggestedItems}
                <Text style={styles.category}>or Choose a Category</Text>
            </View>
            <View style={styles.rowContainer}>
                <TouchableOpacity style={styles.imageContainer}>
                    <Image source={require('../../assets/peopleImage.png')} style={styles.circleImage}/>
                    <Text style={fonts.tag_button_white}>PEOPLE</Text>
                </TouchableOpacity>
                <TouchableOpacity style={styles.imageContainer}>
                    <Image source={require('../../assets/companiesImage.png')} style={styles.circleImage}/>
                    <Text style={fonts.tag_button_white}>COMPANIES</Text>
                </TouchableOpacity>
                <TouchableOpacity style={styles.imageContainer}>
                    <Image source={require('../../assets/contentImage.png')} style={styles.circleImage}/>
                    <Text style={fonts.tag_button_white}>CONTENT</Text>
                </TouchableOpacity>
                <TouchableOpacity style={styles.imageContainer}>
                    <Image source={require('../../assets/groupsImage.png')} style={styles.circleImage}/>
                    <Text style={fonts.tag_button_white}>COMMUNITIES</Text>
                </TouchableOpacity>
                <TouchableOpacity style={styles.imageContainer}>
                    <Image source={require('../../assets/spacesImage.png')} style={styles.circleImage}/>
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
                <WorkingSpace 
                    name={"The Hub"}
                    spaces={"4 spaces available"} 
                    cost={"£25 per day"}
                    story={"Lorem ipsum dolor sit amet, consecteteur elit, sed \n do eiusmod tempor incididunt ut labore dolore."}
                />
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
        borderTopLeftRadius: 15,
        borderTopRightRadius: 15,
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
        marginBottom: 50,
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
        marginLeft: 20,
    },
    seeAll: {
        color: 'grey',
        fontFamily: 'Poppins-Bold',
        fontSize: 10,
        marginLeft: 250,
    },
    searchText: {
        color: 'grey',
        fontFamily: 'Poppins-Light',
        fontSize: 12,
    }
});

export default SearchScreen;