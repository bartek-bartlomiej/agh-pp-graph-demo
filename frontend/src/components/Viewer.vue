<template>
  <div class="card cytoscape-container">
    <div class="cytoscape-display" ref="container" />
  </div>
</template>

<script>
import cytoscape from 'cytoscape'
import cloneDeep from 'lodash.clonedeep'
import style from '../assets/style.json'

export default {
  name: 'Example',
  props: {
    graph: {
      type: Object
    },
    layout: {
      type: Object
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
      this.$_cy.remove('*')
      if (graph === undefined) {
        return
      }
      this.$_cy.add(cloneDeep(graph.elements))
      this.$_cy.center()
      this.update(this.layout)
    },
    layout (value) {
      this.update(value)
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
