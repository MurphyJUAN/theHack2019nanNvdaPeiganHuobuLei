
<template>
<div class="rankpage">
   
    <div class="container">
        <div class="bar">
            <v-select class='col-lg-3 col-md-6 col-sm-6' style='margin-bottom: 30px' :options="['涼度','甜度','互動程度','無聊度','用功時間','資源滿意度']"></v-select>
            <tr class="items">
                <td class="item item0">課程</td>
                <td class="item item0">教師</td>
                <td class="item item1">涼度</td>
                <td class="item item2">甜度</td>
                <td class="item item3">互動程度</td>
                <td class="item item4">無聊度</td>
                <td class="item item5">用功時間</td>
                <td class="item item6">資源滿意度</td>
            </tr>
            <tr class="course" v-for="(item, idx) in courses" :key="idx" 
            data-toggle="modal" data-target="#exampleModalCenter"
            @click="window(idx)"
            >
                
                <td class="line course_name"  >{{item.name}}</td>
                <td class="line course_name"  >{{item.teacher}}</td>
                <td class="line comfort" :class="[item.comfort >='4.0'  ? 'red' : 'black']">    {{item.comfort}}</td>
                <td class="line sweet" :class="[item.sweet >='4.0' ? 'red' : 'black']"> {{item.sweet}}</td>
                <td class="line interactor" :class="[item.interact >='4.0' ? 'red' : 'black']">  {{item.interact}}</td>
                <td class="line boring" :class="[item.boring >='4.0' ? 'red' : 'black']"> {{item.boring}}</td>
                <td class="line course_time" :class="[item.time >='4.0' ? 'red' : 'black']"> {{item.time}}</td>
                <td class="line source" :class="[item.source >='4.0' ? 'red' : 'black']"> {{item.source}}</td>  
            </tr>
            
        </div>
        

        <!-- Modal -->
        <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title" id="exampleModalLongTitle">{{courses[idx].name}}</h1>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="sub-title">ＴＡ們修過這堂課</div>
            <div class="modal-body">
                <nav>
                    <div class="nav nav-tabs" id="nav-tab" role="tablist">
                        <a class="nav-item nav-link active" id="nav-rank-tab" data-toggle="tab" href="#nav-rank" role="tab" aria-controls="nav-rank" aria-selected="true">為課程評分</a>
                        <a class="nav-item nav-link" id="nav-home-tab" data-toggle="tab" href="#nav-home" role="tab" aria-controls="nav-home" aria-selected="false">查看評分</a>
                        <a class="nav-item nav-link" id="nav-profile-tab" data-toggle="tab" href="#nav-profile" role="tab" aria-controls="nav-profile" aria-selected="false">課程說明</a>
                    </div>
                </nav>
                <div class="tab-content" id="nav-tabContent">
                    <div class="tab-pane fade show active" id="nav-rank" role="tabpanel" aria-labelledby="nav-rank-tab">
                        <div class="scorepage">
  <div class="container">
    <div class="row">
      <div class="intro">
        <p class="sub)intro">如果之後對「{{courses[idx].name}}」有新評價，您隨時可以回來修改評分。</p>
      </div>
    </div>

    <div class="row ">
      <form action="">
        <div class="form-group col-12">
          <div class="write-rating-box">
            <div class="rating-label">涼度</div>
            <star-rating :star-size="25"></star-rating>
          </div>
          <div class="write-rating-box">
            <div class="rating-label">甜度</div>
            <star-rating :star-size="25"></star-rating>
          </div>
          <div class="write-rating-box">
            <div class="rating-label">互動程度</div>
            <star-rating :star-size="25"></star-rating>
          </div>
          <div class="write-rating-box">
            <div class="rating-label">無聊度</div>
            <star-rating :star-size="25"></star-rating>
          </div>
          <div class="write-rating-box">
            <div class="rating-label">用功時間</div>
            <star-rating :star-size="25"></star-rating>
          </div>
          <div class="write-rating-box">
            <div class="rating-label">資源滿意度</div>
            <star-rating :star-size="25"></star-rating>
          </div>
          <button type="submit" class="btn btn-primary btn-lg">送出評分</button>
        </div>
      </form>
    </div>

    

    

  
    
    
  </div>
</div>
                    </div>
                    <div class="tab-pane fade" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab">
                        <div class="score" >
                            <div class="order" >
                                <h5 >涼度</h5>
                                <h5 class="w_score" :class="[courses[idx].comfort >='4.0'  ? 'red' : 'black']">{{courses[idx].comfort}}</h5>
                            </div>
                            <div class="order" >
                                <h5 class="w_text "> 甜度</h5>
                                <h5 class="w_text w_score" :class="[courses[idx].sweet >='4.0'  ? 'red' : 'black']">{{courses[idx].sweet}}</h5>
                            </div>
                            <div class="order">
                                <h5 class="w_text">互動程度</h5>
                                <h5 class="w_text w_score" :class="[courses[idx].interact >='4.0'  ? 'red' : 'black']">{{courses[idx].interact}}</h5>
                            </div>
                            <div class="order">
                                <h5 class="w_text ">無聊度</h5>
                                <h5 class="w_text w_score" :class="[courses[idx].boring >='4.0'  ? 'red' : 'black']">{{courses[idx].boring}}</h5>
                            </div>
                            <div class="order">
                                <h5 class="w_text ">用功時間</h5>
                                <h5 class="w_text w_score" :class="[courses[idx].time >='4.0'  ? 'red' : 'black']">{{courses[idx].time}}</h5>
                            </div>
                            <div class="order">
                                <h5 class="w_text ">資源滿意度</h5>
                                <h5 class="w_text w_score" :class="[courses[idx].source >='4.0'  ? 'red' : 'black']">{{courses[idx].source}}</h5>
                            </div>
                            <div class="total_rank">{{courses[idx].total_rank}}個人共同評分</div>
                        </div>
                    </div>
                    <div class="tab-pane fade" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab">
                        <p v-html="courses[idx].content"></p>
                        
                    </div>
                    
                </div>

                
                 
                <div class="comment">
                    <h2 data-toggle="tooltip" data-placement="left" title="我們支援Markdown語法！">留言區</h2>
                    <form  v-on:submit.prevent='submit' >
                        <div class="form-group">
                            <textarea required="required" placeholder="在想些什麼？" v-model='input' class="form-control" ></textarea>
                            
                        </div>
                        <button class="btn btn-info" >送出</button>
                        <br />
                        <br />
                        <legend></legend>
				    </form>
                    <div v-if='courses[idx].total_comment == 0' >
							<div class="alert alert-info" >
								還沒有任何留言 ＴＴ
							</div>
					</div>
                    <div class="list-group" >
							<div class="list-group-item" v-for= "(comment,idx) in courses[idx].comments " :key="idx" v-if="idx<=9">
								<strong>{{student_id}}   {{name}}</strong> 
                                <p class="content"><vue-markdown :linkify="true" :emoji="true"
                                table-class="table table-striped" >{{comment.comment}}</vue-markdown></p>
								<div class="like">
									<img class="like_img" src="../static/thumb-up.svg" alt="" v-on:click='like(idx)' v-if="comment.islike==false">
                                    <img class="like_img" src="../static/thumb-up-red.svg" alt="" v-on:click='like(idx)' v-if="comment.islike==true">
									<div class="like_text" v-if="comment.total_likes>0"> {{comment.total_likes}}</div> 
                                </div>
                                
                                <div class="dislike">
                                    <img class="dislike_img" src="../static/thumb-down.svg" alt="" v-on:click='dislike(idx)' v-if="comment.isdislike==false">
                                    <img class="dislike_img" src="../static/thumb-down-blue.svg" alt="" v-on:click='dislike(idx)' v-if="comment.isdislike==true">
									<div class="dislike_text" v-if="comment.total_dislikes>0">{{comment.total_dislikes}}</div>   
                                    
								</div>
                                
                                
								
							</div>
						</div>
                </div>
            </div>
            
            
            <div class="modal-footer">
                
                
            </div>
            </div>
        </div>
        </div> 




    </div>

    
</div>      

  
</template>

<script>
import StarRating from 'vue-star-rating'
import VueMarkdown from 'vue-markdown'
import {eventBus} from '../main'
import Vue from 'vue'
import vSelect from 'vue-select'
Vue.component('v-select', vSelect)

// $(function () {
//   $('[data-toggle="tooltip"]').tooltip()
// })

export default {
    data: function(){
        return{
            name: "昂昂同學",
            student_id: "#12345",
            idx:1,
            input: "",
            courses:[
                {
                    name: '演算法',
                    teacher: '王叉叉',
                    comfort: '3.5',
                    sweet: '0.0',
                    interact: '4.0',
                    boring: '5.0',
                    time: '5.0',
                    source: '3.0',
                    total_rank: '150',
                    comments: [],
                    total_comment: 0,
                    content:'This course introduces basic concepts of data representation and manipulation.<br/>We will teach how to solve a given problem efficiently and effectively ',
                    
                },
                {
                    name: '計算機網路概論',
                    teacher: '李大大',
                    comfort: '4.5',
                    sweet: '0.0',
                    interact: '2.0',
                    boring: '5.0',
                    time: '5.0',
                    source: '3.0',
                    total_rank: '20',
                    comments: [],
                    total_comment: 1,
                    content:"一、課程目的<br/>本課程期學生對於計算機網路設計原理有基本瞭解。<br/>二、課程大綱<br/>介紹計算機網路與網際網路，資料鏈結層與區域網路，網路層通訊協定，傳輸層通訊協定，網路應用層。",
                }
            ]
        };
    },
    
    components:{
        VueMarkdown,
        StarRating
    },
    methods:{
        window: function(idx){
            this.idx=idx;
        },
        goSubmit(){
            location. reload()
        },
        getSingleTon: function (comment) {
			return function () {
				return {
					comment,total_likes: 0, total_dislikes: 0,islike: false, isdislike: false
				}
			}
        },
        submit() {
			var comment = this.getSingleTon(this.input);
			var old = this.courses[this.idx].comments;
			var newc = [...old,comment()];
			this.courses[this.idx].comments = newc;
			this.input = "";
			this.courses[this.idx].total_comment = this.courses[this.idx].comments.length;
        },
        like(index) {
            if(this.courses[this.idx].comments[index].islike==false){
                this.courses[this.idx].comments[index].total_likes = this.courses[this.idx].comments[index].total_likes + 1
                this.courses[this.idx].comments[index].islike=true
            }else{
                this.courses[this.idx].comments[index].islike=false
                this.courses[this.idx].comments[index].total_likes--
            }
        },
        dislike(index) {
            if(this.courses[this.idx].comments[index].isdislike==false){
                this.courses[this.idx].comments[index].total_dislikes = this.courses[this.idx].comments[index].total_dislikes + 1
                this.courses[this.idx].comments[index].isdislike=true
            }else{
                this.courses[this.idx].comments[index].isdislike=false
                this.courses[this.idx].comments[index].total_dislikes--
            }
            
        },
        
        

    }
     
  

}
</script>

<style lang="sass" scope >
@import "vue-select/src/scss/vue-select.scss"
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

@keyframes rotate
  0%
    transform: rotate(0deg)
  20%
    transform: rotate(20deg)
  50%
    transform: rotate(0deg)
  70%
    transform: rotate(-20deg)
  100%
    transform: rotate(0deg)
  
html,body
  overflow-x: hidden
  font-size: 16px
  min-width: 500px
  padding-right: 0 !important




  
// -------------------

.red
    color: $color_red
.black
    color: black

.rankpage
    // background: $color_white
    background: white
.tr,.td
    display: block
    color: $color_blue
.tr
    border: solid 1px
    &:hover
        background-color: $color_red
.bar
    padding: 40px 0px 40px 0px




    
.item0
    padding: 0px 100px 0px 100px
.item1,.item2,.item3,.item4,.item5,.item6
    padding: 0px 45px 0px 45px
    //border: solid 1px

.item
    border-bottom: solid  1px rgba(0,0,0,.1)
    text-align: center
    font-weight: bold
    padding: 0px 0px 15px 0px
    

.bar_hr
    margin-top: 20px
    margin-bottom: 0px
    padding: 0
    color: black
    

.course
    padding: 0
    margin-top: 0px
    cursor: pointer
    transition-duration: 0.5s
     
    &:hover
        background-color: $color_gray
.course_name
    padding: 0px 5px 0px 5px
    width: 233px
    text-align: center

.comfort,.sweet
    width: 125px
.interactor,.course_time
    width: 155px
.boring
    width: 142px
.source
    width: 170px
.comfort,.sweet,.interactor,.boring,.course_time,.source
    text-align: center
    padding: 5px 0px 5px 0px
    &::after
        content: "★"
.line
    border-bottom: solid 1px rgba(0,0,0,.1)
.modal
    max-height: 800px
    overflow: hidden

    
.modal-body
    max-height: 500px
    margin-top: -35px
    overflow-y: auto
    
.modal-dialog
    overflow-y: initial !important
.score
    display: flex
    flex-wrap: wrap
    width: 100%
    //border: solid 1px
    align-content: center
    padding: 10px
    
    
    
.order
    display: flex
    width: 50%
    


.w_score
    display: flex
    justify-content: flex-end
    flex: 1
    padding: 0px 15px 0px 0px
    &::after
        content: "★"

.tab-pane
    padding: 15px 0px 0px 0px

.grade
    width: 100%

.modal-title
    margin-bottom: 30px !important
    
.tab-content
    margin-bottom: 30px
    
.nav-item
    color: rgba(22, 115, 143, 1)

.sub-title
    display: flex
    flex: 1
    top: -35px
    margin-left: 15px
    font-size: 15px
    color: $color_gray
    justify-content: flex-start
    
    &::before
        content: " "
        display: block
        width: 6px
        height: 25px
        background-color: $color_yellow

.total_rank
    color: $color_red
    font-size: bold
    margin-top: 10px
    display: flex
    flex: 1
    justify-content: flex-end
    &::before
        content: "這堂課由"
        color: $color_blue

.fix
    width: 15%
    height: 15%
    position: fixed
    right: 10px
    bottom: 50px
    z-index: 10
    cursor: pointer
    
    &:hover
        animation: rotate 0.4s linear both

.like,.dislike
    display: inline-block
    margin-right: 10px
    //border: solid 1px
    padding: 15px
    width: 100px
    
   
    
    

    

.like_text,.dislike_text
    display: inline-block
    color: $color_gray
    //border: solid 1px

.like_img,.dislike_img
    width: 30px
    height: 30px
    cursor: pointer
    display: inline-block
.content
    margin-top: 25px

.write-rating-box
  padding-top: 5px
  padding-bottom: 0px
  margin-bottom: 10px
  border-bottom: 1px solid #E0E0E0
  display: block
.rating-label,.rating
  display: inline-block
.rating-label
  width: 100px
  text-align: center
  vertical-align: middle
.rating
  vertical-align: middle

input[type=checkbox]
  margin-right: 10px
  margin-left: 10px

    




  






    


</style>