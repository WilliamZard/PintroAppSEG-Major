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
import TimeAgo from 'react-native-timeago';

class ChatroomEntry extends Component {
  constructor(props) {
    super(props);
    this.state = {
      lastMessage: null,
      lastSeen: null,
    }
  }

  async componentDidMount() {
    let lastSeen;
    let lastMessage;
    let lastSeenRef = firebase.database().ref(
      "last_seen/"+this.props.chat_id+'/'+this.props.currentEmail.replace(/[.#$\[\]]/g, '?')
    );
    await lastSeenRef.once("value", snap => {
      lastSeen = snap.val();
    });

    await firebase.database().ref("chat/"+this.props.chat_id)
      .orderByChild("order")
      .once("value", snap => {
        snap.forEach(value => {
          lastMessage = value.val();
          return true;
        });
      });
    this.setState({
      lastSeen,
      lastMessage,
    });
  }

  updateLastMessage = lastMessage => {
    if (lastMessage == null) return;
    this.setState({
      lastMessage: lastMessage,
      lastSeen: lastMessage._id,
    });
  };

  render() {
    console.log(JSON.stringify(this.state));
    let hasSeen = this.state.lastMessage == null || this.state.lastSeen === this.state.lastMessage._id;
    let lastMessageStyle = hasSeen ? styles.lastMessage : styles.lastMessageNew;
    return (
      <TouchableOpacity
        onPress={() => {
          this.props.navigation.navigate('Chat', {
            email: this.props.currentEmail,
            recipient: this.props.recipient,
            chat_id: this.props.chat_id,
            updateLastMessage: this.updateLastMessage,
          });
        }}>
        <View style={styles.profileContainer}>
          <Image
            source={{
              uri: 'https://www.gravatar.com/avatar/',
            }}
            style={styles.profileImage}
          />
          <View style={styles.profileText}>
            <Text style={styles.profileName} numberOfLines={1}>User: {this.props.recipient}</Text>
            <View style={styles.messageText}>
              {this.state.lastMessage == null ? null :
                <>
                  <Text style={lastMessageStyle} numberOfLines={1}>
                    {this.state.lastMessage == null ? '' : this.state.lastMessage.text}
                  </Text>
                  <Text style={{...lastMessageStyle, flexGrow: 1}}>• <TimeAgo
                    timestamp={this.state.lastMessage.createdAt}
                    interval={20000}
                    style={lastMessageStyle}/>
                  </Text>
                </>
              }
            </View>
          </View>
          <View style={{...styles.newMessageMarker, opacity: hasSeen ? 0 : 100}} />
        </View>
      </TouchableOpacity>
    );
  }
}

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
    return <ChatroomEntry
      navigation={this.props.navigation}
      recipient={item.recipient}
      chat_id={item.chat_id}
      currentEmail={this.state.currentEmail}
    />;
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
  },
  profileContainer: {
    flexDirection: 'row',
    marginTop: 8,
    marginBottom: 8,
    paddingBottom: 12,
    borderBottomColor: '#F1F1F2',
    borderBottomWidth: 2,
    paddingLeft: 18,
  },
  profileImage: {
    width: 60,
    height: 60,
    borderRadius: 30,
  },
  profileName: {
    fontSize: 16,
    fontFamily: 'Poppins-SemiBold',
    color: 'black',
    marginTop: 6,
  },
  emailView: {
    marginTop: 6,
    marginBottom: 6,
    marginLeft: 18,
  },
  subHeaderText: {
    fontFamily: 'Poppins-SemiBold',
    fontSize: 18,
  },
  profileText: {
    flex: 1,
    flexDirection: "column",
    marginLeft: 6
  },
  lastMessage: {
    color: 'grey',
    fontFamily: 'Poppins-Regular',
    fontSize: 12,
    flex: 1,
  },
  lastMessageNew: {
    color: 'black',
    fontFamily: 'Poppins-SemiBold',
    fontSize: 12,
    flex: 1,
  },
  messageText: {
    flexDirection: 'row',
    alignItems: 'flex-start',
  },
  newMessageMarker: {
    height: 12,
    width: 12,
    borderRadius: 12,
    margin: 25,
    marginRight: 30,
    backgroundColor: 'orange',
  }
});
