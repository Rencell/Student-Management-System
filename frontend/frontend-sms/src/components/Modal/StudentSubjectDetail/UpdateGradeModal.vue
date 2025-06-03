<script setup>
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import Multiselect from '@vueform/multiselect'
import '@vueform/multiselect/themes/default.css'
import { computed, onMounted, reactive, ref, watch } from 'vue';
import Button from '@/components/ui/button/Button.vue';
import gradeService from '@/services/grades/grade';

const emit = defineEmits(['update-grade'])


const form = reactive({
    name: "",
    score: null,
    max_score: null,
    type: null,
    enrollment_id: null,
    percentage: null
})

const showEditStudentDialog = defineModel(
    'open', { default: false },
)
const props = defineProps({
    id: Number,
})


const grade_info = ref([])
watch(showEditStudentDialog, async (newVal) => {
    if (newVal) {
        try {
            const response = await gradeService.list_grades(props.id)
            grade_info.value = response.data
        } catch (e) {
            console.log(e)
        }
    }
})

const submit = async () => {

    if (policeAlert.value)
        return;

    try {
        const response = await gradeService.update_grade(props.id,grade_info.value)
        showEditStudentDialog.value = false
        emit('update-grade', response.data)
    } catch (e) {
        console.error(e)
    }
}

const policeAlert = computed(() => {
  return grade_info.value.score > grade_info.value.max_score


})

</script>




<template>


    <Dialog v-model:open="showEditStudentDialog" @update:open="showEditStudentDialog = false">
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
                        <Label for="studno">Grade Name</Label>
                        <Input v-model="grade_info.name" id="studno" placeholder="Midterm Exam" required />
                    </div>
                    <div class="flex gap-2">
                        <div class="grow">
                            <Label for="score">Score</Label>
                            <Input v-model="grade_info.score" @input="onScoreInput" type="number" placeholder="85" id="score" required />
                        </div>
                        <div class="grow">
                            <Label for="score">Max Score</Label>
                            <Input v-model="grade_info.max_score" @input="onScoreInput" type="number" placeholder="100" id="score" required />
                        </div>
                    </div>

                    <p v-if="policeAlert" class="text-red-400 text-sm">Max Score cannot be lower than the Score.</p>
                </div>
                <DialogFooter>
                    <Button type="submit">Update Grade</Button>
                </DialogFooter>
            </form>
        </DialogContent>
    </Dialog>
</template>