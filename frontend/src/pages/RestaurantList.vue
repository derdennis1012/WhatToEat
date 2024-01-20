<template>
    <div class="p-6">
        <div>
            <h1 key="title" class="text-4xl text-center mb-4 font-bold text-gray-900">Restaurants near {{
                $route.params.postcode }}</h1>
            <p key="subtitle" class="text-center text-gray-500 mb-5">Find the best restaurants near you and order with your
                workmates!</p>
        </div>
        <div class="flex justify-center w-full">
            <div v-if="loadedRestaurants" class="grid grid-cols-1 space-y-6  max-w-3xl">
                <div v-for="(restaurant, key) in loadedRestaurants" :key="key"
                    @click="(e) => openResturaunt(e,restaurant.primarySlug)"
                    class="border border-gray-400 overflow-hidden rounded-md">
                    <div>
                        <div class="relative top-0 w-full h-28">
                            <img :src="formatHero(restaurant.brand.heroImageUrl)" alt="logo" class="w-full h-full" />
                        </div>
                        <div class="flex justify-end right-3 relative top-0 -mt-6 z-10 ">
                            <div class="rounded-md shadow-md w-fit p-1  h-22 w-22 flex justify-center items-center">
                                <img :src="formatLogo(restaurant.brand.logoUrl)" alt="logo"
                                    class="h-20 w-auto bg-white  object-contain" />
                            </div>

                        </div>
                    </div>
                    <div class="relative -top-9">
                        <h2 class="text-2xl font-bold text-gray-900 px-4 py-2">{{ restaurant?.brand?.name }}</h2>
                        <!-- address -->
                        <div>
                            <p class="text-gray-500 px-4 py-2">{{ restaurant?.location?.streetAddress }} {{
                                restaurant?.location?.postalCode }} {{ restaurant?.location?.city }}</p>
                        </div>
                        <!--{ "id": "000PRO11", "primarySlug": "cigkoftem-freiburg", "indicators": { "isDeliveryByScoober": false, "isNew": false, "isTestRestaurant": false, "isGroceryStore": false, "isSponsored": false }, "priceRange": 0, "popularity": 0, "brand": { "name": "Cigköftem", "logoUrl": "https://res.cloudinary.com/tkwy-prod-eu/image/upload/{parameters}/v1705766403/static-takeaway-com/images/chains/de/cigkoftem/logo_465x320", "heroImageUrl": "https://res.cloudinary.com/tkwy-prod-eu/image/upload/{parameters}/v1705766403/static-takeaway-com/images/chains/de/cigkoftem/headers/header", "heroImageUrlType": "CHAIN", "branchName": "Freiburg" }, "cuisineTypes": [ "falafel_1256", "wrap_1416", "falafel_1215" ], "rating": { "votes": 48, "score": 4.2 }, "location": { "streetAddress": "Breisacher Strasse 145", "city": "Freiburg", "country": "DE", "lat": "48.0055831", "lng": "7.8273052", "timeZone": "Europe/Amsterdam" }, "supports": { "delivery": true, "pickup": true, "vouchers": true, "stampCards": false, "discounts": false }, "shippingInfo": { "delivery": { "isOpenForOrder": true, "isOpenForPreorder": true, "openingTime": null, "duration": 20, "durationRange": { "min": 20, "max": 30 }, "deliveryFeeDefault": 349, "minOrderValue": 4500, "lowestDeliveryFee": { "from": 0, "fee": 349 }, "dynamicDeliveryFeeInfo": { "expiryTime": null, "token": null } }, "pickup": { "isOpenForOrder": true, "isOpenForPreorder": true, "openingTime": null, "distance": { "unit": "m", "quantity": 8107 } } }, "paymentMethods": [ "sofort", "paypal", "creditcard", "giropay", "bitpay" ] } -->
                        <!-- is open  ? -->
                        <div class="flex justify-between pr-5">
                            <div>
                                <p v-if="restaurant?.shippingInfo?.delivery?.isOpenForOrder"
                                    class="text-green-500 px-4 py-2">Open</p>
                                <p v-else class="text-red-500 px-4 py-2">Closed</p>
                            </div>
                            <div>
                                <div v-if="loadedVotes[restaurant.primarySlug]" class="text-2xl font-bold">
                                    <h4>
                                        {{ loadedVotes[restaurant.primarySlug] }}
                                        <span class="text-xs">Vote</span>
                                    </h4>

                                </div>
                                <div>
                                    <button @click="(e) => {
                                        vote(e, restaurant.primarySlug)
                                    }" class="text-sm bg-orange-400 text-white rounded-md py-1 px-3 ">Vote</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="w-full flex py-3 px-3 items-center justify-center bg-orange-400 text-white rounded-md"
                    @click="resetVote">
                    Reset Vote
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'RestaurantList',
    data() {
        return {
            loadedRestaurants: null,
            loadedVotes: null
        }
    },
    methods: {
        async getVotes() {
            var data = await this.$api.votes.getAllVotes()
            this.loadedVotes = data
            this.sortRestaurants();
        },
        openResturaunt(e,slug) {
            //chekc if the vote button was clicked if yes dont redirect
            if (e.target.classList.contains('bg-orange-400')) {
                return;
            }
            this.$router.push({ name: 'RestaurantDetail', params: { primarySlug: slug } });
        },
        vote(e, slug) {
            e.preventDefault();
            this.$api.votes.addVote(slug)
            //update loadedVotes
            setTimeout(() => {
                this.getVotes();
            }, 300);
        },
        resetVote(e) {
            e.preventDefault();
            this.$api.votes.resetVote()
            //update loadedVotes
            this.getVotes();
        },
        async getRestaurants() {
            //get the postcode param 
            const postcode = this.$route.params.postcode;
            //check if postcode is valid if not redirect to search page
            if (postcode.length < 4) {
                this.$router.push({ name: 'SearchRestaurant' });
                return;
            }
            //get restaurants from api
            var data = await this.$api.restaurant.searchByPostalCode(postcode)
            console.log(data)
            this.loadedRestaurants = data.restaurants
        },
        sortRestaurants() {
            return;
            //sort by votes
            //set the voted resturants on top of the list
            //loadedresturants is an object
            var sorted = Object.entries(this.loadedRestaurants).sort((a, b) => {
                //a[0] is the key
                //a[1] is the value
                //b[0] is the key
                //b[1] is the value
                //check if a[0] is in loadedVotes
                if (this.loadedVotes[a[0]]) {
                    return -1
                }
                return 1
            })
            this.loadedRestaurants = sorted
        },
        formatLogo(logoUrl) {
            //input is like https://res.cloudinary.com/tkwy-prod-eu/image/upload/%7Bparameters%7D/v1705765848/static-takeaway-com/images/chains/de/cigkoftem/logo_465x320
            //outpul should be https://res.cloudinary.com/tkwy-prod-eu/image/upload/%7Bparameters%7D/v1705765848/static-takeaway-com/images/chains/de/cigkoftem/logo_465x320
            return logoUrl.replace('{parameters}', 'c_fill,f_auto,h_200,q_auto,w_200')
        },
        formatHero(imgURL) {
            //input https://res.cloudinary.com/tkwy-prod-eu/image/upload/{parameters}/v1705766275/static-takeaway-com/images/chains/de/cigkoftem/headers/header
            //https://res.cloudinary.com/tkwy-prod-eu/image/upload/c_thumb,h_240/f_auto/q_auto/dpr_2.0/v1705766085/static-takeaway-com/images/chains/de/cigkoftem/headers/header
            return imgURL.replace('{parameters}', 'c_thumb,h_240/f_auto/q_auto/dpr_2.0')
        }
    },
    created() {
        this.getRestaurants();
        this.getVotes();
    }
}
</script>