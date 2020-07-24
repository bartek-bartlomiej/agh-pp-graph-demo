<template>
  <div>
    <p class="menu-label">
      Algorithm
    </p>
    <b-select
      placeholder="Select an algorithm"
      v-model="algorithm"
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
import apiOperationMixin from '../../mixins/apiOperationMixin'
import state from '../../state'

const mixinData = {
  operationName: 'get_layouts',
  shouldRetry: true,
  consoleErrorMessage: 'Could not get algorithms',
  toastErrorMessage: 'Could not display algorithms'
}

export default {
  name: 'NetworkXPanel',
  mixins: [
    apiOperationMixin
  ],
  data () {
    const { algorithm } = state
    return {
      algorithm: algorithm !== undefined && algorithm.provider === 'network-x' ? algorithm : undefined,
      algorithms: [],
      ...mixinData
    }
  },
  watch: {
    algorithm (algorithm) {
      state.algorithm = algorithm
    },
    algorithms (algorithms) {
      if (this.algorithm === undefined) {
        return
      }
      const doesContain = algorithms.some((algorithm) => algorithm.name === this.algorithm.name)
      if (!doesContain) {
        this.algorithm = undefined
      }
    }
  },
  methods: {
    handleOperationSucceeded (algorithms) {
      this.algorithms = algorithms.map((algorithm) => ({ provider: 'network-x', ...algorithm }))
    }
  },
  created () {
    this.performOperation()
  }
}
</script>
