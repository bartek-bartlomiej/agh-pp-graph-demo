<template>
  <div class="dashboard is-full-height">
    <generator-panel
      v-model="elements"
    />
    <layout-panel
      v-model="layout"
    />
    <!-- main section -->
    <div class="dashboard-main">
      <section class="hero is-fullheight-with-navbar">
        <div class="hero-body">
          <example
            :elements="elements"
            :layout="layout" />
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import Example from './components/GraphPanel'
import GeneratorPanel from './components/ElementsPanel'
import LayoutPanel from './components/LayoutPanel'

export default {
  name: 'App',
  components: {
    LayoutPanel,
    GeneratorPanel,
    Example
  },
  data () {
    return {
      elements: undefined,
      layout: undefined
    }
  }
}
</script>
