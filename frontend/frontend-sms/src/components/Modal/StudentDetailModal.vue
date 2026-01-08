<script setup>
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Label } from '../ui/label';
import { Input } from '../ui/input';
import Button from '../ui/button/Button.vue';

import Datepicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import { onMounted, ref } from 'vue';
import studentService from '@/services/student/student';
import { useRoute } from 'vue-router';

const route = useRoute();
const emit = defineEmits(['update-info'])

import Multiselect from '@vueform/multiselect'
import '@vueform/multiselect/themes/default.css'

const confirmUpdate = () => {
    emit('update-info')
}

const showEditStudentDialog = defineModel('open', { default: false })

const student_info = ref([])
const retrieve = async (num) => {
    try {
        const response = await studentService.retrieve_student(num);
        student_info.value = response.data
        console.log(student_info.value)
    } catch (e) {
        console.log(e)
    }
}

const submit = async() => {
    
    try {
        await studentService.update_student(route.params.id, student_info.value);
        showEditStudentDialog.value = false
        confirmUpdate();
    } catch (e) {
        console.log(e)
    }
}
onMounted(() =>{
    retrieve(route.params.id)
})

</script>

<template>

    <Dialog v-model:open="showEditStudentDialog" @update:open="showEditStudentDialog = false">
        <DialogContent>
            <DialogHeader>
                <DialogTitle>Update Student</DialogTitle>
                <DialogDescription>
                    Update student of this list.
                </DialogDescription>
            </DialogHeader>
            <form @submit.prevent="submit">
                <div class="grid gap-4 py-4">
                    <div>
                        <Label for="subjectName">Student Name</Label>
                        <Input id="subjectName" placeholder="John Doe" v-model="student_info.name" required />
                    </div>
                    <div class="flex gap-2">
                        <div class="grow">
                            <Label for="studno">Student No.</Label>
                            <Input id="studno" placeholder="Eg. 202482056" v-model="student_info.student_number" required />
                        </div >
                        <div class="grow">
                            <Label for="gender">Gender</Label>
                            <Multiselect v-model="student_info.gender" :options="['male', 'female', 'other']" placeholder="Pick one" />
                        </div>
                    </div>
                    <div>
                        <Label for="email">Email Address</Label>
                        <Input type="email" placeholder="johndoe67@example.com" id="email"
                            required  v-model="student_info.email" />
                    </div>
                    <div>
                        <Label for="birth">Date of Birth</Label>
                        <Datepicker format="yyyy-MM-dd"  v-model="student_info.date_of_birth" />
                    </div>
                </div>
                <DialogFooter>
                    <Button type="submit">Update Student</Button>
                </DialogFooter>
            </form>
        </DialogContent>
    </Dialog>


</template>