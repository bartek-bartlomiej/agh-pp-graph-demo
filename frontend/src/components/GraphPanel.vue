<template>
  <div class="card cytoscape-container">
    <div class="cytoscape-display" ref="container" />
  </div>
</template>

<script>
import cytoscape from 'cytoscape'
import style from '../assets/style.json'

const defaultLayout = {
  name: 'grid'
}

export default {
  name: 'Example',
  props: {
    elements: {
      type: Array,
      required: true,
      default () {
        return []
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
    elements (value) {
      if (this.$_cy === null) {
        return
      }
      this.$_cy.remove('*')
      this.$_cy.add(value)
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
      elements: this.elements,
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
    height: 90vh;
    width: calc(100vw - 34rem);
  }
</style>
