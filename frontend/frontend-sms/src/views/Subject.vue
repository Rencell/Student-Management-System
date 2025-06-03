<script setup>
import scaffold from '@/components/layout/scaffold.vue';
import Button from '@/components/ui/button/Button.vue';
import { Card, CardContent, CardIcon, CardFooter, CardHeader, CardTitle, CardSubtitle } from '@/components/ui/card';
import { CirclePlus, Search, SquarePen, Trash } from 'lucide-vue-next';


import { Input } from '@/components/ui/input';
import { Badge } from '@/components/ui/badge';
import subjectService from '@/services/subject/subject';
import { computed, onMounted, ref } from 'vue';
import enrollmentService from '@/services/enrollment/enrollment';
import gradeService from '@/services/grades/grade';
import subjectModal from '@/components/Modal/Subject/subjectModal.vue';
import { Spinner } from '@/components/ui/spinner';
const subject_list = ref([])
const subject_students = ref([])
const subject_grades = ref([])
const loading = ref(false)

const retrieve_subjects = async () => {
    loading.value = true
    try {
        const response = await subjectService.list_subjects();
        subject_list.value = response.data;

        for (const subject of subject_list.value) {
            await retrieve_subject_students(subject.id)
            await retrieve_average_by_subject(subject.id)
        }

    } catch (e) {
        console.error(e)
    } finally{
        loading.value = false
    }
}
const retrieve_subject_students = async (subject_id) => {
    try {
        const response = await enrollmentService.retrieve_subject_student(subject_id);
        subject_students.value.push(response.data);
    } catch (e) {
        console.error(e)
    }
}

const retrieve_average_by_subject = async (subject_id) => {
    try {
        const response = await gradeService.retrieve_average_by_subject(subject_id);
        subject_grades.value.push(response.data);
    } catch (e) {
        console.error(e)
    }
}
const showEditStudentDialog = ref(false)

const updateSubjectList = (data) => {
    subject_list.value.push(data)
}

const searchQuery = ref('')
const filteredData = computed(() => {
    const lowerCase = searchQuery.value.toLowerCase()
    return subject_list.value.filter(subject =>
        subject.name.toLowerCase().includes(lowerCase) ||
        subject.subject_code.toLowerCase().includes(lowerCase)
    )
})

onMounted(() => {
    retrieve_subjects()
    
})

</script>

<template>

    <subjectModal v-model:open="showEditStudentDialog" @create-subject="updateSubjectList"></subjectModal>
    <div>

        <scaffold>
            <div class="flex justify-between">
                <p class="text-2xl font-bold pb-5 text-card-foreground">Subjects </p>
                <Button @click="showEditStudentDialog = true">
                    <CirclePlus :size="16"></CirclePlus>&nbsp;Add Subject
                </Button>
            </div>

            <Card>
                <CardHeader class="border-b">
                    <CardTitle size="xl">All subjects</CardTitle>
                </CardHeader>

                <CardContent>
                    <Input v-model="searchQuery" class="mt-2" :icon="true" placeholder="Search Subjects...">
                    <Search></Search>
                    </Input>

                    <br>
                    <div v-if="loading" class="flex justify-center">
                        <Spinner class="border-primary">Loading Data...</Spinner>
                    </div>
                    <div v-else>
                        <Card v-for="(subject, index) in filteredData" :key="index"
                            class="mb-2 hover:bg-secondary/70 transition-all">
                            <CardHeader>
                                <CardTitle size="lg">
                                    {{ subject.name }}
                                    <CardSubtitle>{{ subject.subject_code }}</CardSubtitle>
                                    <Badge>Students Enrolled ({{ subject_students[index]?.length || 0 }})</Badge>
    
                                </CardTitle>
                                <CardIcon>
                                    <Badge :value="subject_grades[index]?.average_grade || 0">
                                        {{ subject_grades[index]?.average_grade || 0 }}%</Badge>
                                </CardIcon>
                            </CardHeader>
                        </Card>
                    </div>
                </CardContent>
            </Card>
        </scaffold>
    </div>

</template>