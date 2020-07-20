<template>
  <div></div>
</template>

<script>
import elements from '../../assets/elements.json'

export default {
  name: 'FileGraphProvider',
  created () {
    this.$emit('input', {
      elements
    })
  }
}
</script>
