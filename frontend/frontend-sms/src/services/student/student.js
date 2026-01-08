import axios from "axios";

import session from "../sessions/slash-api";

const END_POINT = "/students/";

const studentService = {
    list_students: () => session.get(END_POINT),
    retrieve_student: (id) => session.get(END_POINT + id),
    total_count: () => session.get(END_POINT + 'count/'),
    create_student: (form) => session.post(END_POINT, 
        { name: form.name,
        student_number: form.student_number,
        gender: form.gender,
        email: form.email,
        date_of_birth: form.birth_date
    }),
    update_student: (num, form) => session.put(END_POINT + num + '/', 
        { name: form.name,
        student_number: form.student_number,
        gender: form.gender,
        email: form.email,
        date_of_birth: form.birth_date
    }),
    
};

export default studentService;

