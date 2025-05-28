<script setup>
import Scaffold from '@/components/layout/scaffold.vue';
import { Card, CardContent, CardIcon, CardFooter, CardHeader, CardTitle, CardSubtitle } from '@/components/ui/card';
import Button from '@/components/ui/button/Button.vue';
import { Badge } from '@/components/ui/badge';
import { CirclePlus, Trash, SquarePen, ArrowLeft } from 'lucide-vue-next';
import { RouterLink } from 'vue-router';





</script>


<template>
    <Scaffold>
        <p class="text-2xl font-bold pb-5 text-card-foreground">Students</p>

        <Card>
            <CardHeader class="border-b">

                <CardTitle :size="'xl'">
                    <Button variant="outline" size="sm"><ArrowLeft size="18"></ArrowLeft></Button>
                    &nbsp;
                    <span class="text-xl font-bold pb-5 text-card-foreground">Student Profile</span>
                    
                </CardTitle>

                <CardIcon>

                    <Button :variant="'outline'" :class="'mr-2'" size="sm">
                        <SquarePen :size="16"></SquarePen>&nbsp;Edit
                    </Button>
                    <Button :variant="'destructive'" size="sm">
                        <Trash :size="16"></Trash>&nbsp;Delete
                    </Button>
                </CardIcon>

            </CardHeader>
            <CardContent class="space-y-2">
                <p class="text-2xl font-semibold">Emma Thompson</p>
                <p class="text-sm text-muted-foreground">emma.thompson@example.com</p>

                <Badge :value="60">60%</Badge>
                <span class="text-sm text-muted-foreground">Average Grade</span>
                <br>
                <Badge :value="112">Grade: 10th</Badge>
                <Badge :value="92">Enrolled: 8/15/2023</Badge>
                <Badge :value="87">Subjects: 2</Badge>
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

                    <Button size="sm">
                        <CirclePlus :size="16"></CirclePlus>&nbsp;Add Subject
                    </Button>
                </CardIcon>

            </CardHeader>
            <CardContent>
                <Card class="my-2">
                    <CardHeader>
                        <CardTitle size="lg">
                            Mathematics
                            <CardSubtitle>Teacher: Dr. Robert Chen</CardSubtitle>
                        </CardTitle>
                        <CardIcon>
                            <Badge value="80">80%</Badge>
                            <RouterLink :to="{name : 'Studentsubjectdetail'}">

                                <Button :variant="'outline'" :class="'mr-2'" size="sm">
                                    <SquarePen :size="16"></SquarePen>
                                </Button>
                            </RouterLink>
                            <Button :variant="'destructive'" size="sm">
                                <Trash :size="16"></Trash>
                            </Button>
                        </CardIcon>
                    </CardHeader>
                </Card>
                
            </CardContent>
        </Card>
    </Scaffold>

</template>