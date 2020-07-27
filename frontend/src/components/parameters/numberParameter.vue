<template>
  <b-field :label="name">
    <b-slider
      :min="min"
      :max="max"
      v-model="currentValue"
      lazy/>
  </b-field>
</template>

<script>
export default {
  name: 'numberParameter',
  props: {
    name: String,
    value: Number,
    min: Number,
    max: Number
  },
  data () {
    return {
      currentValue: this.value
    }
  },
  watch: {
    currentValue (value) {
      this.$emit('update:value', value)
    }
  }
}
</script>
