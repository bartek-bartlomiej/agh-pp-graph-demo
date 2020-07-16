<template>
  <div id="container" ref="container" />
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
  #container {
    width: 100%;
    height: 100%;
    position: absolute;
    z-index: -1;
    top: 0;
    left: 0;
  }
</style>
