<template>
    <div class="home-container">
        <h1>Bienvenido a pruebaCRUD !</h1>
        <ClientsCRUD v-if="isAuthenticated" />
        <div v-else>Para crear clientes debes registrarte o iniciar sesión</div>
    </div>
</template>

<script>
    import ClientsCRUD from '../components/clientsCRUD/ClientsCRUD.vue';

    export default {
        components: {
            ClientsCRUD
        },
        data: () => ({
            csrf: document.head.querySelector('meta[name="csrf-token"]').content,
            email: '',
            password: '',
            isAuthenticated: false,
            userName: ''
        }),
        mounted: function () {
            this.isAuthenticated = window.isAuthenticated !== 'False';
            this.userName = window.userName;
        }
    }
</script>

<style lang="scss" scoped>
    @import 'home.scss';
</style>