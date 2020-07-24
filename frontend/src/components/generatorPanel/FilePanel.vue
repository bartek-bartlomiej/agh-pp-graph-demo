<template>
  <div>
    <p class="menu-label">
      Type
    </p>
    <b-select
      placeholder="Select a type"
      v-model="type">
      <option
        v-for="(type, key) of types"
        :value="type"
        :key="key">
        {{ type.displayName }}
      </option>
    </b-select>

    <p class="menu-label">
      {{ type.displayName }} File
    </p>
    <b-field class="file">
      <b-upload
        v-model="file"
        :accept="type.accept"
      >
        <a class="button is-primary">
          <span>Click to upload</span>
        </a>
      </b-upload>
    </b-field>
  </div>
</template>

<script>
import state from '../../state'
import types from '../../config/acceptedFileTypes'

export default {
  name: 'FilePanel',
  data () {
    const { generator } = state
    const validGenerator = generator !== undefined && generator.provider === 'file' ? generator : undefined
    const type = validGenerator !== undefined ? types[validGenerator.name] : types.json
    return {
      generator: validGenerator,
      type,
      types,
      file: undefined
    }
  },
  watch: {
    generator (generator) {
      state.generator = generator
    },
    file (file) {
      this.generator = {
        provider: 'file',
        name: this.type.name,
        parameters: [
          { name: 'file', value: file }
        ]
      }
    }
  }
}
</script>
