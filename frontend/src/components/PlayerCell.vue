<template>
<div v-if="pick" :class="calculateBG(pick.position)" 
class="cell py-2 rounded-xl px-2 h-[100px]">
  <div class="player flex flex-row">
    <div>
      <div class="text-pick-text player-name font-bold">
        {{ pick.name.split(" ")[0].charAt(0 ) }}. {{ pick.name.split(" ")[1] }}
      </div>
      <div class="text-pick-position">
        {{ pick.position }} <a class="font-bold">-</a> {{ pick.football_team }}
      </div>
      <div class="mt-3">
      <div class="cell-direction-wrap picked">
        <i :class="calculateArrow(pickNumber, columnIndex)"  class="fa-sharp fa-solid ml-2 py-0.5"></i>
      </div>
    </div>
  </div>
    <div class="flex-1">
      <span class="flex justify-end font-semibold opacity-70 text-pick-number font-muli">
        {{ calculatePick(pickNumber, columnIndex, true) }}
      </span>
      <div class="avatar-player flex justify-end">
        <img class="w-[75px] h-[64px]" :src="pick.icon"/>
      </div>
    </div>
  </div>
</div>
<div v-else>
  <div :class="calculateHighlight(columnIndex, pickNumber) ? 'highlighted': ''" class="bg-secondary rounded-xl ml-1 mt-1 py-2 px-2 h-[100px]">
    <div class="player grid grid-cols-2 grid-rows-3">
      <div class="col-start-1"></div>
      <div class="col-start-1 row-start-2"></div>
      <div class="col-start-1 mt-1 row-start-3 cell-direction-wrap not-picked">
        <i :class="calculateArrow(pickNumber, columnIndex)"  class="fa-sharp fa-solid ml-2"></i>
      </div>
      <div class="flex justify-end font-semibold opacity-70 text-pick-number font-muli">
        {{ calculatePick(pickNumber, columnIndex, true)}}
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  props: {
    pickNumber: {
      type: Number
    },
    columnIndex: {
      type: Number
    },
    pickSetting: {
      type: Boolean,
      default: false,
    },
    pick: {
      type: Object,
    },
    draft: {
      type: Object
    },
    picks: {
      type: Array
    }
  },
  methods: {
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
    calculateBG(pos){
      switch (pos) {
        case 'RB': return 'bg-pick-rb';
        case 'WR': return 'bg-pick-wr';
        case 'K': return 'bg-pick-k';
        case 'QB': return 'bg-pick-qb';
        case 'TE': return 'bg-pick-te';
        case 'D/ST': return 'bg-pick-d/st';

        default: return 'bg-secondary'
      }
    },
    calculatePick(roundIndex, teamIndex, roundByRound) {
      if (!roundByRound){
        if (roundIndex % 2 == 0) {
          return roundIndex * this.draft.teams + teamIndex + 1;
        }
        return (roundIndex + 1) * this.draft.teams - teamIndex;
      }
      const pickNumber = roundIndex % 2 === 0 ? teamIndex + 1 : this.draft.teams - teamIndex;
      return `${roundIndex + 1}.${pickNumber}`;
    },
    calculateArrow(roundIndex, teamIndex) {
      roundIndex += 1;
      teamIndex += 1;
      if (roundIndex && roundIndex % 2 == 1) {
        if (teamIndex == this.draft.teams){
          return 'fa-arrow-down'
        }
      }
      if (roundIndex && roundIndex % 2 == 0) {
        if (teamIndex == 1){
          return 'fa-arrow-down'
        }
        return 'fa-arrow-left'
      }
      return 'fa-arrow-right'
    }
  },
  setup () {

    return {

    }
  }
}
</script>

<style scoped>

.picked {
  color: #00131F;
  opacity: 0.5;
}

.not-picked {
  color: #fefeff; 
  opacity: 0.7;
} 

</style>