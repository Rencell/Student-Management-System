<script setup>
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, AlertDialogHeader, AlertDialogTitle, AlertDialogTrigger, } from "@/components/ui/alert-dialog"

import { useRoute, RouterLink } from 'vue-router'

</script>

<template>
    <AlertDialog>
        <AlertDialogTrigger class="inline-flex">
            <slot></slot>
        </AlertDialogTrigger>
        <AlertDialogContent>
            <AlertDialogHeader>
                <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
                <AlertDialogDescription>
                    Are you sure you want to logout?
                </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
                <AlertDialogCancel class="text-primary">Cancel</AlertDialogCancel>
                <RouterLink :to="{name: 'logout'}" >
                    <AlertDialogAction class="w-full">Continue</AlertDialogAction>
                </RouterLink>
            </AlertDialogFooter>
        </AlertDialogContent>
    </AlertDialog>

</template>