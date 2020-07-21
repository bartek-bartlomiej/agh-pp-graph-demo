<template>
  <div class="dashboard is-full-height">
    <graph-panel
      v-model="graph"
    />
    <layout-panel
      :graph="graph"
      v-model="layout"
    />
    <viewer-area
      :graph="graph"
      :layout="layout"
    />
  </div>
</template>

<script>
import GraphPanel from './components/GraphPanel'
import LayoutPanel from './components/LayoutPanel'
import ViewerArea from './components/ViewerArea'

export default {
  name: 'App',
  components: {
    GraphPanel,
    LayoutPanel,
    ViewerArea
  },
  data () {
    return {
      graph: undefined,
      layout: undefined
    }
  }
}
</script>
