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

export default {
  name: 'networkx-graph-provider',
  components: { GeneratorsList: NetworkXGeneratorsList },
  data () {
    return {
      generator: undefined
    }
  }
}
</script>
