<script setup>
import { Card, CardContent, CardIcon, CardFooter, CardHeader, CardTitle, CardSubtitle } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Mail, Lock, Eye, EyeOff, User  } from 'lucide-vue-next';
import Button from '@/components/ui/button/Button.vue';
import { computed, reactive, ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { Spinner } from '@/components/ui/spinner';
import { useRoute, useRouter } from 'vue-router';


const showPassword = ref(false)
const route = useRoute();
const router = useRouter();

const auth = useAuthStore();

const form = reactive({
    username: null,
    email: null,
    password: null,
})


const submit = () => {
    // auth.errors = {}; 
    auth.login(form, route, router)
    if(auth.actionStates){
        form.username = null
        form.password = null
    }
    Object.keys(auth.errors).forEach(key => delete auth.errors[key]);
} 

const error = reactive(auth.errors)
const actions = reactive(auth.actionStates)


</script>

<template>
    
    <div class="w-dvw min-h-screen bg-secondary flex justify-center items-center">
        <Card class="shadow-2xl md:w-md w-fit">
            <CardHeader class="flex flex-col items-center">
                <img class="w-25" src="/icon-192x192.png" alt="">
                <p class="text-2xl font-bold">Welcome back</p>
                <p class="text-sm text-muted-foreground mb-4">Enter your credentials to access your account</p>
            </CardHeader>
            <CardContent class=" space-y-4">
                
                <form @submit.prevent="submit">
                    <div>
                        <Label>Username</Label>
                        <div class="relative mt-2">
                            <User class="absolute left-3 top-3 h-4 w-4 text-gray-400" />
                            <Input v-model="form.username" placeholder="Enter your username" class="pl-10"></Input>
                        </div>
                        <p class="text-xs text-red-400 mt-2">{{ error.username }}</p>
                    </div>
                    <div>
                        <Label>Password</Label>
                        <div class="relative mt-2">
                            <Lock class="absolute left-3 top-3 h-4 w-4 text-gray-400" />
                            <Input v-model="form.password" :type="showPassword ? 'text' : 'password'" placeholder="Enter your password" class="pl-10"></Input>
                            <Button type="button" variant="ghost" size="sm"
                            class="absolute right-0 top-0 h-full px-3 py-2 hover:bg-transparent" @click="showPassword = !showPassword">
                            
                            <component :is="showPassword ? EyeOff : Eye" class="h-4 w-4 text-gray-400" />
                        </Button>
                    </div>
                    <p class="text-xs text-red-400 mt-2">{{ error.password }}</p>
                </div>
                
                <p class="text-xs text-red-400 mt-2">{{ error.non_field_errors }}</p>
                
                <Button type="submit" class="w-full mt-4">
                    <p v-if="!actions.authenticating">Sign in</p>
                    <Spinner v-if="actions.authenticating">Loading...</Spinner>
                </Button>
            </form>
        </CardContent>
        <CardFooter></CardFooter>
        </Card>
    </div>
</template>
