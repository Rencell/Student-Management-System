<script setup>
import { cn } from "@/lib/utils";
</script>

<template>
  <h3
    :class="cn('text-lg font-semibold text-popover-foreground', $attrs.class ?? '')"
    v-bind="$attrs"
  >
    <slot />
  </h3>
</template>