<script setup>
import Scaffold from '@/components/layout/scaffold.vue';
import { Card, CardContent, CardIcon, CardFooter, CardHeader, CardTitle, CardSubtitle } from '@/components/ui/card';
import { Users, BookOpen, GraduationCap } from 'lucide-vue-next';
import { Badge } from '@/components/ui/badge';
import gradeService from '@/services/grades/grade';
import studentService from '@/services/student/student';
import subjectService from '@/services/subject/subject';
import { Spinner } from '@/components/ui/spinner';
import { onMounted, ref } from 'vue';

const loading_top_performer = ref(false)
const loading_recent_student = ref(false)

const list_top_performer = ref([])
const retrieve_top_performer = async() => {
  loading_top_performer.value = true
  try{
    const response = await gradeService.retrieve_top_perform();
    list_top_performer.value = response.data.grade
  }catch(e){
    console.error(e)
  }finally{
    loading_top_performer.value = false
    
  }
}
const list_recent_performer = ref([])
const retrieve_recent_performer = async() => {
  loading_recent_student.value = true
  try{
    const response = await studentService.list_students();
    list_recent_performer.value = response.data
    loading_recent_student.value = false
  }catch(e){
    console.error(e)
  }finally{
    loading_recent_student.value = false
  }
}
const student_total = ref()
const total_count_student = async() => {
  try{
    const response = await studentService.total_count();
    student_total.value = response.data.count;
    
  }catch(e){
    console.error(e)
  }
}
const subject_total = ref()
const total_count_subject = async() => {
  try{
    const response = await subjectService.total_count();
    subject_total.value = response.data.count;
    
  }catch(e){
    console.error(e)
  }
}
const grade_percentage = ref()
const total_percentage_grade = async() => {
  try{
    const response = await gradeService.total_percentage();
    grade_percentage.value = response.data.percentage ;
    
  }catch(e){
    console.error(e)
  }
}
onMounted(() => {
  retrieve_top_performer()
  total_count_student()
  total_count_subject()
  total_percentage_grade()
  retrieve_recent_performer()
})
</script>

<template>
  <Scaffold>
    <p class="text-2xl font-bold pb-5 text-card-foreground">Dashboard</p>
    <div class="flex flex-col gap-3">
      <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        <Card>
          <CardHeader>
            <CardTitle>Total Students</CardTitle>
            <CardIcon>
              <Users :size="17"></Users>
            </CardIcon>
          </CardHeader>
          <CardContent>
            <div class="text-4xl font-bold">{{student_total || 0}}</div>
          </CardContent>
          <CardFooter>
            <div>Number of registered students</div>
          </CardFooter>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Total Subjects</CardTitle>
            <CardIcon>
              <BookOpen :size="17"></BookOpen>
            </CardIcon>
          </CardHeader>
          <CardContent>
            <div class="text-4xl font-bold">{{subject_total || 0}}</div>
          </CardContent>
          <CardFooter>
            <div>Number of written subjects</div>
          </CardFooter>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Average Grade</CardTitle>
            <CardIcon>
              <GraduationCap :size="17"></GraduationCap>
            </CardIcon>
          </CardHeader>
          <CardContent>
            <div class="text-4xl font-bold">{{grade_percentage || 0}}%</div>
          </CardContent>
          <CardFooter>
            <div>Overall student performance</div>
          </CardFooter>
        </Card>
      </div>

      <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle size="xl2">
              Top Performer Students
              <CardSubtitle class="pt-2">View and manage your students</CardSubtitle>
            </CardTitle>
            <CardIcon>
              <Users :size="17"></Users>
            </CardIcon>
          </CardHeader>
          <CardContent>
            <div v-if="loading_top_performer" class="flex justify-center items-center">
              <Spinner class="border-primary">Loading Data...</Spinner>
            </div>
            <div v-else>
              <Card class="mb-3" v-for="top_performer in list_top_performer" :key="top_performer.id">
                <CardHeader>
                  <CardTitle size="lg">
                    {{top_performer.student_name}}
                    <CardSubtitle></CardSubtitle>
                  </CardTitle>
                  <CardIcon>
                    <Badge :value="top_performer.percentage"> {{(top_performer.percentage).toFixed(2)}} %</Badge>
                  </CardIcon>
                </CardHeader>
              </Card>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle size="xl2">
              Recent Students
              <CardSubtitle class="pt-2">View and manage your students</CardSubtitle>
            </CardTitle>
            <CardIcon>
              <Users :size="17"></Users>
            </CardIcon>
          </CardHeader>
          <CardContent>

            <div v-if="loading_recent_student"  class="flex justify-center items-center">
              <Spinner class="border-primary">Loading Data...</Spinner>
            </div>
            <div v-else>
              <Card class="p-3 mb-3" v-for="liststudent in list_recent_performer" :key="liststudent.id">
                <CardTitle size="lg">
                  {{liststudent.name}}
                  <CardSubtitle>{{liststudent.email}}</CardSubtitle>
                </CardTitle>
              </Card>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  </Scaffold>

</template>

<style scoped></style>
