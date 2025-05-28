<script setup>
import { computed } from 'vue';
import { buttonVariants } from './index';
import { cn } from '@/lib/utils';


const props = defineProps ({
    variant: String,
    size: String,
    class: String,
    type: {
        type: String,
        default: "button"
    }
})

const classNames = computed(() => {
    return cn(buttonVariants({ variant: props.variant, size: props.size }), props.class)
})
</script>

<template>
    <button :type="type" :class="classNames">
        <slot></slot>
    </button>
</template>