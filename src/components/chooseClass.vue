<template>
<section class="choose_generalclass" id="choose_generalclass">
  <div class="container">
    <h1 class="section_slo">探索有趣的</h1>
    <h1 class="section_slo2">通識</h1>
    <div class="outter">
      <div class="choose_class col-lg-3 col-md-3 col-sm-12">
        <div class="outer_icon sci"></div>
        <div class="text_pannel">
          <div class="span">自然科學領域</div>
        </div>
      </div>
      <div class="choose_class col-lg-3 col-md-3 col-sm-12">
        <div class="outer_icon soc"></div>
        <div class="text_pannel">
          <div class="span">社會科學領域</div>
        </div>
      </div>
      <div class="choose_class col-lg-3 col-md-3 col-sm-12">
        <div class="outer_icon hum"></div>
        <div class="text_pannel">
          <div class="span">人文學領域</div>
        </div>
      </div>
    </div>
  </div>
</section>
  
</template>

<script>

export default {


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

section.choose_generalclass
  position: relative
  background-color: $color_white
  padding: 100px  0px 100px 0px
  .section_slo
    &::after
      content: "選修"
      color: $color_red
      margin-left: 5px
      font-weight: bold


.choose_class
  
  //margin: 0
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 10px 0px
  border-color: rgba(0, 0, 0, 0.1)
  background-color: white
  border-radius: 3px
  cursor: pointer
  //border: solid 1px 
  width: calc(100% / 3 - 80px)
  margin-right: 10px
  height: 72px
  display: inline-block
  padding: 0px
  
  &:hover > .outer_icon
      background-size: auto 140%
      transition-duration: 0.5s
  .outer_icon
    display: inline-block
    width: 96px
    height: 72px
    //border: solid 1px
    background-size: cover
    background-position: 50% 50%
    background-repeat: no-repeat
    background-size: auto 100%
    padding: 0
    margin: 0
    
    &.sci
      background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8dc5zEEU8amxZ4GneIBKyg7MfXi1JZlVxxQ1isBf0lzJFUoKt2Q)
    &.soc
      background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrKSwRHKEMk5hg7nzm48mZSQgz3v503Cx7rBpRiw_CUR0uCsL-)
    &.hum
      background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHRKwB5FEs2NigBNdKqhYbrUSFgvNbtvPUaYq4AH4sEbkxL0GtKA)
  .text_pannel
    display: inline-block
    position: absolute
    top: calc(100% /2)
    transform: translate(0%,-50%)
    padding: 0px 10px
    font-weight: bold
    .span
      margin-top: -10px
      border: none
      background-color: transparent
      width: auto
      
    

</style>