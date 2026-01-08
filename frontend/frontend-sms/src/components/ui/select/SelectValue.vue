<script setup>
import { computed, inject } from "vue";

const select = inject("select")

const placeholder = defineProps({

  placeholder: String,

})


const displayValue = computed(() => {
  return select?.modelValue?.value || placeholder.placeholder;
});
</script>

<template>
  <div class="text-sm">
    {{ displayValue }}
  </div>
</template>