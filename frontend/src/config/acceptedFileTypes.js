import FileJSONGraphProvider from '../components/providers/fileProvider/FileJSONGraphProvider'
import FileEdgesGraphProvider from '../components/providers/fileProvider/FileEdgesGraphProvider'

const types = {
  json: {
    name: 'json',
    displayName: 'JSON',
    accept: '.json,.JSON',
    providerComponent: FileJSONGraphProvider,
    parameters: []
  },
  edges: {
    name: 'edges',
    displayName: 'Edges List',
    accept: '.edges',
    providerComponent: FileEdgesGraphProvider,
    parameters: [
      {
        name: 'weighted',
        value: false
      }
    ]
  }
}

export default types
