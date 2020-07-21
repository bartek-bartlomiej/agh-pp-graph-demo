<template>
  <aside class="menu">
    <p class="menu-label">
      JSON / Edges List
    </p>
    <b-field class="has-addons" position="is-centered">
      <b-field class="file">
        <b-upload
          native
          v-model="file"
          accept=".json,.JSON,.edges">
          <a class="button is-primary">
            <span>Click to upload</span>
          </a>
        </b-upload>
      </b-field>
    </b-field>
  </aside>
</template>

<script>
import apiOperationMixin from '../../mixin/apiOperationMixin'

function readFile (file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.onload = () => {
      resolve(reader.result)
    }
    reader.onerror = () => {
      reject(reader.error)
    }
    reader.readAsText(file)
  })
}

const mixinData = {
  operationName: 'uploadFile',
  shouldRetry: false,
  consoleErrorMessage: 'Could not upload and parse file',
  toastErrorMessage: 'Could not parse file'
}

export default {
  name: 'FileGraphProvider',
  mixins: [
    apiOperationMixin
  ],
  data () {
    return {
      file: undefined,
      ...mixinData
    }
  },
  computed: {
    operationData () {
      const formData = new FormData()
      formData.append('file', this.file)
      return formData
    }
  },
  watch: {
    file (value) {
      readFile(value)
        .then((content) => {
          try {
            const elements = JSON.parse(content)
            const graph = { elements }
            this.passGraph(graph)
          } catch (e) {
            this.performOperation()
          }
        })
        .catch((error) => console.error(error))
    }
  },
  methods: {
    handleOperationSucceeded (graph) {
      this.passGraph(graph)
    },
    passGraph (graph) {
      graph.data = {
        provider: 'file',
        name: this.file.name,
        ...graph.data
      }
      this.$emit('input', graph)
    }
  }
}
</script>
