<template>
  <div></div>
</template>

<script>
import elements from '../../assets/elements.json'

export default {
  name: 'FileGraphProvider',
  mounted () {
    const graph = {
      elements
    }
    const graphInfo = {
      graph,
      displayName: 'Dummy'
    }
    this.$emit('input', graphInfo)
  }
}
</script>
