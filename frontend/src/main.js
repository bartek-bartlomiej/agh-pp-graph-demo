import Vue from 'vue'
import App from './App.vue'
import cytoscape from 'cytoscape'
import dagre from 'cytoscape-dagre'
import Buefy from 'buefy'

import 'buefy/dist/buefy.min.css'
import 'bulma-dashboard/dist/bulma-dashboard.min.css'

cytoscape.use(dagre)
Vue.use(Buefy)
Vue.config.productionTip = false

new Vue({
  render: h => h(App)
}).$mount('#app')
