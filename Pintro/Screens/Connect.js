import React, {Component} from 'react';
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
} from 'react-native';

import firebase from '@react-native-firebase/app';
import '@react-native-firebase/auth';
import '@react-native-firebase/database';
import Spinner from 'react-native-loading-spinner-overlay';

import Messaging from './Messaging';
import Notifications from './Notifications';

export default class Connect extends Component {
  constructor(props) {
    super(props);
    this.state = {
      screen: 'messaging',
    };
  }

  static navigationOptions = {
    headerShown: false,
  };

  async tryLogin() {
    //this.setState({ errorMessage: null, loading: true });
    //const { email, password } = this.state;
    const email = 'example1@gmail.com';
    const password = '123456';
    firebase
      .auth()
      .signInWithEmailAndPassword(email, password)
      .then(() => {
        //this.setState({ loading: false });
      })
      .catch(error => {
        console.log(error.message);
      });
  }

  render() {
    let currentScreen;
    switch (this.state.screen) {
      case 'messaging':
        currentScreen = (
          <Messaging
            navigation={this.props.navigation}
          />
        );
        break;
      case 'notifications':
        currentScreen = (
          <Notifications
            navigation={this.props.navigation}
          />
        );
        break;
    }
    return (
      <View style={styles.container}>
        <View style={styles.topGroup}>
          <Text style={styles.connectHeader}>Connect</Text>
          <View style={styles.subHeaderRow}>
            <TouchableOpacity
              onPress={() => {
                this.setState({
                  screen: 'messaging',
                });
              }}
              style={
                this.state.screen === 'messaging'
                  ? styles.subHeaderSelected
                  : styles.subHeader
              }>
              <Text style={styles.subHeaderText}>Messages</Text>
            </TouchableOpacity>
            <TouchableOpacity
              onPress={() => {
                this.setState({
                  screen: 'notifications',
                });
              }}
              style={
                this.state.screen === 'notifications'
                  ? styles.subHeaderSelected
                  : styles.subHeader
              }>
              <Text style={styles.subHeaderText}>Notifications</Text>
            </TouchableOpacity>
          </View>
        </View>
        {currentScreen}
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'stretch',
    backgroundColor: 'white',
  },
  topGroup: {
    flexDirection: 'column',
    alignItems: 'center',
    backgroundColor: '#F1F1F2',
  },
  connectHeader: {
    color: 'black',
    textAlign: 'center',
    alignItems: 'center',
    fontSize: 30,
    paddingTop: 10,
    fontFamily: 'Poppins-Regular',
  },
  subHeaderRow: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'flex-start',
    backgroundColor: '#F1F1F2',
    height: 40,
    paddingBottom: 40,
  },
  subHeader: {
    width: '50%',
    height: 40,
    paddingTop: 10,
  },
  subHeaderSelected: {
    width: '50%',
    height: 40,
    paddingTop: 10,
    borderBottomColor: '#F7A72E',
    borderBottomWidth: 3,
  },
  subHeaderText: {
    textAlign: 'center',
    fontFamily: 'Poppins-Regular',
    fontSize: 15,
    color: 'black',
  },
});
