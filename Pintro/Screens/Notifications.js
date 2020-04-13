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
import {connect} from "react-redux";

class AcceptChoiceNotif extends Component {
  // (props, message, accept, decline)
  constructor(props) {
    super(props);
    this.state = {
      recipientData: null,
    };
  }

  async componentDidMount() {
    let recipientData = await fetch(
      `https://bluej-pintro-project.appspot.com/${this.props.requesterType}/${this.props.notification.requester_email}`,
      {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer ' + this.props.token
        },
        redirect: 'follow',
      }
    );
    this.setState({
      recipientData: await recipientData.json()
    });
  }

  render() {
    if (this.state.recipientData == null) {
      return null;
    }
    console.log(JSON.stringify(Object.keys(this.state.recipientData)));
    return (
      <View style={styles.notifContainer}>
        <Image
            source={{
              uri: 'data:image/png;base64,' + this.state.recipientData.profile_image,
            }}
            style={styles.profileImage}
        />
        <View style={styles.notifText}>
          <Text style={styles.notifMessage} numberOfLines={1}>{this.state.recipientData.full_name}{this.props.message}</Text>
          <TimeAgo time={this.props.notification.created_at * 1000} style={styles.timeAgoText}/>
        </View>
        <View style={styles.choiceButtonContainer}>
          <TouchableOpacity
              onPress={this.props.decline}
          >
            <Image
                source={require('../assets/buttonDecline.png')}
                style={styles.choiceButtonStyle}
            />
          </TouchableOpacity>
          <TouchableOpacity
              onPress={this.props.accept}
          >
            <Image
                source={require('../assets/buttonAccept.png')}
                style={styles.choiceButtonStyle}
            />
          </TouchableOpacity>
        </View>
      </View>
    );
  }
}

const notifTypes = {
  follow(props) {
    return <AcceptChoiceNotif
      {...props}
      message=" sent you a follow request."
      requesterType="users"
      accept={async () => {
        await fetch(
          `https://bluej-pintro-project.appspot.com/approve/follow/${props.notification.requester_email}/${this.props.email}`,
          {
            method: 'POST',
            headers: {
              'Authorization': 'Bearer ' + props.token,
            },
            redirect: 'follow',
          }
        );
        props.deleteNotif();
      }}
      decline={async () => {
        await fetch(
          `https://bluej-pintro-project.appspot.com/request/follow/${props.notification.requester_email}/${this.props.email}`,
          {
            method: 'DELETE',
            headers: {
              'Authorization': 'Bearer ' + props.token,
            },
            redirect: 'follow',
          }
        );
        props.deleteNotif();
      }}
    />;
  },
  affiliation(props) {
    return <AcceptChoiceNotif
      {...props}
      message=" sent you an affiliation request."
      requesterType="businesses"
      accept={async () => {
        await fetch(
          `https://bluej-pintro-project.appspot.com/approve/affiliation/${props.notification.requester_email}/${this.props.email}`,
          {
            method: 'POST',
            headers: {
              'Authorization': 'Bearer ' + props.token,
            },
            redirect: 'follow',
          }
        );
        props.deleteNotif();
      }}
      decline={async () => {
        await fetch(
          `https://bluej-pintro-project.appspot.com/request/affiliation/${props.notification.requester_email}/${this.props.email}`,
          {
            method: 'DELETE',
            headers: {
              'Authorization': 'Bearer ' + props.token,
            },
            redirect: 'follow',
          }
        );
        props.deleteNotif();
      }}
    />;
  },
};

class Notifications extends Component {
  constructor(props) {
    super(props);
    this.state = {
      notifs: null,
      loading: true,
    }
  }

  async componentDidMount() {
    let notifData = await fetch(
      `https://bluej-pintro-project.appspot.com/notifications/${this.props.email}`,
      {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer ' + this.props.token,
        },
        redirect: 'follow',
      }
    );
    this.setState({
      loading: false,
      notifs: await notifData.json(),
    });
  }

  deleteNotif = (index) => () => {
    let notifs = [...this.state.notifs];
    notifs.splice(index, 1);
    this.setState({notifs});
  };

  mapNotif = ({item, index}) => {
    let NotificationType = notifTypes[item.relationship_type];
    return <NotificationType
      notification={item}
      deleteNotif={this.deleteNotif(index)}
      token={this.props.token}
    />;
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
}

export default connect(state => {
  return {
    email: state.user.email,
    token: state.auth.tokenToGet,
    userType: state.hasOwnProperty('businessObj') ? 'Business' : "Person",
  };
})(Notifications);

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
