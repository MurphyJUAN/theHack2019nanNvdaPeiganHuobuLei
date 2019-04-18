<template>
<div>
  <appNavbar></appNavbar>
  <appTop></appTop>
  <appSort></appSort>
 
  
  <!-- <appTag></appTag> -->

</div>
  
</template>

<script>

import Top from './Top.vue';
import Navbar from './Navbar.vue';
import Sort from './sortList.vue';


export default {

  components:{
    appTop: Top,
    appNavbar: Navbar,
    appSort: Sort
    
  }

}
</script>

<style lang="sass" >
</style>