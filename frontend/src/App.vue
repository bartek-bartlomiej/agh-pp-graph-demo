<template>
  <div class="dashboard is-full-height">
    <generator-panel />
    <algorithm-panel />
    <viewer-area />
    <component
      :is="graphProvider"
      ref="graphProvider" />
    <component
      :is="layoutProvider"
      ref="layoutProvider" />
  </div>
</template>

<script>
import GeneratorPanel from './components/GeneratorPanel'
import AlgorithmPanel from './components/AlgorithmPanel'
import ViewerArea from './components/ViewerArea'
import state from './state'
import graphSources from './config/graphSources'
import layoutSources from './config/layoutSources'

export default {
  name: 'App',
  components: {
    GeneratorPanel,
    AlgorithmPanel,
    ViewerArea
  },
  data () {
    return {
      state: state
    }
  },
  computed: {
    graphProvider () {
      const { generator } = state
      return generator !== undefined ? graphSources[generator.provider].providerComponent : undefined
    },
    layoutProvider () {
      const { algorithm } = state
      return algorithm !== undefined ? layoutSources[algorithm.provider].providerComponent : undefined
    }
  },
  watch: {
    'state.generator' () {
      this.$nextTick(() => this.$refs.graphProvider.provide())
    },
    'state.graph' () {
      this.$nextTick(() => this.$refs.layoutProvider.provide())
    },
    'state.algorithm': {
      deep: true,
      handler () {
        this.$nextTick(() => this.$refs.layoutProvider.provide())
      }
    }
  }
}
</script>
