import Vue from 'vue'
import App from './App.vue'

import router from './router/router.js'
import store from './store/index'

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App),
})
