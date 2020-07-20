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
          >
            {{ provider.name }}
          </b-radio-button>
        </b-field>
      </header>
      <component
        :is="selectedProvider.component"
        @input="$emit('input', $event)"
      />
    </div>
  </div>
</template>

<script>
import CytoscapeLayoutProvider from './layoutPanel/CytoscapeLayoutProvider'

const providers = {
  'network-x': {
    name: 'NetworkX',
    component: undefined
  },
  cytoscape: {
    name: 'Cytoscape.js',
    component: CytoscapeLayoutProvider
  }
}

export default {
  name: 'LayoutPanel',
  data () {
    return {
      selectedProvider: providers.cytoscape,
      providers
    }
  }
}
</script>
