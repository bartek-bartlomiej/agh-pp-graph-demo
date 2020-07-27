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
        name: 'nodeRepulsion',
        value: 2048,
        min: 1024,
        max: 4096,
        map: value => (_) => value
      },
      {
        name: 'nodeOverlap',
        value: 4,
        min: 1,
        max: 100
      },
      {
        name: 'idealEdgeLength',
        value: 32,
        min: 1,
        max: 32,
        map: value => (edge) => {
          const weight = edge.data('weight')
          return weight !== undefined ? value / weight : value
        }
      },
      {
        name: 'edgeElasticity',
        value: 32,
        min: 1,
        max: 100,
        map: value => (_) => value
      },
      {
        name: 'nestingFactor',
        value: 1.2,
        min: 0,
        max: 2
      },
      {
        name: 'gravity',
        value: 1,
        min: 0,
        max: 10
      },
      {
        name: 'numIter',
        value: 1000,
        min: 500,
        max: 2000
      },
      {
        name: 'initialTemp',
        value: 1000,
        min: 100,
        max: 2000
      },
      {
        name: 'coolingFactor',
        value: 0.99,
        min: 0.01,
        max: 0.99
      },
      {
        name: 'minTemp',
        value: 1.0,
        min: 1.0,
        max: 100
      },
      {
        name: 'animationThreshold',
        value: 250,
        min: 0,
        max: 1000
      },
      {
        name: 'refresh',
        value: 20,
        min: 1,
        max: 1000
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
    parameters: [
      {
        name: 'rankDir',
        value: 'TB',
        values: ['TB', 'BT', 'LR', 'RL']
      },
      {
        name: 'ranker',
        value: 'network-simplex',
        values: ['network-simplex', 'tight-tree', 'longest-path']
      },
      {
        name: 'minLen',
        value: 1,
        min: 1,
        max: 10,
        step: 1,
        map: value => (_) => value
      },
      {
        name: 'edgeWeight',
        value: false,
        map: value => (edge) => {
          const weight = edge.data('weight')
          return weight !== undefined && value ? weight : 1
        }
      }
    ]
  }
}

export default algorithms
