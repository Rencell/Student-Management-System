<script setup>
import { provide, ref } from 'vue'

const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])

const open = ref(false)

provide('select', {
  modelValue: props.modelValue,
  open,
  toggle: () => {
    open.value = !open.value
  },
  select: (value) => {
    emit('update:modelValue', value)
    open.value = false
  }
})
</script>

<template>
  <div class="relative">
    <slot />
  </div>
</template>
