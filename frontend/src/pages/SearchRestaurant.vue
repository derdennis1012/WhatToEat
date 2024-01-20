<template>
      <div class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80" aria-hidden="true">
        <div class="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#f79533] to-[#b81d18] opacity-30 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]" style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)" />
      </div>
  <div class="h-screen bg-yellow-150 w-screen flex flex-wrap justify-center items-center px-20">

    <div class="w-full">
      <h1 class="text-4xl text-center mb-4 font-bold text-gray-900">Ready for Lunch break?</h1>
      <p class="text-center text-gray-500 mb-5">Find the best restaurants near you and order with your workmates!</p>

      <label for="default-search" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Let's deliver</label>
      <div class="relative">
        <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
          <svg class="w-4 h-4 text-gray-500 " aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
            viewBox="0 0 20 20">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
          </svg>
        </div>
        <input type="search" id="default-search"
        @keyup.enter="searchRestaurant"
          v-model="postcode"
          class="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-yellow-500 focus:border-yellow-50"
          placeholder="Just enter the Postcode of your office to continue" required>
        <button type="submit"
          class="text-white absolute end-2.5 bottom-2.5 bg-yellow-400 hover:bg-yellow-500 focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-sm px-4 py-2 " @click="searchRestaurant">Let's go</button>
      </div>
    </div>

  </div>
</template>


<script>

export default {
  data() {
    return {
      postcode: '',
    }
  },
  methods: {
    searchRestaurant() {
      //validate postcode
      if (this.postcode.length < 4) {
        alert('Please enter a valid postcode');
        return;
      }
      //redirect to restaurant list
      this.$router.push({ name: 'RestaurantList', params: { postcode: this.postcode } });
    }  
  }

}
</script>