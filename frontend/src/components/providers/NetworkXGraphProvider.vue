<template>
  <span/>
</template>

<script>
import apiOperationMixin from '../../mixins/apiOperationMixin'
import state from '../../state'

const mixinData = {
  operationName: 'generate',
  shouldRetry: false,
  consoleErrorMessage: 'Could not get generated graph',
  toastErrorMessage: 'Could not generate graph'
}

export default {
  name: 'NetworkXGraphProvider',
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
        name: state.generator.name,
        parameters: state.generator.parameters.map(({ name, value }) => ({ name, value }))
      }
    }
  },
  methods: {
    provide () {
      this.performOperation()
    },
    handleOperationSucceeded (graph) {
      state.graph = graph
    }
  }
}
</script>
