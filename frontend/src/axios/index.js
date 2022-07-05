import axios from "axios"
import store from "../store"

const baseURL = "//review-trello.azurewebsites.net"
axios.defaults.baseURL = baseURL
// axios.defaults.withCredentials = true

let refresh = false


const privateAxios = axios.create({ baseURL })
const token = JSON.parse(localStorage.getItem('token'))
if (token) {
    privateAxios.defaults.headers.common["Authorization"] = "Bearer " + token.access;
} else {
    privateAxios.defaults.headers.common["Authorization"] = "";
}

privateAxios.interceptors.response.use(resp => resp, async error =>
{
    const token = JSON.parse(localStorage.getItem('token'))
    if (error.response.status === 401 && !refresh && token) {
        refresh = true;
        const { status, data } = await axios.post('api/token/refresh/', { refresh: token.refresh });

        if (status === 200) {
            privateAxios.defaults.headers.common['Authorization'] = `Bearer ${data.access}`;
            store.commit("setToken", data)
            error.config.headers["Authorization"] = `Bearer ${data.access}`
            return privateAxios(error.config);
        }
    }
    refresh = false;
    return error;
});


export { privateAxios, baseURL }
