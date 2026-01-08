
import session from "../sessions/slash-dj-rest-auth";


const authentication = {
    getUser: () => 
        session.get("/user/"),
    login: (username, password) => 
        session.post("/login/", {username, password}),
    logout: () => 
        session.post("/logout/", {}),
    setToken(token) {
        session.defaults.headers.common['Authorization'] = `Token ${token}`;
    },
    removeToken() {
        delete session.defaults.headers.common['Authorization'];
    }
    // register: (username, email, password1, password2) => 
    //     session.post('/registration/', {username, email, password1, password2}),
    // confirm_email: (key) => 
    //     session.post(`/registration/account-confirm-email/${key}/`, {key}),
};

export default authentication;