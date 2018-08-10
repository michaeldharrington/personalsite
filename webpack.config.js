const path = require('path')
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,
  entry: './assets/js/index',
  output: {
    path: path.resolve('./assets/bundles/'),
    filename: '[name]-[hash].js',
  },

  plugins: [
    new BundleTracker({filename: '.webpack-stats.json'}),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery'
    })
  ],


  resolve: {
    modulesDirectories: ['node_modules'],
    extensions: ['.js', '.jsx']
  }
}
