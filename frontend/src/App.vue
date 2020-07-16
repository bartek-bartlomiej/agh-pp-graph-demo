<template>
  <div>
    <example :layout-name="selected" />
    <select v-model="selected">
      <option
        v-for="(layout, i) in layouts"
        :key="i"
        :value="layout">
        {{ layout }}
      </option>
    </select>
  </div>
</template>

<script>

import Example from './components/Example'

export default {
  name: 'App',
  components: {
    Example
  },
  data () {
    return {
      layouts: ['random', 'grid', 'circle', 'concentric', 'breadthfirst', 'cose', 'dagre'],
      selected: 'grid'
    }
  }
}
</script>
