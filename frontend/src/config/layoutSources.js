import NetworkXLayoutPanel from '../components/layoutPanel/NetworkXPanel'
import CytoscapeJSLayoutPanel from '../components/layoutPanel/CytoscapeJSPanel'
import NetworkXLayoutProvider from '../components/providers/NetworkXLayoutProvider'
import CytoscapeJSLayoutProvider from '../components/providers/CytoscapeJSLayoutProvider'

const sources = {
  'network-x': {
    displayName: 'NetworkX',
    panelComponent: NetworkXLayoutPanel,
    providerComponent: NetworkXLayoutProvider
  },
  'cytoscape-js': {
    displayName: 'Cytoscape.js',
    panelComponent: CytoscapeJSLayoutPanel,
    providerComponent: CytoscapeJSLayoutProvider
  }
}

export default sources
