<template>
  <b-field :label="name">
    <b-select
      v-model="currentValue">
      <option
        v-for="(value, index) in values"
        :value="value"
        :key="index">
        {{ value }}
      </option>
    </b-select>

  </b-field>
</template>

<script>
export default {
  name: 'enumParameter',
  props: {
    name: String,
    value: String,
    values: Array
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

<style scoped>

</style>
