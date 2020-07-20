<template>
  <div>
    <p class="menu-label">
      Generator
    </p>
    <b-select
      placeholder="Select a generator"
      @input="$emit('input', $event)"
      :loading="pending">
      <option
        v-for="(generator, index) in generators"
        :value="generator"
        :key="index">
        {{ generator.name }}
      </option>
    </b-select>
  </div>
</template>

<script>
import apiOperationMixin from '../../mixin/apiOperationMixin'

const mixinData = {
  operationName: 'get_generators',
  shouldRetry: true,
  consoleErrorMessage: 'Could not get generators',
  toastErrorMessage: 'Could not display generators'
}

export default {
  name: 'generators-list',
  mixins: [
    apiOperationMixin
  ],
  data () {
    return {
      generators: [],
      ...mixinData
    }
  },
  methods: {
    handleOperationSucceeded (generators) {
      this.generators = generators
    }
  },
  mounted () {
    this.performOperation()
  }
}
</script>
