<template>
<div>
    <appNavbar></appNavbar>
    <appLogin></appLogin>
  <!-- <appTag></appTag> -->
</div>
  
</template>

<script>


import Navbar from './Navbar.vue';
import Login from './loginComponent.vue';



export default {

  components:{
    appNavbar: Navbar,
    appLogin: Login
    
  }

}
</script>

<style lang="sass" >
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
  
html,body
  overflow-x: hidden
  font-size: 16px
  min-width: 500px
  background-color: $color_blue
// --------------------
</style>