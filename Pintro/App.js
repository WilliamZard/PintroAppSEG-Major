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
