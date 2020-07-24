<template>
  <div>
    <p class="menu-label">
      Algorithm
    </p>
    <b-select
      placeholder="Select an algorithm"
      v-model="algorithm">
      <option
        v-for="(algorithm, key) of algorithms"
        :value="algorithm"
        :key="key">
        {{ algorithm.displayName }}
      </option>
    </b-select>
  </div>
</template>

<script>
import state from '../../state'
import algorithms from '../../config/cytoscapeJSAlgorithms'

export default {
  name: 'CytoscapeJSPanel',
  props: {
    value: Object
  },
  data () {
    const { algorithm } = state
    const validAlgorithm = algorithm !== undefined && algorithm.provider === 'cytoscape-js' ? algorithm : undefined
    return {
      algorithm: validAlgorithm,
      algorithms: algorithms
    }
  },
  watch: {
    algorithm (algorithm) {
      state.algorithm = algorithm
    }
  }
}
</script>
