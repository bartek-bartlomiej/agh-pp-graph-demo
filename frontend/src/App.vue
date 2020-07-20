<template>
  <div class="dashboard is-full-height">
    <graph-panel
      v-model="graph"
    />
    <template
      v-if="graph !== undefined">
      <layout-panel
        :graph="graph"
        v-model="layout"
      />
    </template>
    <template v-if="graph !== undefined && layout !== undefined">
      <div class="dashboard-main">
        Graph: {{ graph.displayName }}
        Layout: {{ layout.displayName }}
        <section class="hero is-fullheight-with-navbar">
          <div class="hero-body">
            <viewer
              :elements="graph.elements"
              :layout="layout" />
          </div>
        </section>
      </div>
    </template>
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
      graph: undefined,
      layout: undefined
    }
  }
}
</script>
