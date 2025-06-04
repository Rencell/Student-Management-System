<script setup>
import Scaffold from '@/components/layout/scaffold.vue';
import { Card, CardContent, CardIcon, CardFooter, CardHeader, CardTitle, CardSubtitle } from '@/components/ui/card';

import { CirclePlus, Search } from 'lucide-vue-next';
import { Table, TableBody, TableCell, TableCaption, TableFooter, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { computed, onMounted, reactive, ref } from 'vue';
import { useRoute, RouterLink } from 'vue-router'
import studentService from '@/services/student/student';
import addStudentModal from '@/components/Modal/StudentModal/addStudentModal.vue';
import Button from '@/components/ui/button/Button.vue';
import { Input } from '@/components/ui/input';
import { Spinner } from '@/components/ui/spinner';

const loading = ref(false)
const showAddStudentDialog = ref(false)

const datahere = ref([]);

const fyck = async () => {
  loading.value = true
  try {
    const response = await studentService.list_students();
    datahere.value = response.data;
  } catch (e) {
    console.error(e)
  } finally {
    loading.value = false
  }
}

const searchQuery = ref('')


const filteredData = computed(() => {

  const lowerCase = searchQuery.value.toLowerCase()
  return datahere.value.filter(student =>
    student.name.toLowerCase().includes(lowerCase) ||
    student.student_number.toLowerCase().includes(lowerCase)
  )
})

const createStudent = (value) => {
  datahere.value.push(value)
}


onMounted(() => {
  fyck();
})
</script>

<template>

  <addStudentModal v-model:open="showAddStudentDialog" @create-student="createStudent"></addStudentModal>

  <Scaffold>
    <div class="flex justify-between">
      <p class="text-2xl font-bold pb-5 text-card-foreground">Students</p>
      <Button @click="showAddStudentDialog = true">
        <CirclePlus :size="16"></CirclePlus>&nbsp;Add Student
      </Button>
    </div>
    <Card>
      <CardHeader>

        <CardTitle :size="'xl2'">
          Student Management
          <CardSubtitle>View and manage all student profiles</CardSubtitle>
        </CardTitle>

      </CardHeader>
      <CardContent>

        <Input v-model="searchQuery" placeholder="Search Students..." :icon="true">
        <Search></Search>
        </Input>

        <br>
        <Table class="">
          <TableCaption>
            <div v-if="loading" class="flex justify-center">
              <Spinner class="border-primary">Loading Data...</Spinner>

            </div>
            <p v-else>A list of your recent Students.</p>
          </TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead>Name</TableHead>
              <TableHead>ID</TableHead>
              <TableHead class="hidden sm:table-cell">Gender</TableHead>
              <TableHead :class="'text-right'">Actions</TableHead>
            </TableRow>
          </TableHeader>

          <TableBody v-for="student in filteredData" :key="student.id">
            <TableCell :class="'font-medium'">{{ student.name }}</TableCell>
            <TableCell class="text-ellipsis">{{ student.student_number }}</TableCell>
            <TableCell class="hidden sm:table-cell">{{ student.gender }}</TableCell>
            <TableCell :class="'text-right'">
              <RouterLink :to="{ name: 'studentdetail', params: { id: student.id ?? 1 } }">
                <Button>View</Button>
              </RouterLink>
            </TableCell>

          </TableBody>
        </Table>

      </CardContent>

    </Card>
  </Scaffold>


  <!-- Dialog Modal -->


</template>

<style>
.dark {

  .dp__theme_light {
    --dp-primary-color: #5271FF;
    --dp-primary-text-color: #ffffff;
    --dp-hover-color: #84C7EE;
    --dp-border-color: hsl(209, 33%, 16%);
    --dp-text-color: white;
    --dp-background-color: #131B25;
  }
}
</style>
