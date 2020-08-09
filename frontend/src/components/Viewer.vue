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

      const elements = cloneDeep(graph.elements)
      const maxWeight = elements.edges !== undefined && elements.edges[0].data.weight !== undefined
        ? elements.edges.reduce((max, { data }, _) => data.weight > max ? data.weight : max, 1)
        : undefined

      if (maxWeight !== undefined) {
        const denominate = Math.log(maxWeight)
        elements.edges.forEach(edge => {
          edge.data.coefficient = Math.log(edge.data.weight + 1) / denominate
        })
      }

      this.$_cy.add(elements)
      this.$_cy.center()
      this.updateStyle(graph, maxWeight)
      this.update(state.layout)
    },
    'state.layout' (layout) {
      this.update(layout)
    }
  },
  methods: {
    updateStyle (graph, maxWeight) {
      const _style = this.$_cy.style(style)
      if (maxWeight !== undefined) {
        _style
          .selector('edge')
          .style('width', `mapData(weight, 1, ${maxWeight}, 1, 5)`)
          .style('line-color', `mapData(weight, 1, ${maxWeight}, #ccc, #000)`)
      }
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
