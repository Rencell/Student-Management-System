<script setup>
import { inject } from "vue";

const sheet = inject("sheet")

const handleClick = () => {
  sheet.open.value = !sheet.open.value;
};
</script>

<template>
  <div @click="handleClick">
    <slot />
  </div>
</template>