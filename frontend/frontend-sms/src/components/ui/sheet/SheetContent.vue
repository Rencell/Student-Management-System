<script setup>
import { computed, inject, onMounted, onUnmounted, ref, watch } from "vue";
import { cn } from "@/lib/utils";
import { X } from "lucide-vue-next";
import Button from "../button/Button.vue";
import { SheetClose } from ".";

const props = defineProps({
  side: {
    type: String,
    default: 'right',
    validator: (value) => ['top', 'right', 'bottom', 'left'].includes(value),
  },
});


const sheet = inject("sheet");

const handleEscapeKey = (event) => {
  if (event.key === "Escape" && sheet?.open.value) {
    sheet?.close();
  }
};

onMounted(() => {
  document.addEventListener("keydown", handleEscapeKey);
});

onUnmounted(() => {
  document.removeEventListener("keydown", handleEscapeKey);
});

const sideClasses = computed(() => {
  switch (props.side) {
    case "top":
      return "inset-x-0 top-0 border-b data-[state=closed]:slide-out-to-top data-[state=open]:slide-in-from-top";
    case "bottom":
      return "inset-x-0 bottom-0 border-t data-[state=closed]:slide-out-to-bottom data-[state=open]:slide-in-from-bottom";
    case "left":
      return "inset-y-0 left-0 h-full w-3/4 border-r data-[state=closed]:slide-out-to-left data-[state=open]:slide-in-from-left sm:max-w-sm";
    default:
      return "inset-y-0 right-0 h-full w-3/4 border-l data-[state=closed]:slide-out-to-right data-[state=open]:slide-in-from-right sm:max-w-sm";
  }
});
</script>

<template>
  <Teleport to="body">
    <div
      v-if="sheet.open.value"
      class="fixed inset-0 z-50 bg-background/80 backdrop-blur-sm"
      @click="sheet.close()"
    />
    <div
      v-if="sheet.open.value"
      :class="cn(
        'fixed z-50 gap-4 bg-background p-6 shadow-lg transition ease-in-out',
        sideClasses,
        $attrs.class ?? '',
      )"
      :data-state="sheet.open.value ? 'open' : 'closed'"
      @click.stop
    >
      <div class="flex flex-col space-y-2">
        <div class="flex items-center justify-between">
          <slot name="header" />
          <SheetClose>
            <div
              class="rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-secondary"
            >
              <Button variant="outline" size="xs"><X class="h-5 w-5" /></Button>
              <span class="sr-only">Close</span>
            </div>
          </SheetClose>
        </div>
        <slot />
      </div>
    </div>
  </Teleport>
</template>

<style>
.slide-in-from-top {
  animation: slideInFromTop 0.3s ease-out;
}

.slide-out-to-top {
  animation: slideOutToTop 0.3s ease-in;
}

.slide-in-from-bottom {
  animation: slideInFromBottom 0.3s ease-out;
}

.slide-out-to-bottom {
  animation: slideOutToBottom 0.3s ease-in;
}

.slide-in-from-left {
  animation: slideInFromLeft 0.3s ease-out;
}

.slide-out-to-left {
  animation: slideOutToLeft 0.3s ease-in;
}

.slide-in-from-right {
  animation: slideInFromRight 0.3s ease-out;
}

.slide-out-to-right {
  animation: slideOutToRight 0.3s ease-in;
}

@keyframes slideInFromTop {
  from {
    transform: translateY(-100%);
  }
  to {
    transform: translateY(0);
  }
}

@keyframes slideOutToTop {
  from {
    transform: translateY(0);
  }
  to {
    transform: translateY(-100%);
  }
}

@keyframes slideInFromBottom {
  from {
    transform: translateY(100%);
  }
  to {
    transform: translateY(0);
  }
}

@keyframes slideOutToBottom {
  from {
    transform: translateY(0);
  }
  to {
    transform: translateY(100%);
  }
}

@keyframes slideInFromLeft {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}

@keyframes slideOutToLeft {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(-100%);
  }
}

@keyframes slideInFromRight {
  from {
    transform: translateX(100%);
  }
  to {
    transform: translateX(0);
  }
}

@keyframes slideOutToRight {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(100%);
  }
}
</style>