<template>
  <aside class="menu">
    <generators-list
      v-model="generator"/>
    <p class="menu-label">
      Parameters
    </p>
    <div
      class="is-size-7 has-text-centered is-italic"
      v-if="generator === undefined"
    >
      Generator's parameters<br>will be displayed here
    </div>
    <ul
      class="menu-list"
      v-else
    >
      <li><a>TODO params for {{ generator.name }}</a></li>
    </ul>
  </aside>
</template>

<script>
import NetworkXGeneratorsList from './NetworkXGeneratorsList'
import apiOperationMixin from '../../mixin/apiOperationMixin'

const mixinData = {
  operationName: 'generate',
  shouldRetry: false,
  consoleErrorMessage: 'Could not get generated graph',
  toastErrorMessage: 'Could not generate graph'
}

export default {
  name: 'networkx-graph-provider',
  mixins: [
    apiOperationMixin
  ],
  components: {
    GeneratorsList: NetworkXGeneratorsList
  },
  data () {
    return {
      generator: undefined,
      ...mixinData
    }
  },
  computed: {
    operationData () {
      return {
        name: this.generator.name
        // TODO: params
      }
    }
  },
  watch: {
    generator () {
      this.performOperation()
    }
  },
  methods: {
    handleOperationSucceeded (graph) {
      graph.data = {
        name: this.generator.name,
        provider: 'NetworkX',
        ...graph.data
      }
      this.$emit('input', graph)
    }
  }
}
</script>
