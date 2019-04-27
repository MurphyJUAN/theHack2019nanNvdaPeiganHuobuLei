<template>
    <div>
      <form class='mobile-search-bar'>
        <div class="mobile-enter-teacher col-12">
          <input class='teacher-text' type="text" placeholder="輸入教師名稱" v-model="inputTeacher">
          <div class='mobile-cross' @click="removeTeacher()">X</div>
        </div>
        <div class="mobile-enter-class col-12">
          <input class='class-text' type="text" placeholder="輸入課程名稱" v-model="inputCourse">
          <div class='cross' @click="removeCourse()">X</div>
        </div>
        <div class="mobile-choose-department col-12" id="departmentContent">
          <div class='department-text' id="departmentText" @click="showDepartmentList()">{{inputDepartment}}</div>
          <ul class="departments" id = "departmentList" v-if="isDepartmentList"> 
            <div class='college-box' id='collegeBox'>
              <div class="college-title">學院</div>
              <li class="department-firstlayer" id='depFst' v-for="(item,idx) in all_colleges" :key="idx"> 
                  <div class="college" id="colleges" @click="showDetail(idx)">{{item.college}}</div>
              </li>
            </div>
            <div class='department-box' v-if="isDepartmentTitle" id='departmentBox'>
              <div class="department-title">系所</div>
              <ul class="department-secondelayer" id='depdet'>
                <div class="department-detail" @click="selectDepartment(target)" v-for="(target,idx) in all_colleges[detail].departments" :key="idx"
                >{{target}}
                </div>
              </ul>
            </div>
            <div class='choose-box' v-if="isChooseBox">
              <div class="choose-title" @click="selectChooseBox('選修')">選修</div>
              <div class="choose-title" @click="selectChooseBox('必修')">必修</div>
            </div>

          </ul>
          
        </div>
        <div class="mobile-choose-grade col-12" id='chooseGrade'>
          <div class='grade-text col-12' @click="showGradeList()">{{inputGrade}}
            <ul class="grade-layer" id='gradList' v-if="isGradeList">
                    <div class="grade-content" @click="selectGrade(grade), showGradeList()" v-for="(grade,idx) in grades" :key="idx">
                    {{grade}}</div>
            </ul>
          </div>
          
        </div>
        <div class="mobile-choose-classTime col-12">
          <div class='classTime-text' @click="showClassTimeList()">空堂塞課</div>
            <ul class="mobile-classTime-layer right" v-if="isClasstimeList">
          <table>
            <tbody>
              <tr>
                <td class="blank"></td>
                <td class="title">Mon</td>
                <td class="title">Tue</td>
                <td class="title">Wed</td>
                <td class="title">Thu</td>
                <td class="title">Fri</td>
              </tr>
              <tr>
                <td class="time">08:00</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in First" :key="idx"
                >
                {{item.name}}</td>
              </tr>
              <tr>
                <td class="time">09:00</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Second" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">10:10</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Third" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">11:10</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Fourth" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">12:10</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Nth" :key="idx"  
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">13:20</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Fifth" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">14:20</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Sixth" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">15:30</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Seventh" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">16:30</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Eigth" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">17:30</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Ninth" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              </tbody>
          </table>
        </ul>
          
          
        </div>
        <button type="button" size="lg"  class="mobile-ready-search btn btn-warning" @click="goRank">搜索</button>
      </form>
      <!-- ------------------------Below is Desktop------------------ -->
      <form class='search-bar'>
        <div class="enter-teacher">
          <input class='teacher-text' type="text" placeholder="輸入教師名稱" v-model="inputTeacher">
          <div class='cross' @click="removeTeacher()">X</div>
        </div>
        <div class="enter-class">
          <input class='class-text' type="text" placeholder="輸入課程名稱" v-model="inputCourse">
          <div class='cross' @click="removeCourse()">X</div>
        </div>
        <div class="choose-department" id="departmentContent">
          <div class='department-text' id="departmentText" @click="showDepartmentList()">{{inputDepartment}}</div>
          <ul class="departments" id = "departmentList" v-if="isDepartmentList"> 
            <div class='college-box' id='collegeBox'>
              <div class="college-title">學院</div>
              <li class="department-firstlayer" id='depFst' v-for="(item,idx) in all_colleges" :key="idx"> 
                  <div class="college" id="colleges" @click="showDetail(idx)">{{item.college}}</div>
              </li>
            </div>
            <div class='department-box' v-if="isDepartmentTitle" id='departmentBox'>
              <div class="department-title">系所</div>
              <ul class="department-secondelayer" id='depdet'>
                <div class="department-detail" @click="selectDepartment(target)" v-for="(target,idx) in all_colleges[detail].departments" :key="idx"
                >{{target}}
                </div>
              </ul>
            </div>
            <div class='choose-box' v-if="isChooseBox">
              <div class="choose-title" @click="selectChooseBox('選修')">選修</div>
              <div class="choose-title" @click="selectChooseBox('必修')">必修</div>
            </div>

          </ul>
          
        </div>
        <div class="choose-grade" id='chooseGrade'>
          <div class='grade-text' @click="showGradeList()">{{inputGrade}}
            <ul class="grade-layer" id='gradList' v-if="isGradeList">
                    <div class="grade-content" @click="selectGrade(grade), showGradeList()" v-for="(grade,idx) in grades" :key="idx">
                    {{grade}}</div>
            </ul>
          </div>
          
        </div>
        <div class="choose-classTime">
          <div class='classTime-text' @click="showClassTimeList()">空堂塞課</div>
            <ul class="classTime-layer right" v-if="isClasstimeList">
          <table>
            <tbody>
              <tr>
                <td class="blank"></td>
                <td class="title">Mon</td>
                <td class="title">Tue</td>
                <td class="title">Wed</td>
                <td class="title">Thu</td>
                <td class="title">Fri</td>
              </tr>
              <tr>
                <td class="time">08:00</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in First" :key="idx"
                >
                {{item.name}}</td>
              </tr>
              <tr>
                <td class="time">09:00</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Second" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">10:10</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Third" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">11:10</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Fourth" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">12:10</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Nth" :key="idx"  
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">13:20</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Fifth" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">14:20</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Sixth" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">15:30</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Seventh" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">16:30</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Eigth" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              <tr>
                <td class="time">17:30</td>
                <td class="drop" @click="item.click=!item.click" :class="item.click? 'isClick':'unClick'" v-for="(item,idx) in Ninth" :key="idx"
                
                >{{item.name}}</td>
              </tr>
              </tbody>
          </table>
        </ul>
          
          
        </div>
        <div class="ready-search">
          <button type="button" class="btn btn-warning" @click="goRank">搜索</button>
        </div>
      </form>
      
         
    </div>
</template>

<script>
  import Vue from 'vue'
  import vSelect from 'vue-select'
  Vue.component('v-select', vSelect)
  export default {
  data: function(){
  return{
  placeholder:'您想學習什麼課程？',
  selectedTags:[],
  isDepartmentList: false,
  isDepartmentTitle: false,
  isChooseBox: false,
  isGradeList: false,
  isClasstimeList: false,
  detail: 0,
  inputTeacher: "",
  inputCourse: "",
  inputDepartment: "必選修",
  inputGrade: "選擇年級",
  First:[
  {name:"M1", click: false},
  {name:"T1", click: false},
  {name:"W1", click: false},
  {name:"R1", click: false},
  {name:"F1", click: false}
  ],
  Second:[
  {name:"M2", click: false},
  {name:"T2", click: false},
  {name:"W2", click: false},
  {name:"R2", click: false},
  {name:"F2", click: false}
  ],
  Third:[
  {name:"M3", click: false},
  {name:"T3", click: false},
  {name:"W3", click: false},
  {name:"R3", click: false},
  {name:"F3", click: false}
  ],
  Fourth:[
  {name:"M4", click: false},
  {name:"T4", click: false},
  {name:"W4", click: false},
  {name:"R4", click: false},
  {name:"F4", click: false}
  ],
  Nth:[
  {name:"Mn", click: false},
  {name:"Tn", click: false},
  {name:"Wn", click: false},
  {name:"Rn", click: false},
  {name:"Fn", click: false}
  ],
  Fifth:[
  {name:"M5", click: false},
  {name:"T5", click: false},
  {name:"W5", click: false},
  {name:"R5", click: false},
  {name:"F5", click: false}
  ],
  Sixth:[
  {name:"M6", click: false},
  {name:"T6", click: false},
  {name:"W6", click: false},
  {name:"R6", click: false},
  {name:"F6", click: false}
  ],
  Seventh:[
  {name:"M7", click: false},
  {name:"T7", click: false},
  {name:"W7", click: false},
  {name:"R7", click: false},
  {name:"F7", click: false}
  ],
  Eigth:[
  {name:"M8", click: false},
  {name:"T8", click: false},
  {name:"W8", click: false},
  {name:"R8", click: false},
  {name:"F8", click: false}
  ],
  Ninth:[
  {name:"M9", click: false},
  {name:"T9", click: false},
  {name:"W9", click: false},
  {name:"R9", click: false},
  {name:"F9", click: false}
  ],
  all_colleges: [
  {
  college: "",
  departments: [
  ]
  },
  {
  college: "電機資訊學院",
  departments: [
  "資訊工程學系",
  "電機工程學系",
  "電機資訊學院學士班",
  "通訊工程研究所",
  "電子工程研究所",
  "資訊系統與應用研究所",
  "光電工程研究所"
  ]
  },
  {
  college: "理學院",
  departments: [
  "數學系",
  "物理學系",
  "化學系",
  "理學院學士班",
  "統計學研究所",
  "天文研究所",
  "計算與建模科學研究所"
  ]
  },
  {
  college: "工學院",
  departments: [
  "化學工程學系",
  "動力機械工程學系",
  "材料科學工程學系",
  "工業工程與工程管理學系",
  "工學院學士班",
  "奈米工程與微系統研究所",
  "生物醫學工程研究所",
  "工工碩士在職專班"
  ]
  },
  {
  college: "原子科學院",
  departments: [
  "工程與系統科學系",
  "生醫工程與環境科學系",
  "原子科學院學士班",
  "核子工程與科學研究所",
  "分析與環境科學研究所"
  ]
  },
  {
  college: "人文社會學院",
  departments: [
  "中國文學系",
  "外國語文學系",
  "人文社會學院學士班",
  "歷史研究所",
  "語言學研究所",
  "人類學研究所",
  "社會學研究所",
  "哲學研究所",
  "台灣文學研究所",
  "華文文學研究所",
  "教師在職進修碩士班"
  ]
  },
  {
  college: "生命科學院",
  departments: [
  "生命科學系",
  "醫學科學系",
  "生命科學學士班",
  "分子與細胞生物研究所",
  "分子醫學研究所",
  "生物資訊與結構生物研究所",
  "生物科技研究所",
  "系統神經科學研究所"
  ]
  },
  {
  college: "科技管理學院",
  departments: [
  "計量財務金融學系",
  "經濟學系",
  "科技管理學院學士班",
  "科技管理研究所",
  "MBA",
  "科技法律研究所",
  "EMBA",
  "IMBA",
  "服務科學研究所",
  "MPM",
  "MFB"
  ]
  },
  {
  college: "竹師教育學院",
  departments: [
  "教育與學習科技學系",
  "幼兒教育學系",
  "特殊教育學系",
  "教育心理與諮商學系",
  "體育學系",
  "英語教學系",
  "環境與文化資源學系",
  "竹師教育學院學士班",
  "學習科學與科技研究所",
  "數理教育研究所",
  "台灣語言研究與教學研究所"
  ]
  },
  {
  college: "藝術學院",
  departments: ["音樂學系", "藝術與設計學系", "藝術學院學士班"]
  }
  ],
  grades: ["一年級", "二年級", "三年級", "四年級"]
  };
  },
  methods:{
  selectedTag:function(message){
  if(!this.selectedTags.includes(message)) {
  this.selectedTags.push(message);
  }else {
  this.selectedTags.splice(
  this.selectedTags.indexOf(message), 1);
  }
  },
  goRank(){
  this.$router.push({path:'/Rank'})
  },
  changePlaceholder(message){
  this.placeholder=message
  },
  showDepartmentList(){
  this.isDepartmentList = !this.isDepartmentList
  this.axios.get('https://api.coindesk.com/v1/bpi/currentprice.json').then((response)=>{
    console.log(response)
  }).catch((response)=>{
    console.log(response)  
})
  },

  showGradeList(){
    if(this.inputDepartment.match('研究所')){
      this.isGradeList = false;
      this.inputGrade = '無'
    }else {
      this.isGradeList = !this.isGradeList
    }
  },
  showClassTimeList(){
    this.isClasstimeList = !this.isClasstimeList
  },
  showDetail(idx){
    console.log('====',idx)
    this.detail = idx
    this.isDepartmentTitle = true
  },
  hideDetail(idx){
    console.log('====',idx)
    this.detail = 0
  },
  selectDepartment(target){
    this.inputDepartment = target
    this.isChooseBox = true
  },
  selectGrade(target){
    this.inputGrade = target
    this.isGradeList = false
  },
  selectChooseBox(target){
    this.isDepartmentList = !this.isDepartmentList
    this.detail = 0
    let str = this.inputDepartment + '．' + target
    this.inputDepartment = str
    this.isDepartmentTitle = !this.isDepartmentTitle
    this.isChooseBox = !this.isChooseBox
  },
  removeTeacher(){
    this.inputTeacher = ""
  },
  removeCourse(){
    this.inputCourse = ""
  }
  
  },
  mounted() { 
    document.addEventListener('click', (e) => {
       if (e.target.parentElement.id != 'depFst' && e.target.parentElement.id != 'depdet' && e.target.parentElement.id != 'departmentContent' && e.target.parentElement.id != 'collegeBox' && e.target.parentElement.id != 'departmentBox') {
         this.isDepartmentList = false 
         }
       if(e.target.parentElement.id != 'gradList' && e.target.parentElement.id != 'chooseGrade') {
         this.isGradeList = false 
         }
     })
}
  }

</script>

<style lang="sass" scope>
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
.mobile-search-bar
  width: 100%
  display: flex
  flex-direction: column
  background-color: transparent
  cursor: pointer
  margin-top: 30px
  @media screen and (min-width: 960px)
    display: none
  
.search-bar
  width: 100%
  display: inline-flex
  flex-direction: row
  background-color: $color_white
  cursor: pointer
  height: 50px
  border-radius: 5px
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 10px 0px
  margin-top: 30px
  @media screen and (max-width: 960px)
    display: none

input
  background: none
  border: none
  outline: none
  padding: none

::placeholder
  font-weight: bold

.mobile-enter-teacher,.mobile-enter-class,.mobile-choose-department,.mobile-choose-classTime,.mobile-choose-grade,.mobile-ready-search
  background-color: $color_white
  padding: 5px 15px
  line-height: 35px
  text-align: center
  margin-top: 5px
  border-radius: 5px
  display: inline-flex

.mobile-cross
  justify-content: flex-end

.enter-teacher,.enter-class,.choose-department,.choose-classTime,.choose-grade
  padding: 5px 15px
  line-height: 35px
  text-align: center
  flex: 5
  border-right: solid 1px $color_gray
.choose-department
  flex: 9
.enter-teacher,.enter-class,.choose-department,.choose-classTime,.choose-grade
  display: inline-flex
  justify-content: space-between
  
.cross
  justify-content: flex-end

.teacher-text,.class-text,.department-text,.classTime-text,.grade-text
  color: $color_blue
  font-weight: bold
  width: 100%

.choose-grade
  flex: 3
.ready-search
  padding: 5px 15px
  line-height: 35px
  text-align: center
  border: none
  flex: 3

.departments
  position: absolute
  display: inline-flex
  flex-direction: row
  justify-content: space-between
  top: 51px
  left: 0px
  overflow-y: auto
  overflow-x: hidden
  white-space: normal
  max-height: calc(100vh - 100px)
  // width: 511px
  // height: 480px
  z-index: 10
  background-color: $color_white
  list-style: none
  padding: 20px
  border-radius: 5px
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 10px 0px
  .department-firstlayer,.college-title
    text-align: left
  .department-secondelayer
    text-align: left
    padding: 0px

.college,.department-detail,.grade-content
  &:hover
    color: $color_orange

.college-title, .choose-title
  font-weight: bold

.department-title
  position: absolute
  font-weight: bold
  top: 0px

  

.grade-layer
  position: absolute
  display: inline-flex
  flex-direction: column
  justify-content: flex-start
  top: 47px
  left: -15px
  width: 127.33px
  height: 180px
  z-index: 10
  background-color: $color_white
  list-style: none
  padding: 20px
  border-radius: 5px
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 10px 0px


.classTime-layer
  z-index: 10
  top: 51px
  left: -70px

.mobile-classTime-layer
  z-index: 10
  top: 51px
  right: 0px







.isClick
    background-color: $color_orange
.unClick
    background-color: $color_white



.right
  position: absolute
  transform: translate( -10%,0)
  color: $color_gray
  background-color: $color_white
  margin: 0
  padding: 20px
  border-radius: 5px
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 10px 0px
td.title , td.blank , td.time, td.drop
  border: solid 0.5px $color_gray
  padding: 10px 15px 10px 15px
  font-weight: bold
tr:hover>td.time
  color: $color_red
td.drop
  color: $color_white
  // &:hover
  //   background-color: $color_brown
.highlight
  background-color: $color_brown

.college-box, .choose-box
  width: 100px
.department-box
  width: 220px
  padding: 35px 0px 20px 30px
        
        
    



</style>