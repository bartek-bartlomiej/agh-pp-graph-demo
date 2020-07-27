<template>
  <div>
    <div
      class="is-size-7 has-text-centered is-italic"
      v-if="parameters === undefined">
      {{ name }}'s parameters<br>will be displayed here
    </div>
    <div
      class="is-size-7 has-text-centered is-italic"
      v-else-if="parameters.length === 0">
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
  </div>
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
  },
  methods: {
    dbg ($event) {
      console.log('dbg', $event)
    }
  }
}
</script>
