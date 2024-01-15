
<template>
    <div class="flex min-h-full flex-1 flex-col justify-center py-12 sm:px-6 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=orange&shade=600" alt="Your Company" />
            <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account</h2>
        </div>
    
        <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-[480px]">
            <div class="bg-white px-6 py-12 shadow sm:rounded-lg sm:px-12">
                <div class="space-y-6">
                    <div>
                        <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
                        <div class="mt-2">
                            <input id="email" name="email" type="email" autocomplete="email" v-model="email" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-orange-600 sm:text-sm sm:leading-6"
                            />
                        </div>
                    </div>
    
                    <div>
                        <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
                        <div class="mt-2">
                            <input id="password" name="password" type="password" v-model="password" autocomplete="current-password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-orange-600 sm:text-sm sm:leading-6"
                            />
                        </div>
                    </div>
    
                    <div class="flex items-center justify-between">
                        <div class="flex items-center">
                            <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-orange-600 focus:ring-orange-600" />
                            <label for="remember-me" class="ml-3 block text-sm leading-6 text-gray-900">Remember me</label>
                        </div>
    
                        <div class="text-sm leading-6">
                            <a href="#" class="font-semibold text-orange-600 hover:text-orange-500">Forgot password?</a>
                        </div>
                    </div>
    
                    <div>
                        <button @click="loginUser" class="flex w-full justify-center rounded-md bg-orange-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-orange-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-orange-600">Sign in</button>
                    </div>
                </div>
            </div>
    
            <p class="mt-10 text-center text-sm text-gray-500">
                Not a registered yet? {{ ' ' }}
                <a href="#" class="font-semibold leading-6 text-orange-600 hover:text-orange-500">Ask your admin to set up your account</a>
            </p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            email: '',
            password: '',
        }
    },
    methods: {
        async loginUser() {
            try {
                var user = this.$api.auth.login(
                    {
                        email:"hshshsh@gmail.com",
                        password:"1012db"
                    }
                )
                console.log(user)

            } catch (error) {
                console.log(error)
            }
        },
    },
    created() {
        console.log(this.$api)
    },
}
</script>