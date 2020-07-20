<template>
  <div class="dashboard-panel is-small has-background-grey-light is-scrollable">
    <div class="dashboard-panel-content">
      <header class="dashboard-panel-header">
        <p class="menu-label">
          Layout
        </p>
        <b-field position="is-centered">
          <b-radio-button
            v-for="(provider, key) in providers"
            v-model="selectedProvider"
            :native-value="provider"
            :key="key"
            :disabled="graph === undefined"
          >
            {{ provider.name }}
          </b-radio-button>
        </b-field>
      </header>
      <component
        :is="selectedComponent"
        :graph="graph"
        @input="$emit('input', $event)"
      />
    </div>
  </div>
</template>

<script>
import CytoscapeLayoutProvider from './layoutPanel/CytoscapeLayoutProvider'
import NetworkXLayoutProvider from './layoutPanel/NetworkXLayoutProvider'

const providers = {
  'network-x': {
    name: 'NetworkX',
    component: NetworkXLayoutProvider
  },
  cytoscape: {
    name: 'Cytoscape.js',
    component: CytoscapeLayoutProvider
  }
}

export default {
  name: 'LayoutPanel',
  props: {
    graph: Object
  },
  data () {
    return {
      selectedProvider: undefined,
      providers
    }
  },
  computed: {
    selectedComponent () {
      return this.selectedProvider !== undefined ? this.selectedProvider.component : undefined
    }
  },
  watch: {
    graph (graph) {
      if (graph === undefined) {
        return
      }
      this.selectedProvider = providers.cytoscape
    }
  }
}
</script>
