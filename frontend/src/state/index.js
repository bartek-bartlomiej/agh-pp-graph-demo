import algorithms from '../config/cytoscapeJSAlgorithms'

const state = {
  generator: undefined,
  graph: undefined,
  algorithm: algorithms.grid,
  layout: { name: 'grid', parameters: [] }
}

export default state
