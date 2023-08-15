<template>
<div v-if="picks !== [] && draft !== {}">
  <header class="fixed-header grid grid-cols-3 mb-3 mt-2">
    <div v-if="timerActive" class="flex ml-24 px-16">
      <h1 class="text-8xl text-white">{{ formattedTime }}</h1>
    </div>
    <div v-else class="flex ml-24 px-16">
      <h1 class="text-8xl text-white">00:00</h1>
    </div>
    <div class="flex ml-24 px-16 items-center">
      <h1 class="text-5xl text-team font-semibold text-center">{{ draft.name.trim() }}</h1>
    </div>
    <div class="flex justify-end">
      <div class="flex flex-col px-16 justify-end mr-16">
        <h1 class="text-5xl text-team font-semibold">Round {{ draft.round }}</h1>
        <h2 class="flex justify-end text-xl text-gray-500 mr-3"> of 16</h2>
      </div>
    </div>
  </header>
  <div class="draft-board flex px-10 justify-around">
    <div v-for="(column, columnIndex)  in picks" :key="columnIndex" class="flex-col items-stretch w-full">
      <div v-if="teams[columnIndex]" class="draft-header-container">
        <div class="draft-user-header flex justify-center">
          <div class="header-text mt-3 mb-3 text-team">{{ teams[columnIndex].name.trim() }}</div>
        </div>
      </div>
      <div v-else class="draft-header-container">
        <div class="draft-user-header flex justify-center">
          <div class="header-text mt-3 mb-3 text-team">Team {{ columnIndex + 1 }}</div>
        </div>
      </div>
      <div class="flex flex-col">
        <div v-for="(pick, pickNumber) in column" :key="pickNumber" class="">
          <div class="bg-secondary rounded-md mt-0.5 ml-0.5">
            {{pick}}
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<div v-else class="flex justify-center items-center h-screen">
  <div class="text-5xl text-white ">
    <p>Loading...</p>
  </div>
</div>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
      const picks = ref([[1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8]]);
      const draft = ref({name: 'test'});
      const teams = ref([{name: "Trever"}, {name: "Tristen"}]);
    return {
        picks,
        draft,
        teams
    }
  }
}
</script>

<style>
.fixed-header {
  position: sticky;
  z-index: 100;

}

</style>