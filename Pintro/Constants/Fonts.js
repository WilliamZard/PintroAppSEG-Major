import { StyleSheet } from 'react-native';
import Colors from './Colors.js';

const fonts = StyleSheet.create({
    name_black: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        fontSize: 14
    },
    title_black: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Bold',
        fontSize: 12
    },
    title_yellow: {
        color: Colors.pintroYellow,
        fontFamily: 'Poppins-Bold',
        fontSize: 12
    },
    bio: {
        color: 'grey',
        fontFamily: 'Poppins-Light',
        fontSize: 8
    },
    location: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Light',
        fontSize: 8
    },
    tag_button_black: {
        color: Colors.pintroBlack,
        fontFamily: 'Poppins-Light',
        fontSize: 10
    },
    tag_button_white: {
        color: Colors.pintroWhite,
        fontFamily: 'Poppins-Light',
        fontSize: 10
    },
    story: {
        color: 'grey',
        fontFamily: 'Poppins-Bold',
        fontSize:12
    },
    more_yellow: {
        color: Colors.pintroYellow,
        fontFamily: 'Poppins-Bold',
        fontSize:8
    },
    more_white: {
        color: 'grey',
        fontFamily: 'Poppins-light',
        fontSize: 8,
        textAlign: 'right'
    }
});

export { fonts };
