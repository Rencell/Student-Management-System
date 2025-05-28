<script setup>
import Scaffold from '@/components/layout/scaffold.vue';
import { Card, CardContent, CardIcon, CardFooter, CardHeader, CardTitle, CardSubtitle } from '@/components/ui/card';
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import Label from '@/components/ui/label/Label.vue';
import Button from '@/components/ui/button/Button.vue';
import Input from '@/components/ui/input/input.vue';
import { CirclePlus, Search } from 'lucide-vue-next';
import { Table, TableBody, TableCell, TableCaption, TableFooter, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { ref } from 'vue';
import { useRoute, RouterLink } from 'vue-router'

const showAddSubjectDialog = ref(false)
</script>

<template>
  <Scaffold>
    <div class="flex justify-between">
      <p class="text-2xl font-bold pb-5 text-card-foreground">Students</p>
      <Button @click="showAddSubjectDialog = true">
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

        <div class="flex gap-2 items-center">
          <Search class="text-primary" :size="16"></Search>
          <Input :placeholder="'Search Students...'"></Input>
        </div>

        <br>
        <Table>
          <TableCaption>A list of your recent invoices.</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead>Name</TableHead>
              <TableHead>Email</TableHead>
              <TableHead>ID</TableHead>
              <TableHead :class="'text-right w-[100px]'">Subjects</TableHead>
              <TableHead :class="'text-right'">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
              <TableCell :class="'font-medium'">INV001</TableCell>
              <TableCell>Paid</TableCell>
              <TableCell>Credit Card</TableCell>
              <TableCell :class="'text-right'">$250.00</TableCell>
              <TableCell :class="'text-right'"><RouterLink :to="{ name: 'studentdetail' }"><Button>View</Button></RouterLink></TableCell>
            
          </TableBody>
        </Table>
      </CardContent>
    </Card>
  </Scaffold>


  <!-- Dialog Modal -->

  <Dialog :open="showAddSubjectDialog" @update:open="showAddSubjectDialog = false">
    <DialogContent>
      <DialogHeader>
        <DialogTitle>Add Student</DialogTitle>
        <DialogDescription>
          Add a new student to this list.
        </DialogDescription>
      </DialogHeader>
        <div class="grid gap-4 py-4">
          <div>
            <Label for="subjectName">Subject Name</Label>
            <Input id="subjectName" required />
          </div>
          <div>
            <Label for="subjectCode">Subject Code</Label>
            <Input id="subjectCode" required />
          </div>
        </div>
        <DialogFooter>
          <Button type="submit">Add Subject</Button>
        </DialogFooter>
    </DialogContent>
  </Dialog>
</template>

<style scoped></style>
