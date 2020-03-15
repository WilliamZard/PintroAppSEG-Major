import React, { useState } from 'react';
import { Provider } from 'react-redux';
import { StyleSheet, Text, View } from 'react-native';
import * as Font from 'expo-font';
import { AppLoading } from 'expo';
import ReduxThunk from 'redux-thunk';
import { createStore, combineReducers, applyMiddleware } from 'redux';
import auth from './store/reducers/auth';
import Navigator from './navigation/LogInNavigator';
import timeLineReducer from './store/reducers/timeline';
import FinalSignUp from './Screens/FinalSignUp';
import tagsReducer from './store/reducers/tags';
import searchReducer from './store/reducers/search';

/**
 * Loading all fonts. The requite methods imply that the app will
 *  not start before every font has been loaded
 */
const rootReducer = combineReducers({
  auth: auth,
  timelinePosts:timeLineReducer,
  tags:tagsReducer,
  search:searchReducer
});
const store = createStore(rootReducer, applyMiddleware(ReduxThunk));


const fetchFonts = () => {
  return Font.loadAsync({
    'Poppins-Bold': require('./assets/Fonts/Poppins-Bold.otf'),
    'Poppins-Light': require('./assets/Fonts/Poppins-Light.otf'),
    'Poppins-LightItalic': require('./assets/Fonts/Poppins-LightItalic.otf'),
    'Poppins-Medium': require('./assets/Fonts/Poppins-Medium.otf'),
    'Poppins-MediumItalic': require('./assets/Fonts/Poppins-MediumItalic.otf'),
    'Poppins-Regular': require('./assets/Fonts/Poppins-Regular.otf'),
    'Poppins-SemiBold': require('./assets/Fonts/Poppins-SemiBold.otf'),
    'Poppins-SemiBoldItalic': require('./assets/Fonts/Poppins-SemiBoldItalic.otf'),
    'Poppins-Thin': require('./assets/Fonts/Poppins-Thin.otf'),
    'Poppins-ThinItalic': require('./assets/Fonts/Poppins-ThinItalic.otf')
  });
};

export default function App() {


  //State to make sure font is loaded.
  const [fontLoaded, setFontLoaded] = useState(false);
/**
 * AppLoading makes sure that the app does not start before every requirement has been
 * loaded.
 */
  if (!fontLoaded) {
    return <AppLoading
      startAsync={fetchFonts}
      onFinish={() => setFontLoaded(true)}
      onError={(err) => console.log(err)}
    />;
  }

  return (
   <Provider store={store}>
     <Navigator/>
   </Provider>
  )}

const styles = StyleSheet.create({
});

// FROM NEW App.js
import Connect from './Screens/Connect.js';
import Chat from './Screens/Chat.js';

import {createAppContainer} from 'react-navigation';
import {createStackNavigator} from 'react-navigation-stack';

const Stack = createStackNavigator({
  Connect: {
    screen: Connect,
  },
  Chat: {
    screen: Chat,
  },
});

export default createAppContainer(Stack);
