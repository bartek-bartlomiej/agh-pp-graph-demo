<template>
  <span/>
</template>

<script>
import apiOperationMixin from '../../../mixins/apiOperationMixin'
import state from '../../../state'

const mixinData = {
  operationName: 'upload_file',
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
      ...mixinData
    }
  },
  computed: {
    file () {
      return state.generator.parameters[0].value
    },
    weighted () {
      return state.generator.parameters[1].value
    },
    operationParams () {
      return {
        weighted: this.weighted
      }
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
