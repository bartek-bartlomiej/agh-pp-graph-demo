<template>
  <component
    :is="typeProvider"
    ref="typeProvider"
  />
</template>

<script>
import state from '../../state'
import types from '../../config/acceptedFileTypes'

export default {
  name: 'FileGraphProvider',
  computed: {
    typeProvider () {
      return types[state.generator.name].providerComponent
    }
  },
  methods: {
    provide () {
      this.$refs.typeProvider.provide()
    }
  }
}
</script>
