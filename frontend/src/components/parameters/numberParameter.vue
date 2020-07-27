<template>
  <b-field :label="name">
    <b-slider
      :min="min"
      :max="max"
      :step="stepValue"
      v-model="currentValue"
      lazy />
  </b-field>
</template>

<script>
export default {
  name: 'numberParameter',
  props: {
    name: String,
    value: Number,
    min: Number,
    max: Number,
    step: Number
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
  },
  computed: {
    stepValue () {
      return this.step !== undefined ? this.step : (this.max - this.min) / 100
    }
  }
}
</script>
