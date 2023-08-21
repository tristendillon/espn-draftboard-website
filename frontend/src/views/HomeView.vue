<template>
  <div class="flex items-center justify-center py-10 px-10">
    <div class="bg-secondary p-6 rounded-xl shadow-md max-w-6xl mt-5">
      <h1 class="text-5xl font-semibold mb-4 text-center font-muli text-pick-number opacity-75">Thank you for using FFDraftBoard!</h1>
      <div class="text-2xl mt-10 text-pick-arrow-normal text-center">
        FFDraftBoard is the best way to improve your league's draft day experience. <a class="text-blue-500" href="https://chrome.google.com/webstore/detail/ffdraftboard/ljnelhiofbippkmbeioamhnjihkecgbj" target="_blank">Install the Google Chrome extension</a> and enjoy a live draft board which automatically updates as your draft happens 
      </div>
      <div class="text-2xl text-center mt-10 text-pick-arrow-normal"> 
        Support the product by donating to the below venmo or cashapp. Your donation will help support server and development costs and keep the product free to use!
      </div>
      <div class="mt-10 flex flex-row justify-around mb-5 items-center">
        <div class="flex flex-col">
          <div class="text-2xl font-muli font-medium text-pick-number text-center mb-5"><a class="hover:text-blue-500" href="https://cash.app/$DraftBoard?qr=1" target="_blank">CashApp</a></div>
          <img src="/FFdraftCashApp.png" alt="cashapp" />
        </div>
        <!-- <div class="flex flex-col">
            <div class="text-xl font-muli font-medium text-pick-number text-center mb-5">
              <button @click="navigateToDrafts" class="bg-primary hover:bg-pick-position text-pick-number font-semibold py-2 px-4 rounded-xl shadow" ref="DraftsButton">Drafts</button>
            </div>
        </div> -->
        <div class="flex flex-col">
          <div class="text-2xl font-poppins font-medium text-pick-number text-center mb-5"><a class="hover:text-blue-500" href="https://venmo.com/code?user_id=2296110345355264909&cre" target="_blank">Venmo</a></div>
          <img class="w-[256px]" src="/FFdraftVenmo.png" alt="venmo" />
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  setup() {
    
    const navigateToDrafts = () => {
      window.location.href = `${window.location.href}drafts`;
    };

    return {
      navigateToDrafts
    };
  },
};
</script>
