<script setup>
import { Home, Users, TableOfContents } from 'lucide-vue-next';
import { useRoute, RouterLink } from 'vue-router'

const route = useRoute()
const pathname = route.path

const routes = [
    {

        href: "/",
        label: "Dashboard",
        icon: Home,
        active: pathname === "/",
    },
    {

        href: "/class",
        label: "Class",
        icon: TableOfContents,
        active: pathname === "/class",
    },
    {

        href: "/students",
        label: "Students",
        icon: Users,
        active: pathname === "/students" || pathname === "/students/1" || pathname === "/students/1/subjects/subject1",
    },
]
</script>

<template>
    <div class="flex flex-col gap-2 p-4 px-10 border-r w-fit bg-background">
        <RouterLink v-for="(route, key) in routes" :key="key" :to="route.href || '/'"
            :class="route.active ? 'bg-primary text-card ' : 'text-card-foreground'"
            class="flex items-center gap-2 rounded-md px-3 pr-10 py-2 text-sm font-medium hover:bg-blue-500 hover:text-card">
            <component :is="route.icon" :size="20" />
            {{ route.label }}
        </RouterLink>

    </div>

</template>

<style scoped></style>
