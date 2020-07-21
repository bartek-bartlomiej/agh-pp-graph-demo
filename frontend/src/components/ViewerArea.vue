<template>
  <div class="dashboard-main">
    <nav class="navbar is-fixed-top is-light">
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
          <viewer
            :graph="graph"
            :layout="layout"/>
      </div>
    </section>
  </div>
</template>

<script>
import Viewer from './Viewer'
import cloneDeep from 'lodash.clonedeep'

export default {
  name: 'viewer-area',
  components: { Viewer },
  props: {
    graph: Object,
    layout: Object
  },
  data () {
    return {
      graphInfo: {},
      layoutInfo: {}
    }
  },
  watch: {
    graph (graph) {
      if (graph === undefined) {
        return
      }
      this.graphInfo = {
        name: cloneDeep(graph.data.name),
        provider: cloneDeep(graph.data.provider)
      }
    },
    layout (layout) {
      if (layout === undefined) {
        return
      }
      this.layoutInfo = {
        name: cloneDeep(layout.data.name),
        provider: cloneDeep(layout.data.provider)
      }
    }
  },
  computed: {
    graphDescription () {
      if (this.graphInfo.provider === undefined) {
        return '-'
      }
      if (this.graphInfo.provider === 'file') {
        return `Loaded graph from ${this.graphInfo.name}`
      }
      return `${this.graphInfo.name} from ${this.graphInfo.provider}`
    },
    layoutDescription () {
      if (this.layoutInfo.provider === undefined) {
        return '-'
      }
      return `${this.layoutInfo.name} from ${this.layoutInfo.provider}`
    }
  }
}
</script>
