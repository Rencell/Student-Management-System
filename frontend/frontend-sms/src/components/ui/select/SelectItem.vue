<script setup>
import { computed, inject } from 'vue'
import { cn } from '@/lib/utils'
import { Check } from 'lucide-vue-next'

const props = defineProps(['value'])

const select = inject('select')

const isSelected = computed(() => select?.modelValue?.value === props.value)

const handleSelect = () => {
  select?.select(props.value)
}
</script>

<template>
  <div
    class="relative flex w-full cursor-default select-none items-center rounded-sm py-1.5 pl-2 pr-8 text-sm outline-none hover:bg-accent hover:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50"
    :class="cn($attrs.class ?? '')"
    @click="handleSelect"
    v-bind="$attrs"
  >
    <Check
      v-if="isSelected"
      class="absolute right-2 h-4 w-4"
    />
    <slot />
  </div>
</template>
