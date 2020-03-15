import React, {Component} from 'react';
import {StyleSheet} from 'react-native';
import {GiftedChat, Bubble} from 'react-native-gifted-chat';
import firebase from '@react-native-firebase/app';

export default class Chat extends Component {
  constructor(props) {
    super(props);
    this.state = {
      messages: [],
    };

    const {chat_id} = this.props.navigation.state.params;

    this.chatRef = this.getRef().child('chat/' + chat_id);
    this.chatRefData = this.chatRef.orderByChild('order');
    this.onSend = this.onSend.bind(this);
  }

  getRef() {
    return firebase.database().ref();
  }

  listenForItems(chatRef) {
    chatRef.on('value', snap => {
      let items = [];
      snap.forEach(child => {
        items.push({
          _id: child.val().createdAt,
          text: child.val().text,
          createdAt: new Date(child.val().createdAt),
          user: {
            _id: child.val().email,
            avatar: 'https://www.gravatar.com/avatar/',
          },
          email: child.val().email,
        });
      });

      this.setState({
        loading: false,
        messages: items,
      });
    });
  }

  static navigationOptions = ({navigation}) => ({
    title: `${navigation.state.params.recipient}`,
    headerTitleStyle: {
      fontFamily: 'Poppins-Bold',
    },
  });

  componentDidMount() {
    this.listenForItems(this.chatRefData);
  }

  componentWillUnmount() {
    this.chatRefData.off();
  }

  onSend(messages = []) {
    messages.forEach(message => {
      let now = new Date().getTime();
      let msg = {
        _id: now,
        text: message.text,
        createdAt: now,
        user: {
          _id: this.props.navigation.state.params.email,
        },
        email: this.props.navigation.state.params.email,
        order: -1 * now,
      };
      this.chatRef.push(msg);
    });
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
      <GiftedChat
        messages={this.state.messages}
        onSend={this.onSend.bind(this)}
        user={{
          _id: this.props.navigation.state.params.email,
        }}
        renderBubble={this.renderMessage}
        renderTime={() => null}
      />
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
