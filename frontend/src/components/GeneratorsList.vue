<template>
  <ul class="menu-list">
    <li v-if="pending">
      <progress class="progress is-small is-primary" max="100"></progress>
    </li>
    <li
      v-else
      v-for="(generator, i) in generators" :key="i">
      <a
        :class="{ 'is-active': (selectedValue === generator) }"
        @click="selectedValue = generator">
        {{ generator.name }}
      </a>
    </li>
  </ul>
</template>

<script>
import apiOperationMixin from '../mixin/apiOperationMixin'

const mixinData = {
  operationName: 'get_generators',
  shouldRetry: true,
  consoleErrorMessage: 'Could not get generators',
  toastErrorMessage: 'Could not display generators'
}

export default {
  name: 'generators-list',
  mixins: [apiOperationMixin],
  props: {
    value: String
  },
  data () {
    return {
      generators: [],
      selectedValue: this.value,
      ...mixinData
    }
  },
  watch: {
    selectedValue (value) {
      this.$emit('input', value)
    }
  },
  methods: {
    handleOperationSucceeded (generators) {
      console.log(generators)
      this.generators = generators
    }
  },
  mounted () {
    this.performOperation()
  }
}
</script>
