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
        ...state.algorithm.parameters.reduce((acc, parameter, _) => {
          acc[parameter.name] = parameter.map !== undefined ? parameter.map(parameter.value) : parameter.value
          return acc
        }, {})
        // TODO: default params from cytoscape
      }
    }
  }
}
</script>
