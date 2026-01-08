<script setup>
import { inject } from "vue";
import Button from "../button/Button.vue";

const alertDialog = inject("alertDialog")

const handleClick = () => {
  alertDialog?.close();
};
</script>

<template>
  <Button variant="outline" @click="handleClick" v-bind="$attrs">
    <slot />
  </Button>
</template>