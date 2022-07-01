export default {
    initializeStore(state)
    {
        const has = JSON.parse(localStorage.getItem('token'))
        if (has) {
            state.token = JSON.parse(localStorage.getItem('token'))
            state.isAuthenticated = true
        }
    },
    setlistShoe(state, shoes)
    {
        state.listShoe = shoes;
    },
    setCategories(state, categories)
    {
        state.categories = categories;
    },
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
    setCart(state, items)
    {
        state.cart.items = items
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
    }
}
