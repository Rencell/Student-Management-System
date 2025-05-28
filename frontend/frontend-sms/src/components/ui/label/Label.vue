<script setup>
import { cn } from "@/lib/utils";
</script>

<template>
  <label
    :class="cn('text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 text-card-foreground', $attrs.class ?? '')"
    v-bind="$attrs"
  >
    <slot />
  </label>
</template>