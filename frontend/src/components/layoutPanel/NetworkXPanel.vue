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

    <p class="menu-label">
      Parameters
    </p>
    <div
      class="is-size-7 has-text-centered is-italic"
      v-if="algorithm === undefined">
      Algorithm's parameters<br>will be displayed here
    </div>
    <parameters-list
      :name="algorithm.name"
      :parameters="algorithm.parameters"
      v-else />
  </div>
</template>

<script>
import ParametersList from '../ParametersList'
import apiOperationMixin from '../../mixins/apiOperationMixin'
import state from '../../state'

const mixinData = {
  operationName: 'get_algorithms',
  shouldRetry: true,
  consoleErrorMessage: 'Could not get algorithms',
  toastErrorMessage: 'Could not display algorithms'
}

export default {
  name: 'NetworkXPanel',
  components: { ParametersList },
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
