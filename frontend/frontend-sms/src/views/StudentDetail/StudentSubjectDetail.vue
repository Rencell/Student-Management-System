<script setup>
import scaffold from '@/components/layout/scaffold.vue';
import { Card, CardContent, CardIcon, CardFooter, CardHeader, CardTitle, CardSubtitle } from '@/components/ui/card';
import { Table, TableBody, TableCell, TableCaption, TableFooter, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import AlertDecline from '@/components/AlertComponent/AlertDecline.vue';
import { Badge } from '@/components/ui/badge';
import { Trash, CirclePlus, ArrowLeft, SquarePen } from 'lucide-vue-next';
import Button from '@/components/ui/button/Button.vue';
import { computed, onMounted, reactive, ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';
import studentService from '@/services/student/student';
import subjectService from '@/services/subject/subject';
import gradeService from '@/services/grades/grade';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import Multiselect from '@vueform/multiselect'
import '@vueform/multiselect/themes/default.css'
import UpdateGradeModal from '@/components/Modal/StudentSubjectDetail/UpdateGradeModal.vue';
import AddGradeModal from '@/components/Modal/StudentSubjectDetail/AddGradeModal.vue';
import dayjs from 'dayjs'
import Spinner from '@/components/ui/spinner/spinner.vue';

const loading = ref(false)
const route = useRoute()

const grade_data = reactive({
    quiz: [],
    assignment: [],
    activity: [],
})

// DefineModels
const showAddStudentDialog = ref(false)
const showUpdateStudentDialog = ref(false)
const currentGradeId = ref(0)

const updateGradeId = (value) => {
    currentGradeId.value = value
    showUpdateStudentDialog.value = true
}

const initAverageGrade = () => {
    Average.value = ''
    average_grade.value = []
    retrieve_grade_average()
} 

const updateGrade = (value) => {

    const list = grade_data[getTypeName(value.type)]
    const index = list.findIndex(item => item.id === value.id)

    if (index !== -1) {
        Object.assign(list[index], value)
    }

    initAverageGrade();

}

const createGrade = (response) => {
    grade_data[getTypeName(response.type)].push(response);
    
    showAddStudentDialog.value = false
    initAverageGrade();
}

const deleteGrade = async (data, grade_id) => {

    const validTypes = ['quiz', 'assignment', 'activity'];
    try {
        await gradeService.delete_grade(grade_id)
        if (validTypes.includes(data))
            grade_data[data] = grade_data[data].filter(item => item.id !== grade_id);
        initAverageGrade();
    } catch (e) {
        console.error(e)

    }
}

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



const subject_info = ref([])
const retrieve_subject = async (num) => {
    loading.value = true
    try {
        const response = await subjectService.retrieve_subject(num);
        subject_info.value = response.data
    } catch (e) {
        console.log(e)
    }finally{
        loading.value = false
    }
}

const retrieve_grade = async (num) => {
    loading.value = true
    try {
        const response = await gradeService.retrieve_grades(num);
        console.log(response)
        response.data.forEach(item => {
            if (item.type === 1) {
                grade_data.quiz.push(item);
            } else if (item.type === 2) {
                grade_data.assignment.push(item);
            } else if (item.type === 3) {
                grade_data.activity.push(item);
            }
        });
    } catch (e) {
        console.log(e)
    }finally{
        loading.value = false
    }
}


const grade_type = ref([])
const grade_type_with_id = ref([])
const retrieve_grade_type = async () => {
    loading.value = true
    try {
        const response = await gradeService.retrieve_grade_type();
        grade_type.value = response.data.map(item => toUpperCaseValue(item.name))
        grade_type_with_id.value = response.data
    } catch (e) {
        console.log(e)
    }finally{
        loading.value = false
    }
}

const Average = ref()
const average_grade = ref([])
const retrieve_grade_average = async () => {
    loading.value = true
    try {
        const response = await gradeService.retrieve_grade_average(route.params.enroll_id);
        Average.value = response.data.average_grade
        average_grade.value.push(response.data.average_quiz)
        average_grade.value.push(response.data.average_assignment)
        average_grade.value.push(response.data.average_activity)

    } catch (e) {
        console.log(e)
    }finally{
        loading.value = false
    }
}





// UTILITIES
const formatDate = (dateString) => {
    return dayjs(dateString).format('YYYY-MM-DD')
}

const toUpperCaseValue = (value) => {
    return value.charAt(0).toUpperCase() + value.slice(1)
}

const getTypeName = (value) => {
    switch (value) {
        case 1:
            return 'quiz'
        case 2:
            return 'assignment'
        case 3:
            return 'activity'
        default:
            return 'unknown'
    }
}


onMounted(() => {
    retrieve(route.params.stud_id)
    retrieve_subject(route.params.subj_id)
    retrieve_grade(route.params.enroll_id)
    retrieve_grade_type()
    retrieve_grade_average()
})

</script>


<template>

    <UpdateGradeModal @update-grade="updateGrade" :id="currentGradeId" v-model:open="showUpdateStudentDialog">
    </UpdateGradeModal>
    <AddGradeModal @create-grade="createGrade" v-model:open="showAddStudentDialog">

    </AddGradeModal>

    <div>
        <scaffold>

            <div class="flex justify-between">
                <p class="text-2xl font-bold pb-5 text-card-foreground">{{ subject_info.name }} Grades</p>
                <Button @click="showAddStudentDialog = true">
                    <CirclePlus :size="16"></CirclePlus>&nbsp;Add Grades
                </Button>
            </div>
            <div class="space-y-4">
                <Card>
                    <CardHeader class="border-b">
                        <CardTitle size="xl">
                            <RouterLink :to="{ name: 'studentdetail', params: { id: student_info.id ?? 1 } }"><Button
                                variant="outline" size="sm">
                                <ArrowLeft size="18"></ArrowLeft>
                            </Button></RouterLink>
                            &nbsp;
                            Subject Information
                        </CardTitle>
                    </CardHeader>
                    <CardContent class="space-y-2">
                        <div v-if="loading" class="mt-5">
    
                            <Spinner class="border-primary">Loading Data...</Spinner>
                        </div>
                        <p class="text-2xl font-semibold pt-4">{{ student_info.name || 'name' }}</p>
                        <p class="text-sm text-muted-foreground">{{ student_info.email || 'name@gmail.com'}}</p>
                        <Badge :value="Average">{{ Average || 0 }} %</Badge> <span
                            class="text-sm text-muted-foreground">Overall Average
                        </span>
                        <br>
                        <Badge :value="72">Subject: {{ subject_info.subject_code || 'code'}}</Badge>
                        <Badge :value="67">Total Assessment: 3</Badge>
                    </CardContent>
                </Card>

                <!--  Grades -->
                <Card v-for="(grade, category, index) in grade_data" :key="index">
                    <CardHeader>
                        <CardTitle size="xl2">{{ toUpperCaseValue(category) }}
                            <CardSubtitle>Average: <Badge :value="average_grade[index]">{{ average_grade[index] }} %
                                </Badge>
                            </CardSubtitle>
                        </CardTitle>

                    </CardHeader>

                    <CardContent>
                        <Table>
                            <TableCaption>A list of your recent {{category}}.</TableCaption>
                            <TableHeader>
                                <TableRow>
                                    <TableHead>Name</TableHead>
                                    <TableHead>Score</TableHead>
                                    <TableHead class="hidden sm:table-cell">Date</TableHead>
                                    <TableHead>Status</TableHead>
                                    <TableHead>Actions</TableHead>
                                </TableRow>
                            </TableHeader>
                            <TableBody v-for="quiz in grade" :key="quiz.id">
                                <TableCell :class="'font-medium'">{{ quiz.name }}</TableCell>
                                <TableCell>{{ quiz.score }} / {{ quiz.max_score }}</TableCell>
                                <TableCell class="hidden sm:table-cell">{{ formatDate(quiz.created_at) }}</TableCell>
                                <TableCell>
                                    <Badge :value="quiz.percentage">{{ quiz.percentage }} %</Badge>
                                </TableCell>
                                <TableCell >
                                    <Button variant="outline" size="sm" class="mr-2" @click="updateGradeId(quiz.id)">
                                        <SquarePen :size="17"></SquarePen>
                                    </Button>
                                    <AlertDecline @confirm-delete="deleteGrade(category, quiz.id)">
                                        <Button variant="destructive" size="sm">
                                            <Trash :size="17"></Trash>
                                        </Button>
                                    </AlertDecline>
                                </TableCell>

                            </TableBody>
                        </Table>
                    </CardContent>
                </Card>

            </div>
        </scaffold>
    </div>

</template>