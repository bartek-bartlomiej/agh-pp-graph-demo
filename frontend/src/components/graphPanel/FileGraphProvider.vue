<template>
  <div></div>
</template>

<script>
import elements from '../../assets/elements.json'

export default {
  name: 'FileGraphProvider',
  mounted () {
    const graph = {
      data: {
        name: 'elements.json',
        provider: 'file'
      },
      elements
    }
    this.$emit('input', graph)
  }
}
</script>
