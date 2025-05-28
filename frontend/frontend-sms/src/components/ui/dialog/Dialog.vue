<script setup>
import { provide } from "vue";

const open = defineModel("open", { default: false });

const close = () => {
  open.value = false;
};

provide("dialog", {
  open,
  close,
});
</script>

<template>
  <slot />
</template>
