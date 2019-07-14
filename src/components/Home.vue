<template>
<div class='d-inline-flex w-100'>
  <div class='outerBox p-4'>
      <div class='conversationBox'>
        <div class='header w-100 p-2'>
          AI Tutor 
        </div>
        <div class='talkArea'>
          <div class='conversationBlock' v-for="(item, index) in msgGroup">
            
            <div class='w-100' v-if="item['user']">
              <div class='d-inline-flex w-100 p-2'>
                <div class='userTalkFrame w-100 p-3' @click="getSelectText">{{item.user}}</div>
                <div class='userAvastar p-2 ml-2'></div>
              </div>
            </div>
            <div class='w-100'  v-if="item['tutor']">
              <div class='d-inline-flex w-100 p-2'>
                <div class='aiAvastar p-2 mr-2'></div>
                <div class='aiTalkFrame w-100 p-3' @click="getSelectText">
                  <div v-for="(obj, index) in item.tutor">
                    '{{tmpUserMsg.substr(obj.offset,obj.length)}}'' could be replaced by
                    {{obj.replacements}}.<br>
                    For Example: {{obj.corrections}}<br>
                    Because you may make those mistakes: '{{obj.message}}',
                    we provide you some materials to learn:<br>
                    For Bonus, you may be inspired by those resources:
                  </div>
                </div>
              </div>
            </div>
            <div class='w-100' v-if="item['article']">
              <div class='d-inline-flex w-100 p-2'>
                <div class='aiAvastar p-2 mr-2'></div>
                <div class='aiTalkFrame w-100 p-3' @click="getSelectText">
                  {{item.article}}
                </div>
              </div>
            </div>
          </div>
        </div>
        <textarea class='talkBar w-100 p-2'
        type="text"
        v-model="userMsg" 
        @keyup.enter="userSendData()">
        </textarea>
      </div>
    </div>
<!-- ----------------------NoteBook------------------ -->
  <div class='noteBody p-5'>
    <div class='d-inline-flex'>
      <div class='w-100'>
        
        <h5>Title: <input :value="title"></h5>
        <div class='d-inline-flex'>
          <h5>Tags:</h5>
          <p v-for="(item, idx) in tags" class='tag px-2 mx-2'>{{item}}</p>
          <input v-model="addTag" @keyup.enter="sendTag()">
        </div>
        <!-- ----------NoteBook TiTle--------- -->
        <div class='mt-4' v-if="selectText.length">
          <h2>Qutoes</h2>
          <ul v-for="(item, index) in selectText" >
            <li class='quote px-3 w-100'>
              {{item}}
            </li>
            <input class='comment'>
          </ul>
        </div>
        <!-- ----------NoteBook Quote--------- -->
        <div class='mt-4 w-100'>
          <h2 class='w-100'>Screenshot Gallery</h2>
          <div class='gallery w-100 d-inline-flex'>
            <div class='card column'>
              <div id='photo'></div>
              <div class='screenDescription'>Test</div>
            </div>
          </div>
        </div>
        <!-- ----------NoteBook Gallery--------- -->
        <input type='button' id='but_screenshot' value='Take screenshot' @click='screenshot'><br/>
        <div class='mt-4'>
          <appToDo></appToDo>
        </div>
        <div class='d-inline-flex btn-set'>
          <button clss='form-control'>列印</button>
          <button>分享</button>
          <button>社群</button>
        </div>

      </div>
      

    </div>
  </div>   

</div>
  
</template>

<script>
import axios from 'axios'
import VueAxios from 'vue-axios'
import html2canvas from 'html2canvas';
import todo from './todo.vue';
export default {
  data: function(){
    return{
      title: '',
      addTag:'',
      tags: [],
      selectText: [],
      msgGroup: [],
      userMsg: [],
      tmpUserMsg: '',
      tutorMsg: [],
      htmlUrl: '',
      comment: [],
    }
  },
  components: {
    html2canvas,
    appToDo: todo,
  },
  methods:{
    screenshot(){
      html2canvas(document.body).then(function(canvas) {
    document.getElementById('photo').appendChild(canvas);
    });
    },
    sendTag(){
      this.tags.push(this.addTag)
      this.addTag = ''
    },
    toImage () {
      // 第一个参数是需要生成截图的元素,第二个是自己需要配置的参数,宽高等
      html2canvas(this.$refs.imageTofile, {
        backgroundColor: null,
　　　　 useCORS: false // 如果截图的内容里有图片,可能会有跨域的情况,加上这个参数,解决文件跨域问题
      }).then((canvas) => {
        let url = canvas.toDataURL('image/png')
        this.htmlUrl = url
        console.log(this.htmlUrl)
      })
    },
    getSelectText(){
        var t='';
        if(window.getSelection){t=window.getSelection();}
        else if(document.getSelection){t=document.getSelection();}
        else if(window.document.selection){t=window.document.selection.createRange().text;}
        if(t!=''){
          this.selectText.push(t.toString())
          console.log('hello', this.selectText)
          console.log(t)
        }
    },
    userSendData() {
      if(this.userMsg && !this.title){
        var Today=new Date();
        this.title = (Today.getMonth()+1) + " 月 " + Today.getDate() + " 日" + "的筆記"
      }
      var msgGroup = {};
      msgGroup['user'] = this.userMsg
      this.tmpUserMsg = this.userMsg
      this.msgGroup.push(msgGroup)

      this.axios.post('http://149.28.38.89:5000/checkGrammar', {
        text: this.userMsg,
      }).then((response) => {

        console.log(response)
        var msgGroup = {};
        msgGroup['tutor'] = response.data
        this.msgGroup.push(msgGroup)
        console.log(this.msgGroup)

        this.axios.post('http://149.28.38.89:5000/analyze', {
        text: this.tmpUserMsg,
      }).then((response) => {
        console.log(response.data[0].chose_para)
        var msgGroup = {};
        msgGroup['article'] = response.data[0].chose_para
        msgGroup['article_url'] = response.data[0].chose_url

        this.msgGroup.push(msgGroup)
        console.log(this.msgGroup)

      }).catch((response)=>{
        console.log(response)  
      })

      }).catch((response)=>{
        console.log(response)  
      })
      this.userMsg = ''
    }
    
  
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

input
  outline: none
  border: none
.tag
  background-color: purple
  opacity: 0.5
  color: white
  border-radius: 10px
.outerBox
  width: 40%
.conversationBox
  height: 758px
  overflow: hidden
.header 
  background-color: #6055AC
  text-align: center
  color: white
.talkArea
  background-color: rgb(242,236,212)
  height: 638px
  overflow: scroll
.userTalkFrame
  background-color: #EDCDB5
  border-radius: 30px
.userAvastar
  width: 50px
  height: 50px
  border-radius: 100%
  background-image: url('../static/user.jpg')
  background-position: center
  background-size: cover
  
.aiTalkFrame
  background-color: rgba(253,164,21,0.17)
  border-radius: 30px
.aiAvastar
  width: 50px
  height: 50px
  border-radius: 100%
  background-image: url('../static/ai.jpg')
  background-position: center
  background-size: cover
.talkBar
  height: 80px
  position: absolute
  bottom: 0px
// ------------------NoteBody------------

.noteBody
  width: 60%
  height: 758px
.quote
  background-color: $color_gray
.comment
  border: none
  outline: none
  color: gray
.screenDescription
  height: 30px
.btn-set
  position: absolute
  bottom: 0px
</style>