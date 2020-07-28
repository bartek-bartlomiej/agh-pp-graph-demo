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
      this.$_cy.style().clear().update()
      if (graph === undefined) {
        return
      }
      this.$_cy.add(cloneDeep(graph.elements))
      this.$_cy.center()
      this.updateStyle(graph)
      this.update(state.layout)
    },
    'state.layout' (layout) {
      this.update(layout)
    }
  },
  methods: {
    updateStyle (graph) {
      const maxWeight = graph !== undefined && graph.elements.edges !== undefined && graph.elements.edges[0].data.weight !== undefined
        ? graph.elements.edges.reduce((max, { data }, _) => data.weight > max ? data.weight : max, 1)
        : undefined
      const _style = this.$_cy.style(style)
      if (maxWeight !== undefined) {
        _style
          .selector('edge')
          .style('width', `mapData(weight, 1, ${maxWeight}, 1, 5)`)
          .style('line-color', `mapData(weight, 1, ${maxWeight}, #ccc, #000)`)
      }
      // else {
      //   _style
      //     .selector('edge')
      //     .style('width', 1)
      //     .style('line-color', '#ccc')
      // }
      _style.update()
    },
    update (layout) {
      if (this.$_cy === null || layout === undefined) {
        return
      }
      if (this.$_layout !== undefined) {
        this.$_layout.stop()
      }
      this.$_layout = this.$_cy.layout(layout)
      this.$_layout.run()
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
