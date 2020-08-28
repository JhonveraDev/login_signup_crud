<template>
    <div class="background">
        <div class="login-form-container card">
            <div class="card-body">
                <form enctype="multipart/form-data" method="POST" >
                    <input type="hidden" name="csrfmiddlewaretoken" :value="csrf" /> 
                    <div class="form-group">
                        <label for="username">Email: </label>
                        <input id="username" name="username" type="email" v-model="email" class="form-control" required />
                    </div>
                    <div class="form-group">
                        <label for="password">Password: </label>
                        <input id="password" name="password" type="password" v-model="password" class="form-control" required />
                    </div>
                    <button type="submit" class="btn btn-primary">Log in</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: () => ({
        csrf: document.head.querySelector('meta[name="csrf-token"]').content,
        email: '',
        password: ''
    }),
}
</script>

<style lang="scss" scoped>
    @import 'login.scss';
</style>