<script setup>
const props = defineProps({
  size: {
    type: String,
    default: 'sm', // default to "sm"
    validator: (value) => ['xs', 'sm', 'lg', 'xl'].includes(value)
  }
})

// Tailwind text size mapping
const sizeClasses = {
  xs: 'text-xs',
  sm: 'text-sm',
  lg: 'text-lg',
  xl: 'text-xl',
  xl2: 'text-2xl'
}
</script>

<template>
  <h3
    :class="[
      'tracking-tight font-medium',
      sizeClasses[size]
    ]"
  >
    <slot></slot>
  </h3>
</template>
