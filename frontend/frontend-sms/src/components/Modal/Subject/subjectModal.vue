<script setup>
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { onMounted, reactive, ref } from 'vue';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import Button from '@/components/ui/button/Button.vue';
import subjectService from '@/services/subject/subject';
const showEditStudentDialog = defineModel('open', { default: false })

const form = reactive({
    name: null,
    subject_code: null
})

const emit = defineEmits(['create-subject'])

const submit = async () => {
    try{
        const response = await subjectService.create_subject(form)
        showEditStudentDialog.value = false
        emit('create-subject', response.data)
    }catch(e){
        console.error(e)
    }
}

</script>


<template>
    <Dialog v-model:open="showEditStudentDialog" @update:open="showEditStudentDialog = false">
        <DialogContent>
            <DialogHeader>
                <DialogTitle>Add Student</DialogTitle>
                <DialogDescription>
                    Create subject on this list.
                </DialogDescription>
            </DialogHeader>
                <form @submit.prevent="submit">
                    <div class="grid gap-4 py-4">
                        <div>
                            <Label for="subjectName">Subject Name</Label>
                            <Input v-model="form.name" id="subjectName" placeholder="Mathematics" required />
                        </div>
                        <div>
                            <Label for="subjectCode">Subject Code</Label>
                            <Input v-model="form.subject_code" id="subjectCode" placeholder="Code" required />
                        </div>
                    </div>
                    <DialogFooter>
                        <Button type="submit">Add Subject</Button>
                    </DialogFooter>
                </form>
        </DialogContent>
    </Dialog>
</template>