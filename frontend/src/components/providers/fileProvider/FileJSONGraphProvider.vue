<template>
  <span/>
</template>

<script>
import state from '../../../state'

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

export default {
  name: 'FileGraphProvider',
  computed: {
    file () {
      return state.generator.parameters[0].value
    }
  },
  methods: {
    provide () {
      readFile(this.file)
        .then((content) => {
          try {
            const elements = JSON.parse(content)
            state.graph = { elements }
          } catch (error) {
            console.error(error)
          }
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>
