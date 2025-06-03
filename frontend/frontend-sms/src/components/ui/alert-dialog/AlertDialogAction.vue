<script setup>
import { inject, useAttrs } from 'vue'
import Button from "../button/Button.vue";
const alertDialog = inject('alertDialog')

const $attrs = useAttrs()

const handleClick = () => {
    alertDialog?.close()
  
}
</script>

<template>
  <Button variant="default" @click="handleClick" v-bind="$attrs">
    <slot />
  </Button>
</template>
