
export default {

    setSearchString(state, text)
    {
        state.searchString = text
    },
    setToken(state, token)
    {
        state.token = token
        state.isAuthenticated = true
        localStorage.setItem("token", JSON.stringify(token))
    },
    setUser(state, user)
    {
        state.user = user
    },
    logout(state)
    {
        state.user = null
        state.token = null
        localStorage.setItem('token', null)
        state.isAuthenticated = false
        state.user = null
    }
}
