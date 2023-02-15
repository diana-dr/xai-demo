import { createWebHistory, createRouter } from "vue-router";
import UserRanking from "@/components/UserRanking";

const routes = [
    {
        path: "/",
        name: "UserRanking",
        component: UserRanking,
    },

];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;