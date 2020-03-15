import React, {Component} from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  FlatList,
  Image,
} from 'react-native';
import firebase from '@react-native-firebase/app';
import Spinner from "react-native-loading-spinner-overlay";

export default class Messaging extends Component {
  constructor(props) {
    super(props);
    this.accountList = [
      {email: 'example1@gmail.com', password: '123456'},
      {email: 'example2@gmail.com', password: '123456'},
      {email: 'example3@gmail.com', password: '123456'},
      {email: 'example4@gmail.com', password: '123456'},
    ];
    this.currentAccount = 0;
    this.state = {
      chats: null,
      loading: true,
      currentEmail: this.accountList[0].email,
      currentChats: null,
    };
  }

  changeLogin = () => {
    this.setState({loading: true});
    this.currentAccount += 1;
    this.currentAccount %= this.accountList.length;
    let {email, password} = this.accountList[this.currentAccount];
    firebase
      .auth()
      .signOut()
      .then(() => {
        firebase
          .auth()
          .signInWithEmailAndPassword(email, password)
          .then(() => {
            this.setState({
              currentEmail: email,
            });
            this.loadChats(email);
          });
      });
  };

  loadChats(email) {
    // eventually thisll be an api call to /chatrooms/<email>
    // for now ill just hardcode data
    let testData;
    switch (this.state.currentEmail) {
      case 'example1@gmail.com':
        testData = [
          {chat_id: 'CHAT_A_B', recipient: 'example2@gmail.com'},
          {chat_id: 'CHAT_A_C', recipient: 'example3@gmail.com'},
        ];
        break;
      case 'example2@gmail.com':
        testData = [{chat_id: 'CHAT_A_B', recipient: 'example1@gmail.com'}];
        break;
      case 'example3@gmail.com':
        testData = [{chat_id: 'CHAT_A_C', recipient: 'example1@gmail.com'}];
        break;
      case 'example4@gmail.com':
        testData = [];
        break;
    }
    this.setState({
      chats: testData,
      loading: false,
    });
  }

  componentDidMount() {
    this.loadChats(this.state.email);
  }

  renderRow = ({item}) => {
    let recipient = item.recipient;
    let chat_id = item.chat_id;
    return (
      <TouchableOpacity
        onPress={() => {
          this.props.navigation.navigate('Chat', {
            email: this.state.currentEmail,
            recipient,
            chat_id,
          });
        }}>
        <View style={styles.profileContainer}>
          <Image
            source={{
              uri: 'https://www.gravatar.com/avatar/',
            }}
            style={styles.profileImage}
          />
          <Text style={styles.profileName}>User: {recipient}</Text>
        </View>
      </TouchableOpacity>
    );
  };

  render() {
    return (
      <View style={styles.container}>
        <TouchableOpacity onPress={this.changeLogin.bind(this)}>
          <View style={styles.emailView}>
            <Text style={styles.subHeaderText}>
              Direct Chats ({this.state.currentEmail})
            </Text>
          </View>
        </TouchableOpacity>
        <FlatList
          data={this.state.chats}
          renderItem={this.renderRow}
          enableEmptySections={true}
          keyExtractor={item => item.chat_id}
        />
        <Spinner visible={this.state.loading} />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 10,
    marginLeft: 18,
  },
  profileContainer: {
    flexDirection: 'row',
    marginTop: 8,
    marginBottom: 8,
    paddingBottom: 12,
    borderBottomColor: '#F1F1F2',
    borderBottomWidth: 2,
  },
  profileImage: {
    width: 60,
    height: 60,
    borderRadius: 30,
  },
  profileName: {
    marginLeft: 6,
    fontSize: 16,
    fontFamily: 'Poppins-Bold',
    color: 'black',
    marginTop: 6,
  },
  emailView: {
    marginTop: 6,
    marginBottom: 6,
  },
  subHeaderText: {
    fontFamily: 'Poppins-Bold',
    fontSize: 18,
  },
});
