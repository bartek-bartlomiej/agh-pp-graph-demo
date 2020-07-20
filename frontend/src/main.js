import Vue from 'vue'
import VueCytoscape from 'vue-cytoscape'
import App from './App.vue'

Vue.config.productionTip = false

Vue.use(VueCytoscape)

new Vue({
  render: h => h(App)
}).$mount('#app')
