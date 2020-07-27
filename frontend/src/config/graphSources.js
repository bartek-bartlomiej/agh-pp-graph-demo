import NetworkXPanel from '../components/generatorPanel/NetworkXPanel'
import FilePanel from '../components/generatorPanel/FilePanel'
import NetworkXGraphProvider from '../components/providers/NetworkXGraphProvider'
import FileGraphProvider from '../components/providers/FileGraphProvider'

const sources = {
  'network-x': {
    displayName: 'NetworkX',
    panelComponent: NetworkXPanel,
    providerComponent: NetworkXGraphProvider
  },
  file: {
    displayName: 'File',
    panelComponent: FilePanel,
    providerComponent: FileGraphProvider
  }
}

export default sources
