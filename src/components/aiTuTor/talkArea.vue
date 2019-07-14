<template>
    <div class='talkArea'>
      <div class='w-100'>
        <div class='d-inline-flex w-100 p-2'>
          <div class='userTalkFrame w-100 p-3'>我想要改文章！</div>
          <div class='userAvastar p-2 ml-2'>User</div>
        </div>
      </div>
      <div class='w-100' @click="getSelectText">
        <div class='d-inline-flex w-100 p-2'>
          <div class='aiAvastar p-2 mr-2'>Tutor</div>
          <div class='aiTalkFrame w-100 p-3'>好呀！我幫你改！</div>
        </div>
      </div>
    </div>
</template>

<script>
  import userTalk from './userTalk.vue';
  import tutorTalk from './tutorTalk.vue';
  export default {
  data: function(){
    return{
      selectText: '',
    }
  },
  methods:{
    getSelectText(){
        var t='';
        if(window.getSelection){t=window.getSelection();}
        else if(document.getSelection){t=document.getSelection();}
        else if(window.document.selection){t=window.document.selection.createRange().text;}
        if(t!=''){
          this.selectText = t
        }
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

.talkArea
  height: 638px
  overflow: scroll
.userTalkFrame
  background-color: $color_gray
  border-radius: 30px
.userAvastar
  width: 50px
  height: 50px
  border-radius: 100%
  background-color: yellow
.aiTalkFrame
  background-color: $color_gray
  border-radius: 30px
.aiAvastar
  width: 50px
  height: 50px
  border-radius: 100%
  background-color: orange
</style>