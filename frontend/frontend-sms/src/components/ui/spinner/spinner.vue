<script setup>
import { cn } from "@/lib/utils";

</script>


<template>
    <div class="flex gap-2">
        <div class="w-5 h-5 border-4 border-background border-t-transparent rounded-full animate-spin"
        :class="cn($attrs.class ?? '')"></div>
        <slot></slot>
    </div>
</template>
