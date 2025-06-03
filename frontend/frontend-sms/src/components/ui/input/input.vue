<script setup>
import { cn } from '@/lib/utils';
const props = defineProps({
    modelValue: String,
    type: {
        type: String,
        default: 'text'
    },
    placeholder: {
        type: String,
        default: ''
    },
    class: {
        type: String,
        default: ''
    },
    icon: {
        type: Boolean,
        default: false
    }
})

defineEmits(['update:modelValue'])

</script>

<template>

    <div class="flex gap-2 items-center" v-if="props.icon">
        <slot></slot>
        <input :type="type" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)"
            :class="cn('flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm', props.class ?? '')"
            :placeholder="placeholder">
    </div>

    <div v-else>
        <input :type="type" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)"
            :class="cn('text-muted-foreground mt-1 flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm', props.class ?? '')"
            :placeholder="placeholder">

    </div>
</template>