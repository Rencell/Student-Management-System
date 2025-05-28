<template>
    <nav class="sticky top-0 z-30 flex h-16 items-center gap-4 border-b px-4 md:px-6 bg-background">
      <div class="container flex h-16 items-center px-4">
        <RouterLink to="/" class="font-bold text-lg flex gap-3 items-center text-card-foreground"><GraduationCap/> Student Management</RouterLink>
        <div class="ml-auto flex items-center space-x-4">
          <RouterLink to="/" class="text-sm font-medium transition-colors hover:text-primary">
            Dashboard
          </RouterLink>
        </div>
      </div>
    </nav>
  </template>
  
  <script setup lang="ts">
  import { RouterLink } from 'vue-router';
  import { GraduationCap } from 'lucide-vue-next';
  </script>