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
import state from '../../state'
import algorithms from '../../config/cytoscapeJSAlgorithms'
import ParametersList from '../ParametersList'

export default {
  name: 'CytoscapeJSPanel',
  components: { ParametersList },
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
