<script setup>
import sidebar from './partials/sidebar.vue';
import navigation from './partials/navigation.vue';
</script>

<template>
  
  <div class="flex flex-col min-h-screen">
      <navigation></navigation>
    
    <div class="flex h-full ">
        <sidebar></sidebar>
        <div class="grow p-5 min-h-screen bg-background">
          <slot></slot>
        </div>
    </div>
  </div>

</template>

<style scoped>
  
</style>
