import axios from "axios";

import session from "../sessions/slash-api";

const END_POINT = "/grades/";

const gradeService = {
    list_grade: () => session.get(END_POINT),
    retrieve_grades: (enrollment_id) => session.post(END_POINT + 'get_student_grade/', {enrollment_id}),
    list_grades: (grade_id) => session.get(END_POINT + grade_id),
    total_percentage: () => session.get(END_POINT + 'total_percentage/'),
    update_grade: (grade_id, form) => session.patch(END_POINT + grade_id + '/', {
        name:form.name, 
        score:form.score, 
        max_score: form.max_score, 
        enrollment_id:form.enrollment_id
    }),
    retrieve_grade_type: () => session.get(END_POINT + 'get_grade_type/'),
    create_grade: (form) => session.post(END_POINT, {
        name:form.name, 
        score:form.score, 
        max_score: form.max_score, 
        type:form.type, 
        subject:form.subject, 
        enrollment_id:form.enrollment_id
    }),
    retrieve_grade_average: (enrollment_id) => session.get(END_POINT + 'get-grade-average/', {
        params: {
            enrollment_id:enrollment_id
        }
        
    }),
    retrieve_grade_detail_student: (student_id) => session.get(END_POINT + 'get_average_by_detail_student/', {
        params: {
            student_id:student_id
        }
        
    }),
    retrieve_average_by_subject: (subject_id) => session.get(END_POINT + 'get_average_by_subject/', {
        params: {
            subject_id:subject_id
        }
        
    }),
    retrieve_overall_average: (enrollment_id) => session.get(END_POINT + 'get_overall_average/', {
        params: {
            enrollment_id:enrollment_id
        }
        
    }),
    delete_grade: (grade_id) => session.delete(END_POINT + grade_id + '/'),
    retrieve_top_perform: () => session.get(END_POINT + 'get_average_by_student/'),
    
};

export default gradeService;

