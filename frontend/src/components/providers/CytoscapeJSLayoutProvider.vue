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
        name: state.algorithm.name,
        ...state.algorithm.parameters.reduce((acc, item, _) => {
          acc[item.name] = item.value
          return acc
        }, {})
        // TODO: default params from cytoscape
      }
    }
  }
}
</script>
