<template>
  <div class="card cytoscape-container">
    <div class="cytoscape-display" ref="container" />
  </div>
</template>

<script>
import cytoscape from 'cytoscape'
import cloneDeep from 'lodash.clonedeep'
import style from '../assets/style.json'
import state from '../state'

export default {
  name: 'Viewer',
  data () {
    return {
      state: state
    }
  },
  watch: {
    'state.graph' (graph) {
      if (this.$_cy === null) {
        return
      }
      this.$_cy.remove('*')
      if (graph === undefined) {
        return
      }
      this.$_cy.add(cloneDeep(graph.elements))
      this.$_cy.center()
      this.update(state.layout)
    },
    'state.layout' (layout) {
      this.update(layout)
    }
  },
  methods: {
    update (layout) {
      if (this.$_cy === null || layout === undefined) {
        return
      }
      this.$_cy.layout(layout).run()
    }
  },
  mounted () {
    this.$_cy = cytoscape({
      container: this.$refs.container,
      style
    })
  }
}
</script>

<style>
  .cytoscape-container {
    display: flex;
    height: 80vh;
  }
  .card > .cytoscape-display {
    height: 80vh;
    width: calc(100vw - 34rem);
  }
</style>
