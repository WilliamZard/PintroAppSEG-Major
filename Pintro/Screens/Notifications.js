import React, {Component} from 'react';
import {
  StyleSheet,
  Text,
  View,
  FlatList,
  TouchableOpacity,
  Image,
} from 'react-native';
import Spinner from "react-native-loading-spinner-overlay";
import TimeAgo from "react-native-timeago";

function acceptChoiceNotif(props, message, accept, decline) {
  return (
    <View style={styles.notifContainer}>
      <Image
        source={{
          uri: 'https://www.gravatar.com/avatar/'
        }}
        style={styles.profileImage}
      />
      <View style={styles.notifText}>
        <Text style={styles.notifMessage} numberOfLines={1}>{message}</Text>
        <TimeAgo time={props.notification.created_at * 1000} style={styles.timeAgoText}/>
      </View>
      <View style={styles.choiceButtonContainer}>
        <TouchableOpacity
          onPress={decline}
        >
          <Image
            source={require('../assets/Images/buttonDecline.png')}
            style={styles.choiceButtonStyle}
          />
        </TouchableOpacity>
        <TouchableOpacity
          onPress={accept}
        >
          <Image
            source={require('../assets/Images/buttonAccept.png')}
            style={styles.choiceButtonStyle}
          />
        </TouchableOpacity>
      </View>
    </View>
  );
}

const notifTypes = {
  // TODO: add actual api calls to this (button functionality and getting user data)
  follow(props) {
    return acceptChoiceNotif(
      props,
      `User ${props.notification.requester_email} sent you a follow request.`,
      () => {
        console.log('accept pressed for follow request');
      },
      () => {
        console.log('decline pressed for follow request');
      }
    );
  },
  affiliation(props) {
    return acceptChoiceNotif(
      props,
      `Business ${props.notification.requester_email} sent you an affiliation request.`,
      () => {
        console.log('accept pressed for affiliation request');
      },
      () => {
        console.log('decline pressed for affiliation request');
      }
    );
  },
};

export default class Notifications extends Component {
  constructor(props) {
    super(props);
    this.state = {
      notifs: null,
      loading: true,
    }
  }

  async componentDidMount() {
    // TODO: put an actual api call here
    // these should have recipient_email as well
    // but i dont actually need to use it, so whatever
    this.setState({
      loading: false,
      notifs: [
        {
          requester_email: 'example1@gmail.com',
          relationship_type: 'follow',
          created_at: 1585777435.3389518
        },
        {
          requester_email: 'example2@gmail.com',
          relationship_type: 'affiliation',
          created_at: 1585777415.3389518
        }
      ]
    });
  }

  mapNotif = ({item}) => {
    let NotificationType = notifTypes[item.relationship_type];
    return <NotificationType notification={item}/>;
  };

  render() {
    return (
      <View style={styles.container}>
        <FlatList
          data={this.state.notifs}
          renderItem={this.mapNotif}
          enableEmptySections={true}
          keyExtractor={(notif) => notif.requester_email + '/' + notif.relationship_type}
        />
        <Spinner visible={this.state.loading} />
      </View>
    );
  }
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 10,
  },
  notifContainer: {
    flexDirection: 'row',
    marginTop: 8,
    marginBottom: 8,
    paddingBottom: 12,
    borderBottomColor: '#F1F1F2',
    borderBottomWidth: 2,
    paddingLeft: 12,
  },
  profileImage: {
    width: 40,
    height: 40,
    borderRadius: 30,
  },
  notifText: {
    flex: 1,
    flexDirection: "column",
    marginLeft: 8
  },
  notifMessage: {
    fontSize: 12,
    fontFamily: 'Poppins-SemiBold',
    color: 'black',
  },
  timeAgoText: {
    fontSize: 10,
    fontFamily: 'Poppins-Regular',
    color: 'grey',
    marginTop: 6,
  },
  choiceButtonContainer: {
    marginRight: 15,
    flexDirection: 'row',
  },
  choiceButtonStyle: {
    marginRight: 5,
    height: 40,
    width: 40,
  },
});
