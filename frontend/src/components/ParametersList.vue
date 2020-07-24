<template>
  <div>
    <p class="menu-label">
      Parameters
    </p>
    <div
      class="is-size-7 has-text-centered is-italic"
      v-if="currentParameters === undefined">
      {{ name }}'s parameters<br>will be displayed here
    </div>
    <ul
      class="menu-list"
      v-else>
      <li
        v-for="(parameter, index) in currentParameters"
        :key="index"
        >
        <a>TODO {{ parameter.name }}</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ParametersList',
  props: {
    name: String,
    parameters: Array
  },
  data () {
    return {
      currentParameters: this.parameters
    }
  },
  watch: {
    currentParameters (parameters) {
      this.$emit('update:parameters', parameters)
    }
  }
}
</script>
