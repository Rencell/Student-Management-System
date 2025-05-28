<script setup>
import Scaffold from '@/components/layout/scaffold.vue';
import { Card, CardContent, CardIcon, CardFooter, CardHeader, CardTitle, CardSubtitle } from '@/components/ui/card';
import { Users, BookOpen, GraduationCap } from 'lucide-vue-next';
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
            <div class="text-4xl font-bold">11</div>
          </CardContent>
          <CardFooter>
            <div>Number of registered students</div>
          </CardFooter>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Average Grade</CardTitle>
            <CardIcon>
              <BookOpen :size="17"></BookOpen>
            </CardIcon>
          </CardHeader>
          <CardContent>
            <div class="text-4xl font-bold">11</div>
          </CardContent>
          <CardFooter>
            <div>Overall student performance</div>
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
            <div class="text-4xl font-bold">11</div>
          </CardContent>
          <CardFooter>
            <div>Overall student performance</div>
          </CardFooter>
        </Card>
      </div>

      <div>
        <Card>
          <CardHeader>
            <CardTitle size="xl2">
              Recent Studies
              <CardSubtitle class="pt-2">View and manage your students</CardSubtitle>
            </CardTitle>
            <CardIcon>
              <Users :size="17"></Users>
            </CardIcon>
          </CardHeader>
          <CardContent>
            <Card class="p-3 mb-3">
              <CardTitle size="lg">
                Recent Studies
                <CardSubtitle>View and manage your students</CardSubtitle>
              </CardTitle>
            </Card>
            <Card class="p-3 mb-3">
              <CardTitle size="lg">
                Recent Studies
                <CardSubtitle>View and manage your students</CardSubtitle>
              </CardTitle>
            </Card>
            <Card class="p-3 mb-3">
              <CardTitle size="lg">
                Recent Studies
                <CardSubtitle>View and manage your students</CardSubtitle>
              </CardTitle>
            </Card>
          </CardContent>
        </Card>
      </div>
    </div>
  </Scaffold>

</template>

<style scoped></style>
