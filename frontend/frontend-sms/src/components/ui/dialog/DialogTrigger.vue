<script setup>
import { inject } from "vue";

const dialog = inject("dialog");

const handleClick = () => {
  dialog.open.value = !dialog.open.value;
};
</script>

<template>
  <div @click="handleClick">
    <slot />
  </div>
</template>