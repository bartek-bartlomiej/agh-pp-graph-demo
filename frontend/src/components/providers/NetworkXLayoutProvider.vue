<template>
  <span/>
</template>

<script>
import apiOperationMixin from '../../mixins/apiOperationMixin'
import state from '../../state'

const mixinData = {
  operationName: 'arrange',
  shouldRetry: false,
  consoleErrorMessage: 'Could not get nodes positions',
  toastErrorMessage: 'Could not arrange graph'
}

export default {
  name: 'NetworkXLayoutProvider',
  mixins: [
    apiOperationMixin
  ],
  data () {
    return {
      ...mixinData
    }
  },
  computed: {
    operationData () {
      return {
        graph: state.graph,
        layout: {
          name: state.algorithm.name
          // TODO: params from NetworkX
        }
      }
    }
  },
  methods: {
    provide () {
      this.performOperation()
    },
    handleOperationSucceeded (positions) {
      const map = new Map(positions.map((pos) => [
        pos.id,
        {
          x: Number.parseFloat(pos.x) * 1000,
          y: Number.parseFloat(pos.y) * 1000
        }
      ]))

      state.layout = {
        name: 'preset',
        positions: (node) => map.get(node.id())
        // TODO: params from cytoscape 'preset' layout
      }
    }
  }
}
</script>
