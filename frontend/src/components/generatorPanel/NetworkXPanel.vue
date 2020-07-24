<template>
  <div>
    <p class="menu-label">
      Generator
    </p>
    <b-select
      placeholder="Select a generator"
      v-model="generator"
      :loading="pending">
      <option
        v-for="(generator, index) in generators"
        :value="generator"
        :key="index">
        {{ generator.name }}
      </option>
    </b-select>
  </div>
</template>

<script>
import apiOperationMixin from '../../mixins/apiOperationMixin'
import state from '../../state'

const mixinData = {
  operationName: 'get_generators',
  shouldRetry: true,
  consoleErrorMessage: 'Could not get generators',
  toastErrorMessage: 'Could not display generators'
}

export default {
  name: 'NetworkXPanel',
  mixins: [
    apiOperationMixin
  ],
  data () {
    const { generator } = state
    const validGenerator = generator !== undefined && generator.provider === 'network-x' ? generator : undefined
    return {
      generator: validGenerator,
      generators: [],
      ...mixinData
    }
  },
  watch: {
    generator (generator) {
      state.generator = generator
    },
    generators (generators) {
      if (this.generator === undefined) {
        return
      }
      const doesContain = generators.some((generator) => generator.name === this.generator.name)
      if (!doesContain) {
        this.generator = undefined
      }
    }
  },
  methods: {
    handleOperationSucceeded (generators) {
      this.generators = generators.map((generator) => ({ provider: 'network-x', ...generator }))
    }
  },
  created () {
    this.performOperation()
  }
}
</script>
