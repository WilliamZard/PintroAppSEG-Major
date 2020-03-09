import React from 'react';
import {
View,
Text,
StyleSheet
} from 'react-native';


const FirstScreen = props => {

return (
    <View style={styles.main}>
        <Text>
            First Screen
        </Text>
    </View>
);

};

const styles = StyleSheet.create({
main:{
    justifyContent:'center',
    alignItems:'center'
}
});

export default FirstScreen;