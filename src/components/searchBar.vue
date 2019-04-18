<template>
    <div>
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
                  <div class="college-title">學院</div>
                  <li class="department-firstlayer" v-for="(item,idx) in all_colleges" :key="idx"> 
                      <div class="college" id="colleges" @click="showDetail(idx)">{{item.college}}</div>
                  </li>
                  <div class="department-title">系所</div>
                  <ul class="department-secondelayer">
                    <div class="department-detail" @click="selectDepartment(target)" v-for="(target,idx) in all_colleges[detail].departments" :key="idx"
                    >{{target}}</div>
                  </ul>
                  
                  
              </ul>
          
        </div>
        <div class="choose-grade">
          <div class='grade-text' @click="showGradeList()">{{inputGrade}}
            <ul class="grade-layer" v-if="isGradeList">
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


  export default {
    
  data: function(){
  return{
  placeholder:'您想學習什麼課程？',
  selectedTags:[],
  isDepartmentList: false,
  isGradeList: false,
  isClasstimeList: false,
  detail: 0,
  inputTeacher: "",
  inputCourse: "",
  inputDepartment: "選擇學院與系所",
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
  "全部",
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
  "全部",
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
  "全部",
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
  "全部",
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
  "全部",
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
  "全部",
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
  "全部",
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
  "全部",
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
    this.isGradeList = !this.isGradeList
  },
  showClassTimeList(){
    this.isClasstimeList = !this.isClasstimeList
  },
  showDetail(idx){
    console.log('====',idx)
    this.detail = idx
  },
  hideDetail(idx){
    console.log('====',idx)
    this.detail = 0
  },
  selectDepartment(target){
    this.inputDepartment = target
    this.isDepartmentList = !this.isDepartmentList
  },
  selectGrade(target){
    this.inputGrade = target
    this.isGradeList = false
  },
  removeTeacher(){
    this.inputTeacher = ""
  },
  removeCourse(){
    this.inputCourse = ""
  }
  
  },
  // mounted() { 
  //   document.addEventListener('click', (e) => {
  //      if (e.target.parentElement.id != 'departmentContent' && e.target.parentElement.id != 'departmentList') this.isDepartmentList = false }
  //      ) }

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

input
  background: none
  border: none
  outline: none
  padding: none

::placeholder
  font-weight: bold

.enter-teacher,.enter-class,.choose-department,.choose-classTime,.choose-grade,.ready-search
  border-right: solid 1px $color_gray
  padding: 5px 15px
  line-height: 35px
  text-align: center
  flex: 6
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
  border: none
  flex: 2

.departments
  position: absolute
  display: inline-flex
  flex-direction: column
  justify-content: flex-start
  top: 51px
  left: 0px
  width: 511px
  height: 480px
  z-index: 10
  background-color: $color_white
  list-style: none
  padding: 20px
  border-radius: 5px
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 10px 0px
  .department-firstlayer,.college-title
    text-align: left
  .department-secondelayer
    position: absolute
    top: 55px
    right: 20px
    text-align: right

.college,.department-detail,.grade-content
  &:hover
    color: $color_orange

.college-title
  font-weight: bold

.department-title
  position: absolute
  font-weight: bold
  top: 20px
  right: 20px

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
        
        
    



</style>