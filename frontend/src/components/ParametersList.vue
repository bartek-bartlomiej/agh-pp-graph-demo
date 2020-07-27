<template>
  <div
    class="is-size-7 has-text-centered is-italic"
    v-if="parameters.length === 0">
      No parameters
  </div>
  <section
    v-else>
      <component
        v-for="(parameter, index) in parameters"
        :key="index"
        :is="types[typeof parameter.value]"
        v-bind.sync="parameter"
      />
  </section>
</template>

<script>
import numberParameter from './parameters/numberParameter'
import booleanParameter from './parameters/booleanParameter'

const types = {
  boolean: booleanParameter,
  number: numberParameter
}

export default {
  name: 'ParametersList',
  props: {
    name: String,
    parameters: Array
  },
  data () {
    return {
      types
    }
  }
}
</script>
