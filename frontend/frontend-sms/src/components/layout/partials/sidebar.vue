<script setup>
import { Home, Users, TableOfContents, Book, GraduationCap } from 'lucide-vue-next';
import { useRoute, RouterLink } from 'vue-router'
import {
    Sheet,
    SheetContent,
    SheetDescription,
    SheetHeader,
    SheetTitle,
    SheetTrigger,
} from "@/components/ui/sheet"
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

        href: "/Subjects",
        label: "Subjects",
        icon: Book,
        active: pathname === "/Subjects",
    },
    {

        href: "/students",
        label: "Students",
        icon: Users,
        active: pathname === "/students" || pathname.startsWith("/students/")
    },
]

const openSheet = defineModel('open', { default: false })
</script>

<template>
    <div class="hidden md:flex flex-col gap-2 p-4 px-10 border-r w-fit bg-background">
        <RouterLink v-for="(route, key) in routes" :key="key" :to="route.href || '/'"
            :class="route.active ? 'bg-primary text-card ' : 'text-card-foreground'"
            class="flex items-center gap-2 rounded-md px-3 pr-10 py-2 text-sm font-medium hover:bg-blue-500 hover:text-card">
            <component :is="route.icon" :size="20" />
            {{ route.label }}
        </RouterLink>

    </div>

    <Sheet v-model:open="openSheet">
        <SheetContent side="left" class="w-64 p-5">
            <template #header>
                <div class="flex h-16 items-center gap-2 border-b">
                    <GraduationCap class="h-6 w-6" />
                    <span class="font-bold text-sm">Student Management System</span>
                </div>
            </template>
            <RouterLink v-for="(route, key) in routes" :key="key" :to="route.href || '/'"
                :class="route.active ? 'bg-primary text-card ' : 'text-card-foreground'"
                class="p-6 flex items-center gap-2 rounded-md px-3 pr-10 py-2 text-sm font-medium hover:bg-blue-500 hover:text-card">
                <component :is="route.icon" :size="20" />
                {{ route.label }}
            </RouterLink>
        </SheetContent>
    </Sheet>

</template>

<style scoped></style>
