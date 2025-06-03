<script setup>
import { inject, onMounted, onUnmounted } from 'vue'
import { cn } from '@/lib/utils'

// Safely inject the select context
const select = inject('select')

if (!select) {
  throw new Error('Select context not found. Make sure you are using <Select> as a parent.')
}

const handleEscapeKey = (event) => {
  if (event.key === 'Escape' && select.open.value) {
    select.toggle()
  }
}

onMounted(() => {
  document.addEventListener('keydown', handleEscapeKey)
})

onUnmounted(() => {
  document.removeEventListener('keydown', handleEscapeKey)
})
</script>

<template>
  <Teleport to="body">
    <!-- Overlay that closes the dropdown -->
    <div
      v-if="select.open.value"
      class="fixed inset-0 z-40"
      @click="select.toggle"
    />

    <!-- Dropdown -->
    <div
      v-if="select.open.value"
      class="fixed z-50 mt-2 min-w-[8rem] rounded-md border bg-popover text-popover-foreground shadow-md animate-in fade-in-80"
      :class="cn($attrs.class ?? '')"
      :style="{ top: 'calc(100px)', left: 'calc(100px)' }" <!-- Adjust positioning as needed -->
      v-bind="$attrs"
    >
      <div class="p-1">
        <slot />
      </div>
    </div>
  </Teleport>
</template>
