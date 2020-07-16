<template>
  <div class="card cytoscape-container">
    <div class="cytoscape-display" ref="container" />
  </div>
</template>

<script>
import cytoscape from 'cytoscape'
import style from '../assets/style.json'
import elements from '../assets/elements.json'

export default {
  name: 'Example',
  props: {
    layoutName: {
      type: String,
      required: true,
      default: 'grid'
    }
  },
  data () {
    return {}
  },
  watch: {
    layoutName (value) {
      if (this.$_cy === null) {
        return
      }
      this.$_cy.layout({ name: value }).run()
    }
  },
  mounted () {
    const cy = cytoscape({
      container: this.$refs.container,
      elements,
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
    min-width: 50vw;
    height: 90vh;
    width: 100vw;
  }
</style>
