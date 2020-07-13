<template>
  <div id="example">
    <cytoscape
      ref="cyRef"
      :config="config">
      <cy-element
        v-for="def in elements"
        :key="`${def.data.id}`"
        :definition="def"/>
    </cytoscape>
  </div>
</template>

<script>
import config from '../assets/example-config.json'
import elements from '../assets/example-elements.json'

export default {
  name: 'Example',
  data () {
    return {
      config: config,
      elements: elements
    }
  }
}

</script>

<style>
  #example {
    width: 100%;
    height: 800px;
  }
</style>
