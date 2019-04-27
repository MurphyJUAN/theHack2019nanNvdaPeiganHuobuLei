<template>
<div class="jumbotrom" id="header_index">
  <div class="container">
    <h1 class="header_slo">隨著需求學習</h1>
    <appSearch></appSearch>
    
  </div>
</div>
</template>

<script>
import searchBar from './searchBar.vue';
export default {
    components:{
    appSearch: searchBar
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
  
html,body
  overflow-x: hidden
  font-size: 16px
  min-width: 500px
// --------------------

.jumbotrom
  
  position: relative
  background-color: $color_blue
  padding: 100px  0px 200px 0px
  @media screen and (max-width: 960px)
    padding: 100px  0px 100px 0px
  
  
  .header_slo
      color: $color_white
      padding: 0px 0px 30px 20px
      &::before
        content: " "
        display: block
        position: absolute
        left: 5px
        width: 5px
        height: 50px
        background-color: $color_orange
    

</style>