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
        value: 400000,
        min: 0,
        max: 1000000,
        step: 100000,
        map: value => (_) => value
      },
      {
        name: 'nodeOverlap',
        value: 20,
        min: 1,
        max: 100
      },
      {
        name: 'idealEdgeLength',
        value: 100,
        min: 0,
        max: 1000,
        step: 100,
        map: value => (edge) => {
          const coefficient = edge.data('coefficient')
          return coefficient !== undefined ? value * (1 - 0.5 * coefficient) : value
        }
      },
      {
        name: 'edgeElasticity',
        value: 100,
        min: 1,
        max: 200
      },
      {
        name: 'nestingFactor',
        value: 5,
        min: 0,
        max: 10
      },
      {
        name: 'gravity',
        value: 80,
        min: 0,
        max: 100
      },
      {
        name: 'numIter',
        value: 1000,
        min: 500,
        max: 10000
      },
      {
        name: 'initialTemp',
        value: 200,
        min: 100,
        max: 1000
      },
      {
        name: 'coolingFactor',
        value: 0.95,
        min: 0.01,
        max: 0.99
      },
      {
        name: 'minTemp',
        value: 1.0,
        min: 0.0,
        max: 10
      },
      {
        name: 'refresh',
        value: 20,
        min: 1,
        max: 50
      },
      {
        name: 'randomize',
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
  },
  cola: {
    provider: 'cytoscape-js',
    name: 'cola',
    displayName: 'Cola.js',
    parameters: [
      {
        name: 'fit',
        value: false
      },
      {
        name: 'randomize',
        value: true
      },
      {
        name: 'nodeSpacing',
        value: 10,
        min: 1,
        max: 40,
        map: value => (_) => value
      },
      {
        name: 'edgeLength',
        value: 300,
        min: 100,
        max: 1000,
        map: value => (edge) => {
          const coefficient = edge.data('coefficient')
          return coefficient !== undefined ? value * (1 - 0.5 * coefficient) : value
        }
      },
      {
        name: 'allConstIter',
        value: 100,
        min: 100,
        max: 20000,
        step: 100
      },
      {
        name: 'maxSimulationTime',
        value: 4000,
        min: 1000,
        max: 60000,
        step: 1000
      }
    ]
  },
  springy: {
    provider: 'cytoscape-js',
    name: 'springy',
    displayName: 'Springy',
    parameters: [
      {
        name: 'fit',
        value: false
      },
      {
        name: 'randomize',
        value: false
      },
      {
        name: 'infinite',
        value: false
      },
      {
        name: 'stiffness',
        value: 400,
        min: 0,
        max: 1000
      },
      {
        name: 'repulsion',
        value: 400,
        min: 0,
        max: 1000
      },
      {
        name: 'damping',
        value: 0.5,
        min: 0,
        max: 1
      },
      {
        name: 'edgeLength',
        value: 10,
        min: 10,
        max: 100,
        step: 10,
        map: value => (edge) => {
          const coefficient = edge.data('coefficient')
          return coefficient !== undefined ? value * (1 - 0.5 * coefficient) : value
        }
      }
    ]
  }
}

export default algorithms
