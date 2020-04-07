import React, {Component} from 'react';
import {StyleSheet, View} from 'react-native';
import {GiftedChat, Bubble} from 'react-native-gifted-chat';
import firebase from 'firebase';
import Spinner from "react-native-loading-spinner-overlay";

export default class Chat extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      messages: [],
    };
    this.lastMessage = null;

    const {chat_id, email} = this.props.navigation.state.params;

    this.chatRef = this.getRef().child('chat/' + chat_id);
    this.lastSeenRef = this.getRef()
        .child('last_seen/' + chat_id)
        .child(email.replace(/[.#$\[\]]/g, '?'));
    this.chatRefData = this.chatRef.orderByChild('order');
    this.onSend = this.onSend.bind(this);
  }

  getRef() {
    return firebase.database().ref();
  }

  listenForItems(chatRef) {
    chatRef.on('value', snap => {
      let items = [];
      this.lastMessage = null;
      snap.forEach(child => {
        if (this.lastMessage == null)
          this.lastMessage = child.val();

        items.push({
          _id: child.val().createdAt,
          text: child.val().text,
          createdAt: new Date(child.val().createdAt),
          user: {
            _id: child.val().user._id,
            avatar: 'https://www.gravatar.com/avatar/',
          },
        });
      });

      if (this.lastMessage != null)
        this.lastSeenRef.set(this.lastMessage._id);

      this.setState({
        loading: false,
        messages: items,
      });
    });
  }

  static navigationOptions = ({navigation}) => ({
    title: `${navigation.state.params.recipient}`,
    headerTitleStyle: {
      fontFamily: 'Poppins-SemiBold',
    },
    headerStyle: {

    }
  });

  componentDidMount() {
    this.listenForItems(this.chatRefData);
  }

  componentWillUnmount() {
    this.chatRefData.off();
    this.props.navigation.state.params.updateLastMessage(this.lastMessage);
  }

  onSend(messages = []) {
    let id;
    messages.forEach(message => {
      id = new Date().getTime();
      let msg = {
        _id: id,
        text: message.text,
        createdAt: id,
        user: {
          _id: this.props.navigation.state.params.email,
        },
        order: -1 * id,
      };
      this.chatRef.push(msg);
    });
    this.lastSeenRef.set(id);
  }

  renderMessage = props => {
    return (
      <Bubble
        {...props}
        textStyle={{
          left: styles.leftText,
          right: styles.rightText,
        }}
        wrapperStyle={{
          left: styles.leftBubble,
          right: styles.rightBubble,
        }}
      />
    );
  };

  render() {
    return (
      <View style={{flex: 1}}>
        <GiftedChat
          messages={this.state.messages}
          onSend={this.onSend.bind(this)}
          user={{
            _id: this.props.navigation.state.params.email,
          }}
          renderBubble={this.renderMessage}
          renderTime={() => null}
        />
        <Spinner visible={this.state.loading} />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  leftText: {
    color: 'black',
    fontFamily: 'Poppins-Regular',
    fontSize: 14,
  },
  rightText: {
    color: 'white',
    fontFamily: 'Poppins-Regular',
    fontSize: 14,
  },
  leftBubble: {
    backgroundColor: 'white',
    padding: 10,
    flex: 1,
    marginLeft: 5,
  },
  rightBubble: {
    backgroundColor: 'black',
    padding: 10,
    flex: 1,
    marginRight: 5,
  },
});
