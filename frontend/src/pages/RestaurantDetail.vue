<template>
    <div class="w-screen flex justify-center p-4">
        <div class="max-w-4xl block w-full">

            <div>
                <div>
                    <h1 class="text-4xl mb-4 font-bold text-gray-900">{{ restaurant.name }}</h1>
                </div>
                <div>
                    <h3 class="text-2xl mb-4 font-bold text-gray-900">Menu</h3>
                    <div class="grid space-y-4">
                        <div v-for="(category, catKey) in  restaurant.menu?.categories" :key="catKey" class="border border-gray-300 rounded-md p-3">
                           <h4 class="text-xl mb-4 font-bold text-gray-900">{{ category.name }}</h4>
                            <!-- Hero image -->
                            <div v-for="(product, pKey) in category.productIds" :key="pKey" class="flex justify-between">
                               <div> {{ restaurant.menu.products[product].name }}</div>  <div>{{ (restaurant.menu.products[product].variants[0].prices.delivery / 100).toFixed(2) }} €</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>


    </div>
</template>
<script>
export default {
    data() {
        return {
            restaurant: null
        }
    },
    methods: {
        async getRestaurantByprimarySlug() {
            const primarySlug = this.$route.params.primarySlug;
            var data = await this.$api.restaurant.getBySlug(primarySlug)
            this.restaurant = data
        },
        formatHero(imgURL) {
            //input https://res.cloudinary.com/tkwy-prod-eu/image/upload/{parameters}/v1705766275/static-takeaway-com/images/chains/de/cigkoftem/headers/header
            //https://res.cloudinary.com/tkwy-prod-eu/image/upload/c_thumb,h_240/f_auto/q_auto/dpr_2.0/v1705766085/static-takeaway-com/images/chains/de/cigkoftem/headers/header
            return imgURL.replace('{parameters}', 'c_thumb,h_240/f_auto/q_auto/dpr_2.0')
        }
    },
    created() {
        this.getRestaurantByprimarySlug();
    }
}
</script>