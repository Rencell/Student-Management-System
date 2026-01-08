import axios from "axios";

import session from "../sessions/slash-api";

const END_POINT = "/subjects/";

const subjectService = {
    list_subjects: () => session.get(END_POINT),
    retrieve_subject: (id) => session.get(END_POINT + id),
    total_count: () => session.get(END_POINT + 'count/'),
    create_subject: (form) => session.post(END_POINT,
        {
            name: form.name,
            subject_code: form.subject_code
        }
    ),
    
};

export default subjectService;

