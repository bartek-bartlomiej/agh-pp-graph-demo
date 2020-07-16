import Vue from 'vue'
import App from './App.vue'
import cytoscape from 'cytoscape'
import dagre from 'cytoscape-dagre'

cytoscape.use(dagre)

Vue.config.productionTip = false

new Vue({
  render: h => h(App)
}).$mount('#app')
