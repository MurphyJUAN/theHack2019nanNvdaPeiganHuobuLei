<template>
<div>
    <appNavbar></appNavbar>
    <appLogin></appLogin>
  
  
 
  
  <!-- <appTag></appTag> -->

</div>
  
</template>

<script>


import Navbar from './Navbar.vue';
import Login from './loginComponent.vue';



export default {

  components:{
    appNavbar: Navbar,
    appLogin: Login
    
  }

}
</script>

<style lang="sass" >
</style>