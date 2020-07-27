const algorithms = {
  grid: {
    provider: 'cytoscape-js',
    name: 'grid',
    displayName: 'Grid',
    parameters: []
  },
  random: {
    provider: 'cytoscape-js',
    name: 'random',
    displayName: 'Random',
    parameters: []
  },
  circle: {
    provider: 'cytoscape-js',
    name: 'circle',
    displayName: 'Circle',
    parameters: []
  },
  concentric: {
    provider: 'cytoscape-js',
    name: 'concentric',
    displayName: 'Concentric',
    parameters: []
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
    displayName: 'Dagre',
    parameters: []
  }
}

export default algorithms
