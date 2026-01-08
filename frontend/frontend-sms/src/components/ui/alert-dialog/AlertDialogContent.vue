<script setup>
import { inject, onMounted, onUnmounted } from "vue";
import { cn } from "@/lib/utils";

const alertDialog = inject("alertDialog")

const handleEscapeKey = (event) => {
  if (event.key === "Escape" && alertDialog.open.value) {
    alertDialog?.close();
  }
};

onMounted(() => {
  document.addEventListener("keydown", handleEscapeKey);
});

onUnmounted(() => {
  document.removeEventListener("keydown", handleEscapeKey);
});
</script>

<template>
  <Teleport to="body">
    <div
      v-if="alertDialog.open.value"
      class="fixed inset-0 z-50 bg-background/80 backdrop-blur-sm"
      @click="alertDialog.close()"
    />
    <div
      v-if="alertDialog.open.value"
      class="fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 sm:rounded-lg"
      :class="cn($attrs.class ?? '')"
      @click.stop
    >
      <slot />
    </div>
  </Teleport>
</template>