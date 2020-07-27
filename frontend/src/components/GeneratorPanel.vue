<template>
  <div class="dashboard-panel is-small is-light is-scrollable">
    <div class="dashboard-panel-content">
      <header class="dashboard-panel-header">
        <p class="menu-label">
          Graph Source
        </p>
        <b-field position="is-centered">
          <b-radio-button
            v-for="(source, key) of sources"
            v-model="currentSource"
            :native-value="source"
            :key="key"
          >
            {{ source.displayName }}
          </b-radio-button>
        </b-field>
      </header>
      <aside class="menu">
        <component
          :is="currentSource.panelComponent"
        />
      </aside>
    </div>
  </div>
</template>

<script>
import sources from '../config/graphSources'

export default {
  name: 'GeneratorPanel',
  data () {
    return {
      currentSource: sources.file,
      sources
    }
  }
}
</script>
