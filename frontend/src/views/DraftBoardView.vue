<template>
<div v-if="picks !== [] && draft !== null">
  <div class="fixed-header flex flex-row justify-center" v-scroll-transform="{}">
    <div v-if="timerActive" class="flex items-center">
      <Timer :timer="timer" />
    </div>
    <div class="flex ml-24 px-16 items-center justify-center">
      <h1 class="ld:text-4xl md:text-2xl sm:text-xl text-team font-semibold text-center">{{ draft.name.trim() }}</h1>
    </div>
    <div class="flex flex-justify-end flex-col">
        <h1 class="ld:text-4xl md:text-2xl sm:text-xl text-team font-semibold">Round {{ draft.round }}</h1>
        <h2 class="flex justify-end text-xl text-gray-500 mr-3"> of 16</h2>
    </div>
  </div>
  <div class="draft-board flex px-10 justify-around absolute">
    <div v-for="(column, columnIndex) in picks" :key="columnIndex" class="flex-col items-stretch w-[200px]">
      <div v-if="teams[columnIndex]" class="draft-header-container relative" v-y-transform="calculateTransformY">
        <div class="draft-user-header flex justify-center">
          <div class="header-text mt-3 mb-3 text-team">{{ teams[columnIndex].name.trim() }}</div>
        </div>
      </div>
      <div v-else class="draft-header-container">
        <div class="draft-user-header flex justify-center">
          <div class="header-text mt-3 mb-3 text-team">Team {{ columnIndex + 1 }}</div>
        </div>
      </div>
      <div class="flex flex-col w-min-[120px]">
        <div v-for="(pick, pickNumber) in column" :key="pickNumber" class="">
          <div class="mt-1 ml-1 rounded-xl">
            <PlayerCell :pickNumber="pickNumber" :columnIndex="columnIndex" :pick="pick" :draft="draft" :picks="picks"/>
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
import { ref, onMounted } from 'vue';
import PlayerCell from '../components/PlayerCell.vue';
import Timer from '../components/Timer.vue';
import { fetchDraft, fetchPicks, fetchTeams} from '../apis/index.js';

export default {
  computed: {
    calculateTransformY(){
      const windowWidth = window.innerWidth;
      let translateYValue = 67;
      
      if (windowWidth < 1100) {
        translateYValue = 109;
      }
      if (windowWidth < 800) {
        translateYValue = 88;
      }

      return { translateY: translateYValue };
    },
    timerActive() {
      if (this.timer && this.timer.minutes !== null && this.timer.seconds !== null) {
        return true;
      }
      return false;
    },
  },
  setup() {
    const picks = ref([]);
    const draft = ref(null);
    const teams = ref([]);
    const timer = ref({started: false});
    const id = new URL(window.location.href).searchParams.get("id");
    
    const calculateArrayPosition = (pickRound, pickNumber) => {
      let x;
      const y = pickRound - 1;
      if (pickRound % 2 == 1) {
        x = pickNumber - 1;
      } else {
        x = draft.value.teams - pickNumber; 
      }
      return [x, y];
    };
    const notNullLength =((column) =>{
      let length = 0;
      for (const pick of column){
        if (pick){
          length++;
        }
      }
      return length;
    });
    const calculateRound = (() => {
      const startColumn = picks.value[0];
      const endColumn = picks.value[picks.value.length - 1];
      const round = Math.min(notNullLength(startColumn), notNullLength(endColumn));
      if (round == draft.value.roster_spots) {
        timer.value.minutes = 0;
        timer.value.seconds = 0;
        clearInterval(interval.value);
        return draft.value.roster_spots;
      }
      return round + 1;
    });

    onMounted(async () => {
      const authToken = process.env.BEARER_TOKEN;

      const fetchedDraft = await fetchDraft(id, authToken);
      const fetchedTeams = await fetchTeams(id, authToken);
      const fetchedPicks = await fetchPicks(id, authToken);

      console.log(fetchedDraft);
      console.log(fetchedTeams);
      console.log(fetchedPicks);

      draft.value = fetchedDraft[0];
      teams.value = fetchedTeams;

      timer.value.minutes = draft.value.minutes;
      timer.value.seconds = draft.value.seconds;
      for (let i = 0; i < draft.value.teams; i++) {
        const column = []
        for (let j = 0; j < draft.value.roster_spots; j++) {
          column.push(null)
        } 
        picks.value.push(column);
      }

      for (const pick of fetchedPicks) {
        const [x, y] = calculateArrayPosition(pick.pick_round, pick.pick_number);
        picks.value[x][y] = pick;
        //console.log(pick);
      }
      draft.value.round = calculateRound();

      const ws = new WebSocket('ws://localhost:5000');
    }); 

    return {
      picks,
      draft,
      teams,
      timer
    };
  },
  components: { PlayerCell, Timer }
}
</script>

<style>
.fixed-header {
  position: sticky;
  top: 0;
  background: #030617;
  z-index: 100; 
}

.draft-header-container {
  position: sticky;
  top: 0;
  background: #030617;
  z-index: 99; 
}


</style>