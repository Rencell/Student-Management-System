<script setup>
import { inject } from "vue";

const alertDialog = inject("alertDialog")

const handleClick = () => {
  alertDialog.open.value = !alertDialog.open.value;
};
</script>

<template>
  <div @click="handleClick">
    <slot />
  </div>
</template>