<script setup>
import { cn } from "@/lib/utils";




const props = defineProps({
  value: {
    type: Number,
    required: true,
  },
});

const getGradeClass = (score) => {
  if (score === null || score === undefined) return 'bg-gray-100 text-gray-800';
  if (score >= 110) return 'bg-purple-100 text-purple-800';
  if (score >= 90) return 'bg-green-100 text-green-800';
  if (score >= 80) return 'bg-blue-100 text-blue-800';
  if (score >= 70) return 'bg-teal-100 text-teal-800';
  if (score >= 60) return 'bg-amber-100 text-amber-800';
  return 'bg-red-100 text-red-800';
};

</script>

<template>

    <p :class="cn('inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium mr-2',
        getGradeClass(props.value),
        $attrs.class ?? '')" v-bind="$attrs">
        <slot />
    </p>
</template>