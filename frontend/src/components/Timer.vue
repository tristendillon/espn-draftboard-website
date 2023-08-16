<template>
  <div class="flex justify-center items-center">
    <h1 class="ld:text-5xl md:text-3xl sm:text-xl text-white">{{ formattedTime }}</h1>
  </div>
</template>

<script>
export default {
  props: {
    timer: Object,
  },
  computed: {
    formattedTime() {
      const minutes = String(this.timer.minutes).padStart(2, '0');
      const seconds = String(this.timer.seconds).padStart(2, '0');
      return `${minutes}:${seconds}`;
    },
  },
  methods: {
    startCountdown() {
      this.interval = setInterval(() => {
        if (this.timer.minutes === 0 && this.timer.seconds === 0) {
          clearInterval(this.interval);
          // Timer has reached 00:00, you can perform any actions here
        } else {
          if (this.timer.seconds === 0) {
            this.timer.minutes--;
            this.timer.seconds = 59;
          } else {
            this.timer.seconds--;
          }
        }
      }, 1000);
    },
  },
  created() {
    if (!this.timer.started) {
      this.startCountdown();
      this.timer.started = true;
    }
  },
};
</script>

