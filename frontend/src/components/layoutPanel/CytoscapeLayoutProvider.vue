<template>
  <aside class="menu">
    <cytoscape-algorithms-list
      v-model="algorithm"
    />
    <p class="menu-label">
      Parameters
    </p>
    <div
      class="is-size-7 has-text-centered is-italic"
      v-if="algorithm === undefined"
    >
      Algorithm's parameters<br>will be displayed here
    </div>
    <ul
      class="menu-list"
      v-else
    >
      <li><a>TODO params for {{ algorithm.name }}</a></li>
    </ul>
  </aside>
</template>

<script>
import CytoscapeAlgorithmsList from './CytoscapeAlgorithmsList'

export default {
  name: 'CytoscapeLayoutProvider',
  components: { CytoscapeAlgorithmsList },
  data () {
    return {
      algorithm: {
        name: 'grid'
      }
    }
  },
  computed: {
    layout () {
      return {
        name: this.algorithm.name,
        // TODO: params
        displayName: `${this.algorithm.name.toString()} from Cytoscape.js`
      }
    }
  },
  watch: {
    algorithm () {
      this.$emit('input', this.layout)
    }
  }
}
</script>
