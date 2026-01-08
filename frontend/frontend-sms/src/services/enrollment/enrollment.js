import axios from "axios";

import session from "../sessions/slash-api";

const END_POINT = "/enrollment/";

const enrollmentService = {
    list_enrollment: () => session.get(END_POINT),
    retrieve_student: (id) => session.get(END_POINT + id),
    retrieve_enrollment: (stu_id, subj_id) => session.get(`${END_POINT}${stu_id}/${subj_id}`),
    retrieve_student_subject: (student_id) => session.post(END_POINT + 'retrieve_student_subject/', {
      student: student_id,
    }),
    retrieve_subject_student: (subject_id) => session.post(END_POINT + 'retrieve_subject_student/', {
      subject: subject_id,
    }),
    create_enrollment: (student_id, subject) => session.post(END_POINT, {
      student: student_id,
      subject: subject,
    }),
    delete_enrollment: (id) => session.delete(END_POINT + id + '/'),
    
};

export default enrollmentService;

