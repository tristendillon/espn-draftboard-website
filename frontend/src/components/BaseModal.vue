<template>
  <Transition name="modal-outer">
    <div v-show="modalActive" class="absolute w-full bg-black bg-opacity-30 h-screen top-0 left-0 flex justify-center px-8">
    <Transition name="modal-inner">
      <div v-if="modalActive" class="p-4 bg-white self-start md:mt-4 sm:mt-2 max-w-screen-md justify-center">
      <slot />
      <div class="flex justify-center">
        <button class="text-white mt-8 bg-primary py-2 px-6" @click="$emit('close-modal')">
            {{ buttonValue }}
        </button>
        </div>
      </div>
      
    </Transition>
    </div>
  </Transition>
</template>

<script setup>
defineEmits(['close-modal'])
defineProps({
  buttonValue: {
    type: String,
    default: "Close"
  }, 
    modalActive: {
    type: Boolean,
    default: true,
  }
}) 
</script>

<style scoped>
.modal-outer-enter-active,
.modal-outer-leave-active {
  transition: opacity 0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02);
}

.modal-outer-enter-from,
.modal-outer-leave-to {
  opacity: 0;
}

.modal-inner-enter-active {
  transition: all 0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02) 0.15s;
}

.modal-inner-leave-active {
  transition: all 0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02);
}

.modal-inner-enter-from {
  opacity: 0;
  transform: scale(0.8);
}

.modal-inner-leave-to {
  transform: scale(0.8);
}
</style>
