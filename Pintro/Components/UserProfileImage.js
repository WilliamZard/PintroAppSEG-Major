import React, { Component } from "react";
import { StyleSheet, View } from "react-native";
import Svg, { Ellipse } from "react-native-svg";

function UserProfileImage(props) {
  return (
    <View style={styles.container}>
      <Svg viewBox="0 0 99.51 100.14" style={styles.ellipse}>
        <Ellipse
          strokeWidth={1}
          fill="#1a1a1a"
          stroke="rgba(230, 230, 230,1)"
          cx={50}
          cy={50}
          rx={49}
          ry={50}
        ></Ellipse>
      </Svg>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    width: 100,
    height: 100
  },
  ellipse: {
    width: 100,
    height: 100
  }
});

export default UserProfileImage;