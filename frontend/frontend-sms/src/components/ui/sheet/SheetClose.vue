<script setup>
import { inject } from "vue";

const sheet = inject("sheet")

const handleClick = () => {
  sheet?.close();
};
</script>

<template>
  <div @click="handleClick">
    <slot />
  </div>
</template>