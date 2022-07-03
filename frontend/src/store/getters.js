import { baseURL } from "@/axios"
export default {
    thumbnail: (state) =>
    {
        if (state.user)
            return baseURL + state.user.thumbnail
        return null
    },
    avatar: (state) =>
    {
        if (state.user)
            return baseURL + state.user.avatar
        return null
    },
    role: (state) =>
    {
        if (state.user)
            return state.user.role
        return null
    },
}
