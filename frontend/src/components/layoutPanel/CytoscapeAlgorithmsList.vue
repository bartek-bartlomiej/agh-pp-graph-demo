<template>
  <div>
    <p class="menu-label">
      Algorithm
    </p>
    <b-select
      placeholder="Select an algorithm"
      v-model="selected"
      @input="$emit('input', $event)">
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
const algorithms = [
  {
    name: 'grid'
  },
  {
    name: 'random'
  },
  {
    name: 'circle'
  },
  {
    name: 'concentric'
  },
  {
    name: 'breadthfirst'
  },
  {
    name: 'cose'
  },
  {
    name: 'dagre'
  }
]

export default {
  name: 'CytoscapeAlgorithmsList',
  props: {
    value: Object
  },
  data () {
    return {
      selected: this.value,
      algorithms
    }
  }
}
</script>
