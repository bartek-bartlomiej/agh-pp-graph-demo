<template>
  <div>
    <nav class="navbar is-info" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <div class="navbar-item">
          <span class="tag is-large is-white">
            PP Graph App
          </span>
        </div>

        <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarApp">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarApp" class="navbar-menu">
        <div class="navbar-start">
          <div class="navbar-item">
            <div class="select">
              <select v-model="selected">
                <option
                  v-for="(layout, i) in layouts"
                  :key="i"
                  :value="layout">
                  {{ layout }}
                </option>
              </select>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <section class="hero is-fullheight-with-navbar">
      <div class="hero-body">
        <example :layout-name="selected" />
      </div>
    </section>
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
