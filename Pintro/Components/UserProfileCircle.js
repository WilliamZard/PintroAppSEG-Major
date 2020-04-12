import React, { Component } from "react";
import { StyleSheet, View } from "react-native";
import Svg, { Ellipse } from "react-native-svg";

function Index(props) {
  return (
    <View style={styles.container}>
      <Svg viewBox="0 0 90 90" style={styles.ellipse}>
        <Ellipse
          strokeWidth={1}
          fill="#1a1a1a"
          stroke="#f1f1f1"
          cx={41}
          cy={45}
          rx={40}
          ry={45}
        ></Ellipse>
      </Svg>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    width: 82,
    height: 90
  },
  ellipse: {
    width: 82,
    height: 90
  }
});

export default Index;