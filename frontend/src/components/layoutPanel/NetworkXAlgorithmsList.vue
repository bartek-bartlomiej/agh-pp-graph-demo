<template>
  <div>
    <p class="menu-label">
      Algorithm
    </p>
    <b-select
      placeholder="Select an algorithm"
      @input="$emit('input', $event)"
      :loading="pending">
      <option
        v-for="(algorithm, index) in algorithms"
        :value="algorithm"
        :key="index">
        {{ algorithm.name }}
      </option>
    </b-select>
  </div>
</template>

<script>
import apiOperationMixin from '../../mixin/apiOperationMixin'

const mixinData = {
  operationName: 'get_layouts',
  shouldRetry: true,
  consoleErrorMessage: 'Could not get algorithms',
  toastErrorMessage: 'Could not display algorithms'
}

export default {
  name: 'generators-list',
  mixins: [
    apiOperationMixin
  ],
  data () {
    return {
      algorithms: [],
      ...mixinData
    }
  },
  methods: {
    handleOperationSucceeded (algorithms) {
      this.algorithms = algorithms
    }
  },
  mounted () {
    this.performOperation()
  }
}
</script>
