import router from '../router'
import axios from 'axios'
import { privateAxios } from '@/axios';
privateAxios
export default {
    fetchUser(context)
    {
        privateAxios.get("api/users/my/").then(
            res =>
            {
                context.commit('setUser', res.data)
            }
        )
    },
    fetchShoes(context)
    {
        return axios.get("shoes/").then(res =>
            context.commit("setlistShoe", res.data)
        ).catch((error) => console.log(error));
    },
    fetchCart(context)
    {
        return privateAxios.get("cart_details/").then(res =>
            context.commit("setCart", res.data)
        ).catch((error) => console.log(error));
    },
    fetchCategory(context)
    {
        return axios.get("categories/").then(res =>
            context.commit("setCategories", res.data)
        ).catch((error) => console.log(error));
    },
    fetchData(context)
    {
        context.dispatch("fetchCategory")
        context.dispatch("fetchShoes")
        if (context.state.isAuthenticated) {
            context.dispatch("fetchCart")
        }
    },
    login(context, user)
    {
        return axios
            .post("api/token/", user)
            .then(response =>
            {
                const token = response.data
                context.commit('setToken', token)
                axios.defaults.headers.common["Authorization"] = "Bearer " + token.access
                const toPath = router.history.current.query.to || '/'
                router.push(toPath)
            }).then(
                () =>
                {
                    privateAxios.get("api/users/my/").then(
                        res =>
                        {
                            context.commit('setUser', res.data)
                        }
                    )
                }
            )
    },
    signup(context, bodyFormData)
    {
        return axios
            .post("api/users/signup/", bodyFormData, { headers: { "Content-Type": "multipart/form-data" } })

    },
    refreshToken(context)
    {
        return axios.post('api/token/refresh/', { refresh: context.state.token.refresh })
            .then(res =>
                context.commit("setToken", res.data)
            ).catch(
                error => console.log(error)
            )
    }
}
