<template>
<div>
<section class="core_generalclass" id="core_generalclass">
    <div class="container">
        <h1 class="section_slo">尋找專業的</h1>
        <h1 class="section_slo2">通識</h1>
        <div class="class_box">
            <div class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-xs-12 class_window" v-for="(item, idx) in core_class" :key="idx">
                <img class="class_img" v-bind:src="item.img"/>
                <div class="number">{{ item.number }}</div>
                <div class="name">{{item.name}}</div>
            </div>
        </div>
    </div>
</section>
</div>
  
</template>

<script>
export default {
	data: function() {
		return {
    core_class: [
    {
      number: "向度一",
      name: "思維方式",
      img:
        require("../static/數理思維.jpg")
    },
    {
      number: "向度二",
      name: "生命之探索",
      img:
        require("../static/生命探索.png")
    },
    {
      number: "向度三",
      name: "藝術與文學",
      img:
        require("../static/藝術與文學.jpg")
    },
    {
      number: "向度四",
      name: "社會與文化脈動",
      img:
        require("../static/社會脈動.jpg")
    },
    {
      number: "向度五",
      name: "科學技術與社會",
      img:
        require("../static/科學技術.jpg")
    },
    {
      number: "向度六",
      name: "歷史分析",
      img:
        require("../static/歷史思維.jpg")
    }
  ]
        };
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

html,body
  overflow-x: hidden
  font-size: 16px
  min-width: 500px

//一些常用的mixin
@mixin ab_center
  position: absolute
  left: 50%
  top: 50%
  transform: translate(-50%,-50%)

@mixin size($w,$h)
  width: $w
  height: $h

section.core_generalclass
  position: relative
  background-color: $color_white
  padding: 100px  0px 0px 0px

  .class_box
    .class_window
      display: inline-block
      cursor: pointer
      padding: 0
      // max-width: 350px
      
    
      &::before
          content: ""
          display: block
          +size(100%,100%)

          position: absolute
          left: 0
          top: 0

          background-color: rgba(0,0,0,0.7)
          opacity: 0
          z-index: 5
          transition: 0.5s
      
      img
        width: 100%
        overflow: hidden
        height: 25vh
        
        @media screen and (max-width: 480px)
          height: 35vh
        
          

        // max-width: 350px
        
       
        
      .number,.name
        text-align: center
        position: absolute
        left: 50%
        top: 50%
        transform: translate(-50%,-50%)
        color: $color_white
        opacity: 0
        z-index: 7
        font-weight: bold
      .number
        margin-top: -18px
      .name
        margin-top: 18px
        
        font-size: 20px
      &:hover
        &:before,.number,.name
          opacity: 1
.section_slo
  color: $color_blue
  padding: 0px 0px 30px 20px
  display: inline-block
  &::before
    content: " "
    display: block
    position: absolute
    left: 5px
    width: 5px
    height: 50px
    background-color: $color_orange
  &::after
    content: "核心"
    color: $color_red
    margin-left: 5px
    font-weight: bold
.section_slo2
  color: $color_blue
  display: inline-block


</style>