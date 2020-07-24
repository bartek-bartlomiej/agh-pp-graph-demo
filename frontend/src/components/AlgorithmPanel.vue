<template>
  <div class="dashboard-panel is-small has-background-grey-light is-scrollable">
    <div class="dashboard-panel-content">
      <header class="dashboard-panel-header">
        <p class="menu-label">
          Layout Source
        </p>
        <b-field position="is-centered">
          <b-radio-button
            v-for="(source, key) of sources"
            v-model="currentSource"
            :native-value="source"
            :key="key"
            :disabled="!enabled"
          >
            {{ source.displayName }}
          </b-radio-button>
        </b-field>
      </header>
      <aside
        class="menu"
        v-if="enabled">
        <component
          :is="currentSource.panelComponent"
        />
      </aside>
    </div>
  </div>
</template>

<script>
import sources from '../config/layoutSources'
import state from '../state'

export default {
  name: 'AlgorithmPanel',
  computed: {
    enabled () {
      return state.generator !== undefined
    }
  },
  data () {
    return {
      currentSource: sources['cytoscape-js'],
      sources
    }
  }
}
</script>
