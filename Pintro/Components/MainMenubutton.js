import React,{useState} from 'react';
import {View,
Text,
Image,
StyleSheet,TouchableHighlight,
Modal,
TextInput,
Button
} from 'react-native';
import {Ionicons} from '@expo/vector-icons';
import WriteAPost from '../Screens/MainScreens/WriteAPost';
import { TouchableWithoutFeedback } from 'react-native-gesture-handler';

const MainMenuButton = props => {
    const backButton =() =>{
        setWritingPost(false);
        };
    const [inFocus,setInFocus] = useState(false); 
    const [writingPost,setWritingPost] = useState(false); 
    return(
        
        <View style = {{position:'absolute', alignItems:'center',flex:1 ,backgroundColor:'orange'}} >
            <Modal transparent={true} visible={inFocus} style={{backgroundColor:'green'}}>
           
                <View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
                <View style={{width:300,height:400,backgroundColor:'#fcfcfc', position:'absolute',borderRadius:20,shadowColor: "black",
shadowOffset: {
	width: 0,
	height: 4,
},
shadowOpacity: 0.50,
shadowRadius: 15.65,

elevation: 8,
justifyContent:'center'}}>

                    <View style={styles.container}>
                    <Text style={styles.textStyles}>Whats going on</Text>
                   
                   <View style={styles.listofFuncs}>
                       <View style={styles.icon}><Ionicons name = 'ios-star' size ={22} color={'black'}/></View>
                      <View style={styles.buttonsToFunc}><TouchableHighlight><Text>Check-In</Text></TouchableHighlight></View> 
                  
                   </View>
                   <View style={styles.listofFuncs}>
                       <View style={styles.icon}><Ionicons name = 'ios-star' size ={22} color={'black'}/></View>
                       <View style={styles.buttonsToFunc}><TouchableHighlight><Text>Talk to me about</Text></TouchableHighlight></View> 
                  
                   </View>
                   <View style={styles.listofFuncs}>
                       <View style={styles.icon}><Ionicons name = 'ios-star' size ={22} color={'black'}/></View>
                       <View style={styles.buttonsToFunc}><TouchableHighlight><Text>Ask for help</Text></TouchableHighlight></View> 
                  
                   </View>
                   <View style={styles.listofFuncs}>
                       <View style={styles.icon}><Ionicons name = 'ios-star' size ={22} color={'black'}/></View>
                       <View style={styles.buttonsToFunc}><TouchableHighlight
                        onPress={()=>{
                            setInFocus(false);
                            setWritingPost(true);
                        }}
                       ><Text>Request an intro</Text></TouchableHighlight></View> 
                  
                   </View>
                    <View>
                        <TouchableHighlight style={styles.buttonLayout} onPress={()=>setInFocus(false)}><Text style={{color:'white'}}>Cancel</Text></TouchableHighlight>
                    </View>
                    </View>
                    </View>
                    </View>
                  
                    </Modal>
           <View style={styles.button}>
               <TouchableHighlight underlayColor="#7F58FF" onPress={()=>{
                        setInFocus(true);
                    
               }}>
               <View>
               <Modal transparent={false} visible={writingPost} style={{backgroundColor:'green'}}>
<WriteAPost onBack={backButton}/>
                   </Modal>
                
               <Image style={{height: 25, width: 25, resizeMode:'contain'}} source= {require('../images/searchIcon.png')}/>
              
               </View>

               </TouchableHighlight>
           </View>
        </View>
    );

    
};


const styles = StyleSheet.create({
button:{
    alignItems: "center",
    justifyContent: "center",
    width: 52,
    height: 52,
    borderRadius: 36,
    backgroundColor: 'white',
    position: "absolute",
    marginTop: -33,

},listofFuncs:{
      
    flexDirection:'row',
    width:'100%',
    margin:10
   
    

},container:{
    alignItems: "center",
    justifyContent: "center",
},icon:{
    width:40,
    height:40,
    justifyContent:'center',
    alignItems:'center',
    borderRadius:10,
    backgroundColor:'orange',
    marginHorizontal:10
},
buttonsToFunc:{
    justifyContent:'center',
    alignItems:'center',
    width:'70%',
    backgroundColor:'white',
    borderRadius:10,
    shadowColor: "black",
    marginHorizontal:15,

shadowOffset: {
	width: 0,
	height: 4,
},
shadowOpacity: 0.50,
shadowRadius: 15.65,

elevation: 8,

},
buttonLayout:{
    backgroundColor:'#f03434',
    padding:10,
    borderRadius:15,
    shadowOffset: {
        width: 0,
        height: 4,
    },
    shadowOpacity: 0.50,
    shadowRadius: 15.65,
    shadowColor: "grey",
    
}
});
export default MainMenuButton;