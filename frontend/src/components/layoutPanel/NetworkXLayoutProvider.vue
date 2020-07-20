<template>
  <aside class="menu">
    <network-x-algorithms-list
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
import NetworkXAlgorithmsList from './NetworkXAlgorithmsList'
import apiOperationMixin from '../../mixin/apiOperationMixin'

const mixinData = {
  operationName: 'arrange',
  shouldRetry: false,
  consoleErrorMessage: 'Could not get nodes positions',
  toastErrorMessage: 'Could not arrange graph'
}

export default {
  name: 'NetworkXLayoutProvider',
  mixins: [
    apiOperationMixin
  ],
  components: {
    NetworkXAlgorithmsList
  },
  props: {
    graph: Object
  },
  data () {
    return {
      algorithm: undefined,
      ...mixinData
    }
  },
  computed: {
    layout () {
      return {
        name: 'preset',
        positions: undefined
        // TODO: params
      }
    },
    layoutInfo () {
      return {
        layout: this.layout,
        displayName: `${this.algorithm.name.toString()} from NetworkX`
      }
    },
    operationData () {
      return {
        graph: this.graph,
        layout: {
          name: this.algorithm.name
          // TODO: params
        }
      }
    }
  },
  watch: {
    algorithm () {
      this.performOperation()
    }
  },
  methods: {
    handleOperationSucceeded (graph) {
      console.log(graph)
      // this.$emit('input', graph.elements)
    }
  }
}
</script>

<style scoped>

</style>
