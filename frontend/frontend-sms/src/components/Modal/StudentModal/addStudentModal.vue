<script setup>
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Label } from '@/components/ui/label';
import Button from '@/components/ui/button/Button.vue';
import { Input } from '@/components/ui/input';

import Datepicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'

import Multiselect from '@vueform/multiselect'
import '@vueform/multiselect/themes/default.css'
import { reactive } from 'vue';

import dayjs from 'dayjs'

import studentService from '@/services/student/student';

const showAddStudentDialog = defineModel('open', {default: false})
const emit = defineEmits(['create-student'])
const student_form = reactive({
  name: '',
  student_number: '',
  email: '',
  birth_date: '',
  gender: '',
})

const submit = async () => {
  try {
    student_form.birth_date = formatDate(student_form.birth_date)
    const response = await studentService.create_student(student_form);
    showAddStudentDialog.value = false
    console.log(response.data)
    emit('create-student', response.data)
  } catch (error) {
    console.error('Registration failed:', error.response.data);
  }
}

const formatDate = (dateString) => {
  return dayjs(dateString).format('YYYY-MM-DD')
}

const genderOptions = [
    {value: 'male', label:'Male'},
    {value: 'female', label:'Female'},
    {value: 'other', label:'Other'},
]

</script>


<template>
    <Dialog v-model:open="showAddStudentDialog" @update:open="showAddStudentDialog = false">
        <DialogContent>
            <DialogHeader>
                <DialogTitle>Add Student</DialogTitle>
                <DialogDescription>
                    Add a new student to this list.
                </DialogDescription>
            </DialogHeader>
            <form @submit.prevent="submit">
                <div class="grid gap-4 py-4">
                    <div>
                        <Label for="subjectName">Student Name</Label>
                        <Input v-model="student_form.name" id="subjectName" placeholder="John Doe" required />
                    </div>
                    <div class="flex gap-2">
                        <div class="grow">
                            <Label for="studno">Student No.</Label>
                            <Input id="studno" placeholder="Eg. 202482056" v-model="student_form.student_number"
                                required />
                        </div>
                        <div class="grow">
                            <Label for="gender">Gender</Label>
                            <Multiselect v-model="student_form.gender" :options="genderOptions"
                                placeholder="Pick one" />
                            <!-- <Input id="gender" placeholder="Male" required v-model="student_form.gender" /> -->
                        </div>
                    </div>
                    <div>
                        <Label for="email">Email Address</Label>
                        <Input v-model="student_form.email" type="email" placeholder="johndoe67@example.com" id="email"
                            required />
                    </div>
                    <div>
                        <Label for="birth">Date of Birth</Label>
                        <Datepicker v-model="student_form.birth_date" format="yyyy-MM-dd" />
                    </div>
                </div>
                <DialogFooter>
                    <Button type="submit">Add Student</Button>
                </DialogFooter>
            </form>
        </DialogContent>
    </Dialog>
</template>