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
import Colors from '../Constants/Colors';
import WhatAreYourPassions from '../Screens/WhatAreYourPassions';
import HowCanYouHelpOthers from '../Screens/HowCanYouHelpOthers';

import EditPhoto from '../Screens/EditScreens/EditPhoto';
import MainMenubutton from '../Components/MainMenubutton';

import FirstScreen from '../Screens/MainScreens/FirstScreen';
import TimelinePage from '../Screens/MainScreens/TimelinePage';
import HomeScreen from '../Screens/MainScreens/HomeScreen';

import MapScreen from '../Screens/MainScreens/MapScreen';

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

    Map:MapScreen,
    Feed:TimelinePage
});


const MainNav = createBottomTabNavigator({

    firstScreen:{
        screen:FirstScreen,navigationOptions:{
            tabBarLabel:'Screen 1',
            tabBarIcon: (tabInfo) => {
                return <Ionicons name = 'ios-star' size ={22} color={'white'}/>
            },
            tabBarOptions:{
               activeTintColor:'white',
               style: {
                 backgroundColor: '#1a1a1a',//color you want to change
               }
           }
        }
    },
    secondScreen:{
        screen:mapOrFeed,navigationOptions:{
            tabBarIcon: <MainMenubutton/>,
            tabBarOptions:{
                activeTintColor:'white',
                style: {
                  backgroundColor: '#1a1a1a',//color you want to change
                }
            }
        }
    },
    thirdScreen:{
        screen:HomeScreen,navigationOptions:{
            tabBarLabel:'Screen 3',
        tabBarIcon: (tabInfo) => {
            return <Ionicons name = 'ios-star' size ={22} color={'white'}/>
        },
        tabBarOptions:{
            activeTintColor:'white',
            style: {
              backgroundColor: '#1a1a1a',//color you want to change
             
            }
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



const MySwitchNavigator = createSwitchNavigator(
    {
    routeOne: LogInNavigator, 
    routeTwo: MainNav  
    },

  );

export default createAppContainer(MySwitchNavigator);