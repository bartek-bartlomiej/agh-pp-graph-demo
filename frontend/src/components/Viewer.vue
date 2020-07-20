<template>
  <div class="card cytoscape-container">
    <div class="cytoscape-display" ref="container" />
  </div>
</template>

<script>
import cytoscape from 'cytoscape'
import style from '../assets/style.json'

const defaultGraph = {
  elements: []
}
const defaultLayout = {
  name: 'grid'
}

export default {
  name: 'Example',
  props: {
    graph: {
      type: Object,
      required: true,
      default () {
        return defaultGraph
      }
    },
    layout: {
      type: Object,
      required: true,
      default () {
        return defaultLayout
      }
    }
  },
  data () {
    return {}
  },
  watch: {
    graph (graph) {
      if (this.$_cy === null) {
        return
      }
      if (graph === undefined) {
        this.$_cy.remove('*')
        return
      }

      this.$_cy.remove('*')
      this.$_cy.add(graph.elements)
      this.$_cy.layout(this.layout).run()
    },
    layout (value) {
      if (this.$_cy === null) {
        return
      }
      this.$_cy.layout(value).run()
    }
  },
  mounted () {
    const cy = cytoscape({
      container: this.$refs.container,
      elements: this.graph.elements,
      layout: this.layout,
      style
    })
    cy.center()
    this.$_cy = cy
  }
}

</script>

<style>
  .cytoscape-container {
    display: flex;
    max-height: 90vh;
  }
  .card > .cytoscape-display {
    height: 80vh;
    width: calc(100vw - 34rem);
  }
</style>
