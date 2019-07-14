<template>
    <textarea class='talkBar w-100 p-2'
    type="text"
    v-model="userMsg" 
    @keyup.enter="userSendData()">

    </textarea>
</template>

<script>
  import axios from 'axios'
  import VueAxios from 'vue-axios'
  export default {
  data: function(){
    return{
      userMsg: [],
    }
  },
  methods:{
    userSendData() {
      this.axios.post('http://202.182.106.200:5000', {
        text: this.userMsg,
      }).then((response) => {
        console.log(response)
      }).catch((response)=>{
    console.log(response)  
      })
    }
  
  },
  mounted() { 
    
}
  }

</script>

<style lang="sass" scope>
//顏色定義
$color_blue: #282f44
$color_brown: #E6AF2E
$color_yellow: #f5d061
$color_brown: #E6AF2E
$color_white: #ececec
$color_orange: #ff6e3a
$color_red: #FF3D4A
$color_gray: #C2C2C2
// ---------------
*
  font-family: 'Oswald','微軟正黑體' 
  position: relative

//一些常用的mixin
@mixin ab_center
  position: absolute
  left: 50%
  top: 50%
  transform: translate(-50%,-50%)

@mixin size($w,$h)
  width: $w
  height: $h
// ------------------

@keyframes fadeIn
  0%
    opacity: 0
  20%
    opacity: 0.2
  50%
    opacity: 0.5
  70%
    opacity: 0.7
  100%
    opacity: 1
// ----------------------

.talkBar
  height: 80px
  position: absolute
  bottom: 0px
</style>