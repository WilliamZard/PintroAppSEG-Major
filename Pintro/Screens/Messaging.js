import React, {Component} from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  FlatList,
  Image,
} from 'react-native';
import firebase from 'firebase';
import Spinner from "react-native-loading-spinner-overlay";
import TimeAgo from 'react-native-timeago';
import {connect} from "react-redux";

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
      "last_seen/"+this.props.chat_id+'/'+this.props.email.replace(/[.#$\[\]]/g, '?')
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
    let hasSeen = this.state.lastMessage == null || this.state.lastSeen === this.state.lastMessage._id;
    let lastMessageStyle = hasSeen ? styles.lastMessage : styles.lastMessageNew;
    return (
      <TouchableOpacity
        onPress={() => {
          this.props.navigation.navigate('Chat', {
            email: this.props.email,
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
                    {this.state.lastMessage.text}
                  </Text>
                  <Text style={{...lastMessageStyle, flexGrow: 1}}>
                    • <TimeAgo time={this.state.lastMessage.createdAt}/>
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

class Messaging extends Component {
  constructor(props) {
    super(props);
    this.state = {
      chats: null,
      loading: true,
    };
  }

  async loadChats() {
    let userType = this.props.userType === "Business" ? 'businesses' : 'users';
    let chatData = await fetch(
      `https://bluej-pintro-project.appspot.com/${userType}/${this.props.email}/chatrooms/`,
      {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer ' + this.props.token,
        },
        redirect: 'follow',
      }
    );
    this.setState({
      chats: chatData.status !== 200 ? [] : await chatData.json(),
      loading: false,
    });
  }

  async componentDidMount() {
    await this.loadChats();
  }

  renderRow = ({item}) => {
    return <ChatroomEntry
      navigation={this.props.navigation}
      recipient={item.recipient}
      chat_id={item.chat_id}
      email={this.props.email}
    />;
  };

  render() {
    return (
      <View style={styles.container}>
        <View style={styles.emailView}>
          <Text style={styles.subHeaderText}>Direct Chats</Text>
        </View>
        <FlatList
          data={this.state.chats}
          renderItem={this.renderRow}
          enableEmptySections={true}
          keyExtractor={item => `${item.chat_id} ${item.recipient}`}
        />
        <Spinner visible={this.state.loading} />
      </View>
    );
  }
}

export default connect(state => {
  return {
    email: state.user.email,
    token: state.auth.tokenToGet,
    userType: state.hasOwnProperty('businessObj') ? 'Business' : "Person",
  };
})(Messaging);

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
