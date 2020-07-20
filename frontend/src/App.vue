<template>
  <div class="dashboard is-full-height">
    <graph-panel
      v-model="graphInfo"
    />
    <layout-panel
      :graph="graph"
      v-model="layoutInfo"
    />
    <div class="dashboard-main">
      <section class="hero is-fullheight-with-navbar">
        <div class="hero-body">
          <div class="container content">
            <p>
              <viewer
                :graph="graph"
                :layout="layout" />
            </p>
            <p>
              Graph: {{ graphDisplayName }}
              <br/>
              Layout: {{ layoutDisplayName }}
            </p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import Viewer from './components/Viewer'
import GraphPanel from './components/GraphPanel'
import LayoutPanel from './components/LayoutPanel'

export default {
  name: 'App',
  components: {
    LayoutPanel,
    GraphPanel,
    Viewer
  },
  data () {
    return {
      graphInfo: undefined,
      layoutInfo: undefined
    }
  },
  computed: {
    graph () {
      return this.graphInfo !== undefined ? this.graphInfo.graph : undefined
    },
    graphDisplayName () {
      return this.graphInfo !== undefined ? this.graphInfo.displayName : '-'
    },
    layout () {
      return this.layoutInfo !== undefined ? this.layoutInfo.layout : undefined
    },
    layoutDisplayName () {
      return this.layoutInfo !== undefined ? this.layoutInfo.displayName : '-'
    }
  }
}
</script>
