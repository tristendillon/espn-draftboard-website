<template>
  <div class="flex items-center justify-center h-screen">
    <div class="bg-white p-6 rounded-lg shadow-md max-w-7xl mt-5">
      <h1 class="text-5xl font-semibold mb-4 text-center">Thank you for using FFDraftBoard!</h1>
      <div class="text-3xl mt-10">
        FFDraftBoard is the best way to improve your league's draft day experience. Install the Google Chrome extension and enjoy a live draft board which automatically updates as your draft happens 
      </div>
      <div class="text-3xl mt-5 text-center">Link to extension goes here</div>
      <div class="text-3xl mt-10"> 
        Support the product by donating to the below venmo or cashapp. Your donation will help support server and development costs and keep the product free to use!
      </div>
      <div class="mt-10 flex flex-row justify-around mb-5">
        <div class="flex flex-col">
          <div class="text-2xl text-center mb-5">CashApp</div>
          <img src="public/FFdraftCashApp.png" alt="cashapp" />
        </div>
        <div class="flex flex-col">
          <div class="text-2xl text-center mb-5">Venmo</div>
          <img src="public/FFdraftVenmo.png" alt="venmo" />
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  setup() {
    return {};
  },
};
</script>