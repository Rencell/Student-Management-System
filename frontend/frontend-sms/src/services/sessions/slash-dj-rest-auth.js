import axios from 'axios';

const CSRF_COOKIE_NAME = 'csrftoken';
const CSRF_HEADER_NAME = 'X-CSRFToken';

const session = axios.create({
  baseURL: import.meta.env.PROD
    ? "https://student-management-system-rmww.onrender.com/dj-rest-auth"
    : "/dj-rest-auth",
  xsrfCookieName: CSRF_COOKIE_NAME,
  xsrfHeaderName: CSRF_HEADER_NAME,
  withCredentials: true,
});

export default session;