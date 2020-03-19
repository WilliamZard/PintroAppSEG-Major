import {createAppContainer, createSwitchNavigator} from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import { createBottomTabNavigator } from 'react-navigation-tabs';
import WhatsYourStory from '../Screens/WhatsYourStory';
import {Ionicons} from '@expo/vector-icons';
import SignInScreen from '../Screens/SignInScreen';
import HistoryScreen from '../Screens/HistoryScreen';
import StartScreen from '../Screens/StartScreen';
import LetsGetStarted from '../Screens/LetsGetStarted';
import ShowUsYourFace from '../Screens/ShowUsYourFace';
import React from 'react';
import {Image} from 'react-native' ; 
import Colors from '../Constants/Colors';
import WhatAreYourPassions from '../Screens/WhatAreYourPassions';
import HowCanYouHelpOthers from '../Screens/HowCanYouHelpOthers';
import EditPhoto from '../Screens/EditScreens/EditPhoto';
import MainMenubutton from '../Components/MainMenubutton';
import FirstScreen from '../Screens/MainScreens/FirstScreen';
import TimelinePage from '../Screens/MainScreens/TimelinePage';
import HomeScreen from '../Screens/MainScreens/HomeScreen';
import SearchScreen from '../Screens/MainScreens/SearchScreen';
import SearchResults from '../Screens/MainScreens/SearchResults';
import MessageScreen from '../Screens/MainScreens/MessageScreen';
import MapScreen from '../Screens/MainScreens/MapScreen';
import OnBoarding from '../Screens/OnBoarding';


const defaultStackNavOptions = {
    headerStyle: {
        backgroundColor:Colors.pintroBlack,
        shadowColor: 'transparent'
    },
    headerTintColor:'white',
    headerBackTitle:" ",
    title:' '
};
const mapOrFeed = createSwitchNavigator({
    
    
    Feed:TimelinePage,
    Map:MapScreen
});

const SearchNavigator = createStackNavigator({
    Browse:{screen:SearchScreen},
    Results:{screen:SearchResults}
});

const MainNav = createBottomTabNavigator({
    firstScreen:{
        screen:mapOrFeed, navigationOptions:{
            //tabBarLabel:'Screen 1',
            tabBarIcon: (tabInfo) => {
               return  <Image 
                        style={{height: 25, width: 30}}
                        source= {require('../images/homeIcon.png')} />
            },
            tabBarOptions:{
                showLabel: false,
               activeTintColor:'white',
               style: {
                 backgroundColor: 'white',
               },
           }
        }
    },
    searchScreen:{
        screen:SearchScreen,navigationOptions:{
            //tabBarLabel:'Screen 1',
            tabBarIcon: (tabInfo) => {
               return  <Image 
                        style={{height: 25, width: 25}}
                        
                        source= {require('../images/searchIcon.png')} />
            },
            tabBarOptions:{
                showLabel: false,
               activeTintColor:'white',
               style: {
                 backgroundColor: 'white',
               }, 
           }
        }
    },
    secondScreen:{
        screen:FirstScreen, navigationOptions:{
            tabBarIcon: <MainMenubutton/>,
            tabBarOptions:{
                showLabel: false,
                activeTintColor:'white',
                style: {
                  backgroundColor: 'white' 
                }, 
            }
        }
    },
    messageScreen:{
        screen:MessageScreen,navigationOptions:{
            //tabBarLabel:'Screen 1',
            tabBarIcon: (tabInfo) => {
               return  <Image 
                        style={{height: 25, width: 25,resizeMode:'contain'}}
                        source= {require('../images/messageTab.png')} />
            },
            tabBarOptions:{
               activeTintColor:'white',
               showLabel: false,
               style: {
                 backgroundColor: 'white',
               }, 
           }
        }
    },
    thirdScreen:{
        screen:HomeScreen,navigationOptions:{
            tabBarLabel:null,
        tabBarIcon: (tabInfo) => {
            return   <Image 
                    style={{height: 25, width: 30}}
                    source= {require('../images/profileIcon.png')} />
        },
        tabBarOptions:{
            activeTintColor:'white',
                showLabel: false,
            style: {
              backgroundColor: 'white',
             
            }, 
        }
      
        }
    },
});


const LogInNavigator = createStackNavigator({
    Start:{
        screen:StartScreen
    },
    LetsGetStarted:{
        screen:LetsGetStarted},
        Camera:{screen:ShowUsYourFace},
    WhatsYourStory:{screen:WhatsYourStory},
    
    TellUsHistory:{screen:HistoryScreen},
    Passions:{screen:WhatAreYourPassions},
    HelpOthers:{screen:HowCanYouHelpOthers},
    SignIn:{screen:SignInScreen}
},{
defaultNavigationOptions:defaultStackNavOptions});

const Onboarder = createSwitchNavigator({
    Boarding:OnBoarding,
    Login:LogInNavigator
});

const MySwitchNavigator = createSwitchNavigator(
    {
    routeOne: Onboarder, 
    routeTwo: MainNav  
    },
  );
export default createAppContainer(MySwitchNavigator);