<template>
  <div class="field">
    <b-switch
      v-model="currentValue">
      {{ name }}
    </b-switch>
  </div>
</template>

<script>
export default {
  name: 'booleanParameter',
  props: {
    name: String,
    value: Boolean
  },
  data () {
    return {
      currentValue: this.value
    }
  },
  watch: {
    value (value) {
      this.currentValue = value
    },
    currentValue (value) {
      this.$emit('update:value', value)
    }
  }
}
</script>
