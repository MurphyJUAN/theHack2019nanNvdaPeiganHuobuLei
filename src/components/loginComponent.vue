<template>
  <div class='container'>
    <div class='login'>
      <div class='login-box'>
            <div class='loggin-pannel'>
              <button type="button" class="btn btn-danger" style='width: 100%'>
                <div class='icon'>
                  <img src='../static/googleicon.png'>
                </div>
                <div class='text'>
                  使用 Google 帳號登入
                </div>
              </button>
            </div>
            <div class='loggin-pannel'>
              <button type="button" class="btn btn-info" style='width: 100%'>
                <div class='icon'>
                  <img src='../static/yahooicon.png'>
                </div>
                <div class='text'>
                  使用 Yahoo 帳號登入
                </div>
              </button>
            </div>

      </div>

    </div>
  </div>


</template>

<script>
import { eventBus } from '../main'
  export default{
    data: function(){
        return{
            coursesname : this.$route.query.name
        };
    },
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
  background-color: $color_blue
// --------------------

.login
  display: flex
  justify-content: center
  align-items: center
  color: $color_white

.login-box
  margin-top: 25%
  transform: translateY(-50%)

.loggin-pannel
  margin-top: 10px

img
  width: 32px
  height: 32px
.icon
  display: inline-block
  padding: 0px 10px 0px 10px
.text
  display: inline-block
  padding: 0px 20px 0px 20px






    

</style>