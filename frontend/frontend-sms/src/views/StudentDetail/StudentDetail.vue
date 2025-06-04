<script setup>
import Scaffold from '@/components/layout/scaffold.vue';
import { Card, CardContent, CardIcon, CardFooter, CardHeader, CardTitle, CardSubtitle } from '@/components/ui/card';
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue, } from "@/components/ui/select"
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, AlertDialogHeader, AlertDialogTitle, AlertDialogTrigger, } from "@/components/ui/alert-dialog"
import AlertDecline from '@/components/AlertComponent/AlertDecline.vue';
import Button from '@/components/ui/button/Button.vue';
import Label from '@/components/ui/label/Label.vue';
import Input from '@/components/ui/input/input.vue';
import { Badge } from '@/components/ui/badge';
import { CirclePlus, Trash, SquarePen, ArrowLeft } from 'lucide-vue-next';
import { RouterLink, useRoute } from 'vue-router';
import { onMounted, reactive, ref } from 'vue';
import studentService from '@/services/student/student';
import enrollmentService from '@/services/enrollment/enrollment';
import subjectService from '@/services/subject/subject';
import gradeService from '@/services/grades/grade';
import dayjs from 'dayjs'
import Multiselect from '@vueform/multiselect'
import '@vueform/multiselect/themes/default.css'
import StudentDetailModal from '@/components/Modal/StudentDetailModal.vue';
import { Spinner } from '@/components/ui/spinner';

const formatDate = (dateString) => {
    return dayjs(dateString).format('MMMM D, YYYY')
}

const route = useRoute()
const showAddSubjectDialog = ref(false)
const loading = ref(false)

const student_info = ref([])
const retrieve = async (num) => {
    loading.value = true
    try {
        const response = await studentService.retrieve_student(num);
        student_info.value = response.data
    } catch (e) {
        console.log(e)
    }finally{
        loading.value = false
    }
}

const list_subjects_name = ref([])
const list_subjects = ref([])
const retrieveAllSubjects = async () => {
    loading.value = true
    try {
        const response = await subjectService.list_subjects();
        list_subjects_name.value = response.data.map(item => item.name);
        list_subjects.value = response.data
    } catch (e) {
        console.log(e)
    } finally {
        loading.value = false
    }
}

const student_subject = ref([])
const retrieveStudentSubject = async (num) => {
    loading.value = true
    try {
        const response = await enrollmentService.retrieve_student_subject(num);
        student_subject.value = response.data

        response.data.map(item => retrieveAverage(item.id))

    } catch (e) {
        console.log(e)
    }finally{
        loading.value = false
    }
}
const grades = ref([])
const retrieveAverage = async (num) => {
    loading.value = true
    try {
        const response = await gradeService.retrieve_overall_average(num);
        grades.value.push(response.data)

    } catch (e) {
        console.error(e)
    }finally{
        loading.value = false
    }
}

const average_overall_grade = ref('')
const retrieveStudentAverage = async (student_id) => {
    loading.value = true
    try {
        const response = await gradeService.retrieve_grade_detail_student(student_id);
        console.log(response.data)

        average_overall_grade.value = response.data.average_grade
    
    } catch (e) {
        console.error(e)
    }finally{
        loading.value = false
    }
    
}


const matchEnrollmentToAverage = (num) => {
    const match = grades.value.find(item => item.enrollment_id == num)
    return match ? match.average_grade : null;
}

const selected = ref('')
const createSubject = async () => {
    try {
        const selectedItem = list_subjects.value.find(item => item.name == selected.value)
        await enrollmentService.create_enrollment(route.params.id, selectedItem?.id);
        await retrieveStudentSubject(route.params.id)
        showAddSubjectDialog.value = false
    } catch (e) {
        console.log(e)
    }
}

const handleDelete = async(value) => {
    try {
        await enrollmentService.delete_enrollment(value);
        student_subject.value = student_subject.value.filter(subject => subject.id !== value);
    }catch (e) {
        console.log(e)
        alert(1)
    }
}
const reloadInfo = () => {  
    retrieve(route.params.id)
}


const showEditStudentDialog = ref(false)


onMounted(() => {
    
    retrieve(route.params.id)
    retrieveStudentSubject(route.params.id)
    retrieveStudentAverage(route.params.id)
    retrieveAllSubjects()
})
</script>


<template>
    <Scaffold>
        <p class="text-2xl font-bold pb-5 text-card-foreground">Students </p>

        <Card>
            <CardHeader class="border-b">

                <CardTitle :size="'xl'">
                    <RouterLink :to="{ name: 'student' }"><Button variant="outline" size="sm">
                            <ArrowLeft size="18"></ArrowLeft>
                        </Button></RouterLink>
                    &nbsp;
                    <span class="text-xl font-bold pb-5 text-card-foreground">Student Profile</span>

                </CardTitle>

                <CardIcon class="flex">

                    <Button :variant="'outline'" :class="'mr-2'" size="sm" @click="showEditStudentDialog = true">
                        <SquarePen :size="16"></SquarePen>&nbsp;Edit
                    </Button>

                    <StudentDetailModal @update-info="reloadInfo" v-model:open="showEditStudentDialog"></StudentDetailModal>
                    <!-- Dialog -->
                </CardIcon>
            </CardHeader>
            <CardContent class="space-y-2">
                <div v-if="loading" class="mt-5">
                    <Spinner class="border-primary">Loading Information</Spinner>
                </div>
                <p class="text-2xl font-semibold pt-5">{{ student_info.name || 'name' }} </p>
                <p class="text-sm text-muted-foreground">{{ student_info.email || 'name@gmail.com'}}</p>

                <Badge :value="average_overall_grade">{{ average_overall_grade || 0 }}%</Badge>
                <span class="text-sm text-muted-foreground">Average Grade</span>
                <br>
                <Badge :value="112">{{ student_info.gender || 'other'}}</Badge>
                <Badge :value="92">Enrolled: {{ formatDate(student_info.created_at) }}</Badge>
                <Badge :value="87">Subjects: {{ student_subject.length || 0 }}</Badge>
            </CardContent>
        </Card>
        <br>
        <Card>
            <CardHeader class="border-b">

                <CardTitle :size="'xl'">
                    <div class="flex justify-between">
                        <p class="text-xl font-bold pb-5 text-card-foreground">Subjects & Grades</p>
                    </div>
                </CardTitle>

                <CardIcon>

                    <Button size="sm" @click="showAddSubjectDialog = true">
                        <CirclePlus :size="16"></CirclePlus>&nbsp;Add Subject
                    </Button>
                </CardIcon>

            </CardHeader>
            <CardContent>
                <Card class="my-2" v-for="subjects in student_subject" :key="subjects.id">

                    <CardHeader>
                        <CardTitle size="lg">
                            {{ subjects.subject.name }}
                            <CardSubtitle>{{ subjects.subject.subject_code }}</CardSubtitle>
                            <Badge class="block md:hidden" :value="matchEnrollmentToAverage(subjects.id)">
                                {{ matchEnrollmentToAverage(subjects.id) }} %</Badge>
                        </CardTitle>
                        <CardIcon >
                            <Badge class="hidden md:inline-flex" :value="matchEnrollmentToAverage(subjects.id)">
                                {{ matchEnrollmentToAverage(subjects.id) }} %</Badge>
                                <RouterLink
                                    :to="{ name: 'Studentsubjectdetail', params: { stud_id: $route.params.id, subj_id: subjects.subject.id, enroll_id: subjects.id } }">
    
                                    <Button :variant="'outline'" :class="'mr-2'" size="sm">
                                        <SquarePen :size="16"></SquarePen>
                                    </Button>
                                </RouterLink>
    
                                <!-- Dialog -->
                                <AlertDecline @confirm-delete="handleDelete(subjects.id)">
                                    <Button :variant="'destructive'" size="sm">
                                        <Trash :size="16"></Trash>
                                    </Button>
                                </AlertDecline>
                        </CardIcon>
                    </CardHeader>
                </Card>

            </CardContent>
        </Card>
    </Scaffold>



    <Dialog :open="showAddSubjectDialog" @update:open="showAddSubjectDialog = false">
        <DialogContent>
            <DialogHeader>
                <DialogTitle>Add Subject</DialogTitle>
                <DialogDescription>
                    Add a new subject to this list.
                </DialogDescription>
            </DialogHeader>
            <form @submit.prevent="createSubject">
                <div class="grid gap-4 py-4">

                    <Label for="studno">Pick a Subject</Label>
                    <Multiselect v-model="selected" :options="list_subjects_name" placeholder="Pick one" />

                </div>
                <DialogFooter>
                    <Button type="submit">Add Subject</Button>
                </DialogFooter>
            </form>
        </DialogContent>


    </Dialog>
</template>


<style>

    .dark {
        --ms-bg: #131B25;
        --ms-bg-disabled: #F3F4F6;
        --ms-border-color: hsl(209, 33%, 16%);
        --ms-border-color-active: #D1D5DB;
        --ms-ring-width: 2px;
        --ms-ring-color: #383838e7;


        --ms-dropdown-bg: #131B25;
        --ms-option-color-pointed: #075eda;
        --ms-option-bg-pointed: hsl(222.2 47.4% 11.2%);

        --ms-option-bg-selected: hsl(var(--primary));
        --ms-option-color-selected: #131B25;

        --ms-option-color: #ffffff;
        color: white;

    }
</style>