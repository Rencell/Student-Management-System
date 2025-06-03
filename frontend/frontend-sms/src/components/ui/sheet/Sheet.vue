<script setup>
import { provide, ref } from "vue";

const open = defineModel("open", { default: false });

const close = () => {
  open.value = false;
};

provide("sheet", {
  open,
  close,
});
</script>

<template>
  <slot />
</template>