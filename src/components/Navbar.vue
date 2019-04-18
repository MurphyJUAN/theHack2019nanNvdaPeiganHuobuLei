<template >

<div class="navbar">
    <div class="languages">
        <div class="lang" @click="languageBGC(1)" :class="{'hover': language==1}">繁</div>
        <div class="lang" @click="languageBGC(2)" :class="{'hover': language==2}">簡</div>
        <div class="lang" @click="languageBGC(3)" :class="{'hover': language==3}">英</div>
    </div>
    <div class='homepage' @click="goHome">
        RankCourses
    </div>
    <div class='login-icon' @click="goLogin">
            <div class='inside-login-icon'>
                <!-- <svg xmlns="http://www.w3.org/2000/svg" x="100px" y="0px"
                width="32" height="32"
                viewBox="0 0 192 192"
                style=" fill:#000000;"><g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path d="M0,192v-192h192v192z" fill="none"></path><g fill="#ffffff"><path d="M96,9.07617c-22.275,0 -44.55,8.47383 -61.5,25.42383c-33.9,33.9 -33.9,89.1 0,123c16.95,16.95 39.3,25.5 61.5,25.5c22.2,0 44.55,-8.55 61.5,-25.5c1.8,-1.8 1.8,-4.64883 0,-6.29883c-1.8,-1.8 -4.64883,-1.8 -6.29883,0c-30.45,30.45 -79.95,30.45 -110.25,0c-30.45,-30.45 -30.45234,-79.95234 -0.15234,-110.40234c30.45,-30.3 79.95234,-30.3 110.40234,0c1.8,1.8 4.64883,1.8 6.29883,0c1.8,-1.8 1.8,-4.64883 0,-6.29883c-16.95,-16.95 -39.225,-25.42383 -61.5,-25.42383zM121.44434,69c-1.14375,0 -2.26875,0.45059 -3.09375,1.35059l-22.5,22.5c-0.9,0.9 -1.35059,1.94941 -1.35059,3.14941c0,1.2 0.45059,2.24941 1.35059,3.14941l22.5,22.5c0.9,0.9 2.09941,1.35059 3.14941,1.35059c1.05,0 2.24941,-0.45059 3.14941,-1.35059c1.8,-1.8 1.8,-4.64883 0,-6.29883l-14.85059,-14.85059h46.20117c2.55,0 4.5,-1.95 4.5,-4.5c0,-2.55 -1.95,-4.5 -4.5,-4.5h-46.20117l14.85059,-14.85059c1.8,-1.8 1.8,-4.64883 0,-6.29883c-0.9,-0.9 -2.06133,-1.35059 -3.20508,-1.35059zM178.5,91.5c-2.48528,0 -4.5,2.01472 -4.5,4.5c0,2.48528 2.01472,4.5 4.5,4.5c2.48528,0 4.5,-2.01472 4.5,-4.5c0,-2.48528 -2.01472,-4.5 -4.5,-4.5z"></path></g></g></svg> -->
                登入
            </div>
        </div>

</div>
  
</template>

<script>


export default {
    data: function(){
        return{
            flag: 0,
            show: false,
            language: 1
        };
    },
    methods:{
        languageBGC(num){
            this.language=num
        },
        goLogin(){
            this.$router.push({path:'/Login'})
        },
        goHome(){
            this.$router.push({path:'/'})
        },
    }
    
  

}
</script>

<style lang="sass" scope >
@import url('<link href="https://fonts.googleapis.com/css?family=Quicksand:300,400,500,700" rel="stylesheet">')
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
  font-family: 'Quicksand', sans-serif,'微軟正黑體' 
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
  
// -------------------

.hover
    background-color: rgba(255, 255, 255, 0.35)


.navbar
   box-sizing: border-box
   max-height: 90px
   background-color: $color_blue
   display: flex
   flex-direction: row
   border-bottom: solid 1px rgba(255, 255, 255, 0.35)
   
.lang
    display: inline-block
    color: $color_white
    border-radius: 100%
    width: 32px
    height: 32px
    margin: 8px 2px
    text-align: center
    cursor: pointer
    font-size: 16px
    line-height: 30px
    transition-duration: 0.5s

    &:hover
        background-color: rgba(255, 255, 255, 0.35)

.login-icon
    display: flex
    justify-content: flex-end
    cursor: pointer
    color: $color_white

.homepage
    color: $color_orange
    font-weight: bold
    cursor: pointer
    transform: translateX(-50%)



// ---------------



    
    



        












    




    








</style>