<template>
  <nav class="sticky top-0 z-30 flex h-16 items-center gap-4 border-b px-4 md:px-6 bg-background">
    <Button variant="outline" size="icon" class="md:hidden" @click="emit('open-sheet')">
      <Menu className="h-5 w-5" />
      <span className="sr-only">Toggle Menu</span>
    </Button>

    <div class="container flex h-16 items-center px-4">
      <img class="h-full p-2" src="/icon-192x192.png" alt="">
      <RouterLink to="/" class="font-bold text-lg flex gap-3 items-center text-card-foreground">
         Student Management
      </RouterLink>
      <div class="ml-auto flex items-center space-x-4">
        <Moon class="text-black hover:text-black/80 cursor-pointer transition-colors" v-if="!moon_sun"
          @click="darkmode()"></Moon>
        <Sun class="text-primary hover:text-primary/80 cursor-pointer transition-colors" v-else @click="darkmode()">
        </Sun>
        
        <AlertLogout>

          <LogOut class="cursor-pointer text-primary transition-colors hover:text-primary/80"></LogOut>
        </AlertLogout>
       
      </div>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { GraduationCap, Menu, Moon, Sun, LogOut } from 'lucide-vue-next';
import Button from '@/components/ui/button/Button.vue';
import { onMounted, ref } from 'vue';
import AlertLogout from '@/components/AlertComponent/AlertLogout.vue';

const emit = defineEmits(['open-sheet'])
const moon_sun = ref(false)

const darkmode = () => {
  document.documentElement.classList.toggle('dark');
  moon_sun.value = !moon_sun.value
}

onMounted(() => {
  moon_sun.value = document.documentElement.classList.contains('dark');
});
</script>