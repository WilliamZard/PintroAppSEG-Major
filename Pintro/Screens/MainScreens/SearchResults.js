import React, { useState } from 'react';
import { useSelector,useDispatch } from 'react-redux';
import { StyleSheet, View, Text, ScrollView, FlatList } from 'react-native';
import { SearchBar } from 'react-native-elements';
import Colors from '../../Constants/Colors.js';
import Company from '../../Components/Company.js';
import Group from '../../Components/Groups.js';
import UserButton from '../../Components/UserButton.js';
import * as BusinessActions from '../../store/actions/business';
import * as UserActions from '../../store/actions/user';

const SearchResults = props => {
    const dispatch = useDispatch();
    const [scroll,setScroll] = useState(false);
    const searchResults = useSelector(state => state.search.usersArray);
    const currentUser = useSelector(state => state.user.email);

    let businesses = searchResults.map((item) => (item.profile_type === "business")? item : null).filter(profile => profile !== null);
    let users = searchResults.map((item) => (item.profile_type === "person")? item : null).filter(profile => profile !== null);
    
    function onCompanyPress(value) {
        dispatch(BusinessActions.getBusiness(value.email));
        if(value.team_members.includes(currentUser)) {
            props.navigation.navigate('navBusiness');
        } else {
            props.navigation.navigate('Profile');
        }
        //props.navigation.navigate('navBusiness');
    }

    async function onUserPress(value) {
        await dispatch(UserActions.get_Other_User(value));
        props.navigation.navigate('UserProfile');
    }

    businesses = businesses.map((item) => <Company key={item.email} props={props.Company} name={item.full_name} bio={item.short_bio} email={item.email} busObj={item} callback={value => onCompanyPress(value)}/>);
        

    function seeAllUsers() {
        setScroll(true);
    }

    return (
        <ScrollView style={styles.scrollContainer}>
            <View style={styles.pageContainer}>
                <View style={styles.topContainer}>
                    <Text style={styles.results}>Results ({(searchResults.length == 0)? 0 : searchResults.length})</Text>
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
                        onChangeText={()=>{}}
                        value={props.navigation.state.params.searchParam}/>
                </View>  
                <View style={styles.peopleRow}>
                    <Text style={styles.sectionTitle}>People</Text>
                    <Text style={styles.seeAll1} onPress={() => seeAllUsers()} color={scroll? 'grey' : Colors.pintroYellow}>See all</Text>
                </View>
                <FlatList 
                    data={users}
                    renderItem={({ item }) => <UserButton name={item.full_name} email={item.email} userObj={item} callback={value => onUserPress(value)}/>}
                    keyExtractor={item => item.email}
                    horizontal={true}
                    scrollEnabled={scroll}
                />
                <View>
                    <View style={styles.rowContainer}>
                        <Text style={styles.sectionTitle}>Companies</Text>
                        <Text style={styles.seeAll2}>See all</Text>
                    </View>
                    {businesses}
                </View>
                <View>
                    <View style={styles.rowContainer}>
                        <Text style={styles.sectionTitle}>Groups</Text>
                        <Text style={styles.seeAll1}>See all</Text>
                    </View>
                    <Group
                        name={"Group Name 1"}
                        members={"100 Members"}    
                    />
                    <Group
                        name={"Group Name 2"}
                        members={"69 Members"}
                    />
                </View>       
              </View> 
        </ScrollView>
    );
}

const styles = StyleSheet.create({
    pageContainer: {
        marginTop: 80,        
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
        marginBottom: 10,
        textAlign: 'left',
        marginLeft: 20,
    },
    rowContainer: {
        flexDirection: 'row',
    },
    seeAll1: {
        color: 'grey',
        fontFamily: 'Poppins-Bold',
        fontSize: 10,
        textAlign: 'right',
        marginTop: 2.5,
        marginLeft: 295
    },
    seeAll2: {
        color: 'grey',
        fontFamily: 'Poppins-Bold',
        fontSize: 10,
        textAlign: 'right',
        marginTop: 2.5,
        marginLeft: 268
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
        backgroundColor: '#f1f1f2'
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
        marginTop: 20,
    },
});

export default SearchResults;