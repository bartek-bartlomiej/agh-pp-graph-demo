<template>
  <div class="dashboard-panel is-small has-background-grey-lighter is-scrollable">
    <div class="dashboard-panel-content">
      <header class="dashboard-panel-header">
        <p class="menu-label">
          Graph
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
import NetworkXGraphProvider from './elementsPanel/NetworkXGraphProvider'
import FileGraphProvider from './elementsPanel/FileGraphProvider'

const providers = {
  'network-x': {
    name: 'NetworkX',
    component: NetworkXGraphProvider
  },
  file: {
    name: 'File',
    component: FileGraphProvider
  }
}

export default {
  name: 'GeneratorPanel',
  data () {
    return {
      selectedProvider: providers.file,
      providers
    }
  }
}
</script>
