<script setup>
import sidebar from './partials/sidebar.vue';
import navigation from './partials/navigation.vue';
import { ref } from 'vue';

const openSheet = ref(false)

</script>

<template>
  
  <div class="flex flex-col min-h-screen">
      <navigation @open-sheet="openSheet = true"></navigation>
    
    <div class="flex h-full ">
        <sidebar v-model:open="openSheet"></sidebar>
        <div class="grow p-5 min-h-screen bg-background">
          <slot></slot>
        </div>
    </div>
  </div>

</template>

<style scoped>
  
</style>
