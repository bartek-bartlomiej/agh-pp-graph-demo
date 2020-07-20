<template>
  <div class="dashboard is-full-height">
    <!-- left panel -->
    <div class="dashboard-panel is-medium has-thick-padding has-background-grey-lighter is-hidden-mobile is-scrollable">
      <header class="dashboard-panel-header">
        <div class="has-text-centered">
          <span class="tag is-large is-white">
            PP Graph App
          </span>
        </div>
      </header>

      <div class="dashboard-panel-content">
        <aside class="menu">
          <p class="menu-label">
            Graph - from NetworkX
          </p>
          <generators-list/>

          <p class="menu-label">
            Graph - from file
          </p>
          <ul class="menu-list">
            <li>TODO</li>
          </ul>

          <p class="menu-label">
            Layout - from NetworkX
          </p>
          <ul class="menu-list">
            <li><a>TODO</a></li>
            <li><a>TODO</a></li>
            <li><a>TODO</a></li>
          </ul>

          <p class="menu-label">
            Layout - from Cytoscape
          </p>
          <ul class="menu-list">
            <li v-for="(layout, i) in layouts" :key="i">
              <a
                :class="{ 'is-active': (selected === layout) }"
                @click="selected = layout">
                {{ layout }}
              </a>
            </li>
          </ul>
        </aside>
      </div>
    </div>

    <!-- main section -->
    <div class="dashboard-main">
      <section class="hero is-fullheight-with-navbar">
        <div class="hero-body">
          <example :layout-name="selected" />
        </div>
      </section>
    </div>
  </div>
</template>

<script>

import Example from './components/Example'
import GeneratorsList from './components/GeneratorsList'

export default {
  name: 'App',
  components: {
    GeneratorsList,
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
