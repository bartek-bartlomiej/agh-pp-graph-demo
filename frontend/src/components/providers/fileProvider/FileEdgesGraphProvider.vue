<template>
  <span/>
</template>

<script>
import apiOperationMixin from '../../../mixins/apiOperationMixin'
import state from '../../../state'

const mixinData = {
  operationName: 'uploadFile',
  shouldRetry: false,
  consoleErrorMessage: 'Could not upload and parse file',
  toastErrorMessage: 'Could not parse file'
}

export default {
  name: 'FileEdgesGraphProvider',
  mixins: [
    apiOperationMixin
  ],
  data () {
    return {
      generator: state.generator,
      ...mixinData
    }
  },
  computed: {
    file () {
      return this.generator.parameters[0].value
    },
    operationData () {
      const formData = new FormData()
      formData.append('file', this.file)
      return formData
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
