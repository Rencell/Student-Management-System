<script setup>
import scaffold from '@/components/layout/scaffold.vue';
import { Card, CardContent, CardIcon, CardFooter, CardHeader, CardTitle, CardSubtitle } from '@/components/ui/card';
import { Table, TableBody, TableCell, TableCaption, TableFooter, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Badge } from '@/components/ui/badge';
import { Trash, CirclePlus } from 'lucide-vue-next';
import Button from '@/components/ui/button/Button.vue';
</script>


<template>
    <div>
        <scaffold>
            <p class="text-2xl font-bold pb-5 text-card-foreground">Mathematics Grades</p>

            <div class="space-y-4">
                <Card>
                    <CardHeader class="border-b">
                        <CardTitle size="xl">Subject Information
                        </CardTitle>
                    </CardHeader>
                    <CardContent class="space-y-2">
                        <p class="text-2xl font-semibold">Emma Thompson</p>
                        <p class="text-sm text-muted-foreground">emma.thompson@example.com</p>
                        <Badge :value="80">80%</Badge> <span class="text-sm text-muted-foreground">Overall Average
                        </span>
                        <br>
                        <Badge :value="72">Subject: MATH101</Badge>
                        <Badge :value="67">Total Assessment: 3</Badge>
                    </CardContent>
                </Card>
                <!-- Quiz -->
                <Card>
                    <CardHeader>
                        <CardTitle size="xl2">Quiz
                            <CardSubtitle>Average: 85.0%</CardSubtitle>
                        </CardTitle>
                        <CardIcon>
                            <Button :class="'mr-2'" size="sm">
                                <CirclePlus :size="16"></CirclePlus>&nbsp;Add Quiz
                            </Button>
                        </CardIcon>
                    </CardHeader>

                    <CardContent>
                        <Table>
                            <TableCaption>A list of your recent invoices.</TableCaption>
                            <TableHeader>
                                <TableRow>
                                    <TableHead>Name</TableHead>
                                    <TableHead>Score</TableHead>
                                    <TableHead>Date</TableHead>
                                    <TableHead :class="'text-right'">Actions</TableHead>
                                </TableRow>
                            </TableHeader>
                            <TableBody>
                                <TableCell :class="'font-medium'">INV001</TableCell>
                                <TableCell>Paid</TableCell>
                                <TableCell>Credit Card</TableCell>
                                <TableCell :class="'text-right'">
                                    <RouterLink :to="{ name: 'studentdetail' }"><Button variant="destructive" size="sm"><Trash :size="17"></Trash></Button></RouterLink>
                                </TableCell>

                            </TableBody>
                        </Table>
                    </CardContent>
                </Card>
                <!-- Assignment -->
                <Card>
                    <CardHeader>
                        <CardTitle size="xl2">Assignment
                            <CardSubtitle>Average: 85.0%</CardSubtitle>
                        </CardTitle>
                        <CardIcon>
                            <Button :class="'mr-2'" size="sm">
                                <CirclePlus :size="16"></CirclePlus>&nbsp;Add Assignment
                            </Button>
                        </CardIcon>
                    </CardHeader>

                    <CardContent>
                        <Table>
                            <TableCaption>A list of your recent invoices.</TableCaption>
                            <TableHeader>
                                <TableRow>
                                    <TableHead>Name</TableHead>
                                    <TableHead>Score</TableHead>
                                    <TableHead>Date</TableHead>
                                    <TableHead :class="'text-right'">Actions</TableHead>
                                </TableRow>
                            </TableHeader>
                            <TableBody>
                                <TableCell :class="'font-medium'">INV001</TableCell>
                                <TableCell>Paid</TableCell>
                                <TableCell>Credit Card</TableCell>
                                <TableCell :class="'text-right'">
                                    <RouterLink :to="{ name: 'studentdetail' }"><Button variant="destructive" size="sm"><Trash :size="17"></Trash></Button></RouterLink>
                                </TableCell>

                            </TableBody>
                        </Table>
                    </CardContent>
                </Card>
                <!-- Activity -->
                <Card>
                    <CardHeader>
                        <CardTitle size="xl2">Activity
                            <CardSubtitle>Average: 85.0%</CardSubtitle>
                        </CardTitle>
                        <CardIcon>
                            <Button :class="'mr-2'" size="sm">
                                <CirclePlus :size="16"></CirclePlus>&nbsp;Add Activity
                            </Button>
                        </CardIcon>
                    </CardHeader>

                    <CardContent>
                        <Table>
                            <TableCaption>A list of your recent invoices.</TableCaption>
                            <TableHeader>
                                <TableRow>
                                    <TableHead>Name</TableHead>
                                    <TableHead>Score</TableHead>
                                    <TableHead>Date</TableHead>
                                    <TableHead :class="'text-right'">Actions</TableHead>
                                </TableRow>
                            </TableHeader>
                            <TableBody>
                                <TableCell :class="'font-medium'">INV001</TableCell>
                                <TableCell>Paid</TableCell>
                                <TableCell>Credit Card</TableCell>
                                <TableCell :class="'text-right'">
                                    <RouterLink :to="{ name: 'studentdetail' }"><Button variant="destructive" size="sm"><Trash :size="17"></Trash></Button></RouterLink>
                                </TableCell>

                            </TableBody>
                        </Table>
                    </CardContent>
                </Card>
            </div>
        </scaffold>
    </div>

</template>