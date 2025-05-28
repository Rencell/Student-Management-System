<script setup>
import { cn } from "@/lib/utils";

const props = defineProps({
  class: String,
});
</script>

<template>
  <tfoot
    :class="cn('bg-primary font-medium text-primary-foreground', props.class)"
  >
    <slot />
  </tfoot>
</template>