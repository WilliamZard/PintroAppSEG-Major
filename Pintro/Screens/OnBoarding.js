import React from 'react';
import {
    View,
    Text,
    StyleSheet,
    Image
} from 'react-native';
import Onboarding from 'react-native-onboarding-swiper';
import { HeaderTitle } from 'react-navigation-stack';

const OnBoarding = props => {

return(
    <View style={styles.main}>
   <Onboarding
   onSkip={()=>props.navigation.navigate({routeName:'Start'})}
   onDone={()=>props.navigation.navigate({routeName:'Start'})}
    pages={[
      {
        backgroundColor: '#1a1a1a',
        image: <Image style={{width:400,height:600,resizeMode:'contain'}}source={require('../images/handShake.png')} />,
        title: '',
        subtitle: '',
      },
      {
        backgroundColor: '#1a1a1a',
        image: <Image style={{width:400,height:600,resizeMode:'contain'}}source={require('../images/meditation.png')} />,
        title: '',
        subtitle: '',
      },
      {
        backgroundColor: '#1a1a1a',
        image: <Image style={{width:400,height:600,resizeMode:'contain'}}source={require('../images/handClap.png')} />,
        title: '',
        subtitle: "",
      },
    ]}
  />
    </View>
);

};

OnBoarding.navigationOptions={
    headerShown: false
};

const styles = StyleSheet.create({

    main:{
flex:1,
backgroundColor:'#1a1a1a'


    }
});

export default OnBoarding;