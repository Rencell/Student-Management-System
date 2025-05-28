<script setup>
import { inject, onMounted, onUnmounted } from "vue";
import { cn } from "@/lib/utils";
import { X } from "lucide-vue-next";

const dialog = inject("dialog");

const handleEscapeKey = (event) => {
  if (event.key === "Escape" && dialog?.open?.value) {
    dialog.close();
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
      v-if="dialog?.open?.value"
      class="fixed inset-0 z-50 bg-background/70 backdrop-blur-sm"
      @click="dialog.close()"
    />
    <div
      v-if="dialog?.open?.value"
      class="fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 sm:rounded-lg"
      :class="cn($attrs.class ?? '')"
      @click.stop
    >
      <div class="flex flex-col space-y-1.5 text-center sm:text-left">
        <slot name="header" />
      </div>
      <slot />
      <button
        class="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-accent data-[state=open]:text-muted-foreground"
        @click="dialog.close()"
      >
        <X class="h-4 w-4 text-primary" />
        <span class="sr-only">Close</span>
      </button>
    </div>
  </Teleport>
</template>