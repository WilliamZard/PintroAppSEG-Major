import Connect from '../Connect.js';
import Chat from '../Chat.js';

import {createStackNavigator} from 'react-navigation-stack';

export default createStackNavigator({
  Connect: {
    screen: Connect,
  },
  Chat: {
    screen: Chat,
  },
});
