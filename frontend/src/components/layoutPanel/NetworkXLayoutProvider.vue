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

const defaultPositionsFunc = () => ({ x: 0, y: 0 })

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
      positions: defaultPositionsFunc,
      ...mixinData
    }
  },
  computed: {
    layout () {
      return {
        data: {
          name: this.algorithm.name,
          provider: 'NetworkX'
        },
        name: 'preset',
        positions: this.positions
        // TODO: params
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
    handleOperationSucceeded (positions) {
      const nodeMap = new Map(positions.map((pos) => [pos.id, { x: Number.parseFloat(pos.x) * 1000, y: Number.parseFloat(pos.y) * 1000 }]))
      this.positions = (node) => nodeMap.get(node.id())
      this.$emit('input', this.layout)
    }
  }
}
</script>

<style scoped>

</style>
