let token = null
let isAuthenticated = false
const has = JSON.parse(localStorage.getItem('token'))
if (has) {
    token = JSON.parse(localStorage.getItem('token'))
    isAuthenticated = true
}
export default {
    searchString: "",
    user: null,
    token,
    isAuthenticated
}
