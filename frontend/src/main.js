import './assets/tailwind.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

app.directive('scroll-transform', {
mounted(el, binding) {
    const { translateX, translateY } = binding.value;
    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        const scrollX = window.scrollX;
        const translateXValue = scrollX;
        const translateYValue = scrollY;

        el.style.transform = `translate(${translateXValue}px, ${translateYValue}px)`;
    });
},
});
app.directive('y-transform', {
    mounted(el, binding) {
        const { translateY } = binding.value;
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            
            if (scrollY < translateY) {
                el.style.transform = `translate(0, 0px)`;
            }else if (scrollY > translateY){
                el.style.transform = `translate(0, ${translateY}px)`;
            }
        });
    },
    });
  

app.mount('#app')
