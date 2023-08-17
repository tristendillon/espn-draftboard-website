<template>
<div id="main" >
<div v-if="picks !== [] && draft !== null">
  <div class="fixed-header flex flex-row justify-center" v-scroll-transform="{}">
    <div v-if="timerActive" class="flex items-center">
      <Timer :timer="timer" />
    </div>
    <div v-else class="flex justify-center items-center">
      <h1 class="ld:text-5xl md:text-3xl sm:text-xl text-white">00:00</h1>
    </div>
    <div class="flex ml-24 px-16 items-center justify-center">
      <h1 class="ld:text-4xl md:text-2xl sm:text-xl text-team font-semibold text-center">{{ draft.name.trim() }}</h1>
    </div>
    <div class="flex flex-justify-end flex-col">
        <h1 class="ld:text-4xl md:text-2xl sm:text-xl text-team font-semibold">Round {{ draft.round }}</h1>
        <h2 class="flex justify-end text-xl text-gray-500 mr-3"> of 16</h2>
    </div>
  </div>
  <div class="draft-board flex px-10 justify-around absolute py-5">
    <div v-for="(column, columnIndex) in picks" :key="columnIndex" class="flex-col items-stretch" :class="calculateWidth">
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
            <PlayerCell :pickNumber="pickNumber" :columnIndex="columnIndex" :pick="pick" :draft="draft" :highlighted="calculateHighlight(columnIndex, pickNumber)"/>
          </div>
        </div>
      </div>
    </div>
  </div>
  <BaseModal class="z-max" :modalActive="modalPopup" @close-modal="closePopup">
    <div class="p-4">
      <div class="text-center">
        <h2 class="text-2xl font-bold mb-2">Thanks for Using FFDraftBoard!</h2>
        <p class="text-gray-600 mb-4">Consider donating to help support the product and keep it ad free!</p>
      </div>

      <div class="flex justify-center space-x-6 mt-4">
        <img src="/FFdraftCashApp.png" alt="cashapp" class="w-40 h-40">
        <img src="/FFdraftVenmo.png" alt="venmo" class="w-40 h-40">
      </div>
    </div>
</BaseModal>

</div>
<div v-else class="flex justify-center items-center h-screen">
  <div class="text-5xl text-white ">
    <p>Loading...</p>
  </div>
</div>
</div>

</template>

<script>
import { ref, onMounted, onUnmounted, watch } from 'vue';
import PlayerCell from '../components/PlayerCell.vue';
import Timer from '../components/Timer.vue';
import BaseModal from '../components/BaseModal.vue';
import { fetchDraft, fetchPicks, fetchTeams, fetchTimer} from '../apis/index.js';

export default {
  computed: {
    calculateWidth () {
      const numberOfTeams = this.draft.teams;
      if (numberOfTeams < 10) {
        return "w-[230px]"
      }
      return "w-[210px]"

    },
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
      if (!this.timer.active){
        return false
      }
      if (this.timer && this.timer.minutes !== null && this.timer.seconds !== null) {
        return true;
      }
      return false;
    },
  },
  methods: {
    closePopup() {
      this.modalPopup = false;
    }, 
    calculateHighlight(x, y) {
      if (x == 0 && y == 0) { return true; }
      if (y % 2 == 0) {
        if (x == 0) { 
          if (this.picks[x][y -1 ]){
            return true
          }
          return false; 
        }
        if (this.picks[x - 1][y]){
          return true;
        }
        return false;
      } else{ 
        if (x == this.draft.teams - 1) { 
          if (this.picks[x][y -1 ]){
            return true
          }
          return false; 
        }
        if (this.picks[x + 1][y]){
          return true;
        }
      }
    },
  },  
  setup() {
    const modalPopup = ref(null);

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
        timer.value.active = false
        modalPopup.value = true;
        return draft.value.roster_spots;
      } 
      return round + 1;
    });

    onMounted(async () => {
      const [fetchedDraft, fetchedTeams, fetchedPicks, fetchedTimer] = await Promise.all([
        fetchDraft(id),
        fetchTeams(id),
        fetchPicks(id),
        fetchTimer(id)
      ]);

      modalPopup.value = true;
      // console.log(modalPopup);
      // console.log(fetchedDraft);
      // console.log(fetchedTeams);
      // console.log(fetchedPicks);
      // console.log(fetchedTimer);

      draft.value = fetchedDraft;
      teams.value = fetchedTeams;
      if (fetchedTimer) {
        timer.value.minutes = fetchedTimer.minutes;
        timer.value.seconds = fetchedTimer.seconds;
      }else{
        timer.value.minutes = 0;
        timer.value.seconds = 0;
      }

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

      const pickSocket = new WebSocket('wss://espndraftboard.com/ws/');
      const timerSocket = new WebSocket('wss://espndraftboard.com/ws/');

      pickSocket.onopen = ((event) => {
        //console.log("Pick Socket connection opened:", event);
      });

      pickSocket.onmessage = function(event) {
        const message = JSON.parse(event.data);
        const pick = message.message;
        if(pick.draft_id != id) {
          return;
        }
        const [x, y] = calculateArrayPosition(pick.pick_round, pick.pick_number);
        picks.value[x][y] = pick;
        draft.value.round = calculateRound();
        timer.value.started = false;
        timer.value.minutes = fetchedTimer.minutes;
        timer.value.seconds = fetchedTimer.seconds;
        draft.minutes = 0;
        //clearInterval(interval.value);
    };


      pickSocket.onclose = ((event) => {
        //console.log("Pick Socket connection closed:", event);
      });

      timerSocket.onopen = ((event) => {
        //console.log("Timer Socket connection opened:", event);
      });

      timerSocket.onmessage = ((event) => {
        const message = JSON.parse(event.data);
        timerData = message.message;
        if(timerData.draft_id != id) {
          return;
        }
        timer.value.minutes = timerData.minutes;
        timer.value.seconds = timerData.seconds;
        draft.value.minutes = timerData.minutes;
        draft.value.seconds = timerData.seconds;
      });

      timerSocket.onclose = ((event) => {
        //console.log("Timer Socket connection closed:", event);
      })


    }); 

    const setBodyOverflow = () => {
      if (modalPopup.value) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = '';
      }
    };

    watch(modalPopup, setBodyOverflow);

    onUnmounted(() => {
      document.body.style.overflow = '';
    })
    
    return {
      picks,
      draft,
      teams,
      timer,
      modalPopup
    };
  },
  components: { PlayerCell, Timer, BaseModal}
}
</script>

<style>
.fixed-header {
  position: sticky;
  top: 0;
  background: #030617;
  z-index: 99; 
}

.draft-header-container {
  position: sticky;
  top: 0;
  background: #030617;
  z-index: 98; 
}

.z-max {
  z-index: 100;
}
</style>  