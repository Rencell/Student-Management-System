<script setup>
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import Multiselect from '@vueform/multiselect'
import '@vueform/multiselect/themes/default.css'
import { computed, onMounted, reactive, ref, watch } from 'vue';
import Button from '@/components/ui/button/Button.vue';
import gradeService from '@/services/grades/grade';
import { RouterLink, useRoute } from 'vue-router';

const showAddStudentDialog = defineModel(
    'open', { default: false },
)

const form = reactive({
    name: "",
    score: null,
    max_score: null,
    type: null,
    enrollment_id: null,
    subject: null,
    percentage: null
})
const clearform = () => {
    form.name = null
    form.score = null
    form.max_score = null
    form.type = null
    form.enrollment_id = null
    form.subject = null
    form.percentage = null
}

const emit = defineEmits(['create-grade'])

const submit = async() => {

    if(policeAlert.value)
        return;
    

    try {
        const response = await gradeService.create_grade(form);
        emit('create-grade', response.data)
        showAddStudentDialog.value = false
        clearform()
    }catch(e){
        console.error(e)
    }
}

const grade_type = [
    {value:1, label:'Quiz'},
    {value:2, label:'Examination'},
    {value:3, label:'Activity'},
]

const policeAlert = computed(() => {
  return form.score > form.max_score

})

onMounted(() => {
    const route = useRoute()
    form.enrollment_id = route.params.enroll_id
    form.subject = route.params.subj_id
})

</script>

<template>
    <Dialog :open="showAddStudentDialog" @update:open="showAddStudentDialog = false">
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
                        <Label for="subjectName">Grade Type</Label>
                        <Multiselect v-model="form.type"  :options="grade_type" placeholder="Pick one" />
                    </div>
                    <div>
                        <Label for="studno">Grade Name</Label>
                        <Input v-model="form.name" id="studno" placeholder="Midterm Exam" required />
                    </div>
                    <div class="flex gap-2">
                        <div class="grow">
                            <Label for="score">Score</Label>
                            <Input v-model="form.score" type="number" placeholder="85" id="score" required />
                        </div>
                        <div class="grow">
                            <Label for="score">Max Score</Label>
                            <Input v-model="form.max_score" type="number" placeholder="100" id="score" required />
                        </div>

                    </div>
                    <p v-if="policeAlert" class="text-red-400 text-sm">Max Score cannot be lower than the Score.</p>
                </div>
                <DialogFooter>
                    <Button type="submit">Add Grade</Button>
                </DialogFooter>
            </form>
        </DialogContent>
    </Dialog>


</template>