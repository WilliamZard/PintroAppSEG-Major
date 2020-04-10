import React, { Component } from "react";
import { StyleSheet, View } from "react-native";
import Svg, { Ellipse } from "react-native-svg";

function UserMoodCircle(props) {
  return (
    <View style={styles.container}>
      <Svg viewBox="0 0 40.38 40.32" style={styles.ellipse2}>
        <Ellipse
          strokeWidth={1}
          fill="#f6ab48"
          stroke="rgba(230, 230, 230,1)"
          cx={20}
          cy={20}
          rx={20}
          ry={20}
        ></Ellipse>
      </Svg>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    width: 40,
    height: 40
  },
  ellipse2: {
    width: 40,
    height: 40
  }
});

export default UserMoodCircle;