<template>
<div>
  <appNavbar></appNavbar>
  <appTop></appTop>
  <appCore></appCore>
  <appChoose></appChoose>
  
  <!-- <appTag></appTag> -->

</div>
  
</template>

<script>
import CoreClass from './coreClass.vue';
import ChooseClass from './chooseClass.vue';
import Top from './Top.vue';
import Navbar from './Navbar.vue';


export default {

  components:{
    appCore: CoreClass,
    appChoose: ChooseClass,
    appTop: Top,
    appNavbar: Navbar
    
  }

}
</script>

<style lang="sass" >
</style>