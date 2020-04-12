import React, { Component } from "react";
import { StyleSheet, View } from "react-native";
import Svg, { Ellipse } from "react-native-svg";

function Index(props) {
  return (
    <View style={styles.container}>
      <Svg viewBox="0 0 35 35" style={styles.ellipse2}>
        <Ellipse
          strokeWidth={1}
          fill="#f6ab48"
          stroke="#f1f1f1"
          cx={15}
          cy={16}
          rx={15}
          ry={15}
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