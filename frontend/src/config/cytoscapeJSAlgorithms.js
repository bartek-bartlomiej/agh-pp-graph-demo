const algorithms = {
  grid: {
    provider: 'cytoscape-js',
    name: 'grid',
    displayName: 'Grid'
  },
  random: {
    provider: 'cytoscape-js',
    name: 'random',
    displayName: 'Random'
  },
  circle: {
    provider: 'cytoscape-js',
    name: 'circle',
    displayName: 'Circle'
  },
  concentric: {
    provider: 'cytoscape-js',
    name: 'concentric',
    displayName: 'Concentric'
  },
  breadthfirst: {
    provider: 'cytoscape-js',
    name: 'breadthfirst',
    displayName: 'Breadthfirst',
    parameters: [
      {
        name: 'directed',
        value: false
      },
      {
        name: 'circle',
        value: false
      },
      {
        name: 'grid',
        value: false
      },
      {
        name: 'maximal',
        value: false
      }
    ]
  },
  cose: {
    provider: 'cytoscape-js',
    name: 'cose',
    displayName: 'CoSE (Compound Spring Embedder)',
    parameters: [
      {
        name: 'gravity',
        value: 1,
        min: 0,
        max: 10
      },
      {
        name: 'randomized',
        value: false
      }
    ]
  },
  dagre: {
    provider: 'cytoscape-js',
    name: 'dagre',
    displayName: 'Dagre'
  }
}

export default algorithms
