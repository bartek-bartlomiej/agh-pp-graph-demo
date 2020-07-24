<template>
  <span/>
</template>

<script>
import state from '../../state'

export default {
  name: 'CytoscapeJSLayoutProvider',
  methods: {
    provide () {
      state.layout = {
        name: state.algorithm.name
        // TODO: params from algorithm
        // TODO: default params from cytoscape
      }
    }
  }
}
</script>
