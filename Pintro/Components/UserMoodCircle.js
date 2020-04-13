import React, { Component } from "react";
import { StyleSheet, View } from "react-native";
import Svg, { Ellipse } from "react-native-svg";

function Index(props) {
  return (
    <View style={styles.container}>
      <Svg viewBox="0 0 45 45" style={styles.ellipse2}>
        <Ellipse
          strokeWidth={1}
          fill="#f6ab48"
          stroke="#f1f1f1"
          cx={23}
          cy={23}
          rx={23}
          ry={23}
        ></Ellipse>
      </Svg>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    width: 30,
    height: 31
  },
  ellipse2: {
    width: 30,
    height: 31
  }
});

export default Index;