<template>
  <div class="dashboard-main">
    <nav class="navbar is-fixed-top has-background-grey-lighter">
      <div class="navbar-brand">
        <span class="navbar-item">
          <span class="tags has-addons">
            <span class="tag is-dark is-medium">Graph</span>
            <span class="tag is-primary is-medium">{{ graphDescription }}</span>
          </span>
        </span>
        <span class="navbar-item">
          <span class="tags has-addons">
            <span class="tag is-dark is-medium">Layout</span>
            <span class="tag is-info is-medium">{{ layoutDescription }}</span>
          </span>
        </span>
      </div>
    </nav>
    <section class="hero is-fullheight-with-navbar">
      <div class="hero-body">
          <viewer />
      </div>
    </section>
  </div>
</template>

<script>
import Viewer from './Viewer'
import state from '../state'
import graphSources from '../config/graphSources'
import layoutSources from '../config/layoutSources'

export default {
  name: 'ViewerArea',
  components: { Viewer },
  computed: {
    graphDescription () {
      if (state.generator === undefined) {
        return '-'
      }
      const { provider, name } = state.generator // TODO use displayName
      if (provider === undefined) {
        return '-'
      }
      if (provider === 'file') {
        return `Graph loaded from ${state.generator.parameters[0].value.name}`
      }
      return `${name} from ${graphSources[provider].displayName}`
    },
    layoutDescription () {
      if (state.algorithm === undefined) {
        return '-'
      }
      const { provider, name } = state.algorithm // TODO use displayName
      if (provider === undefined) {
        return '-'
      }
      return `${name} from ${layoutSources[provider].displayName}`
    }
  }
}
</script>
