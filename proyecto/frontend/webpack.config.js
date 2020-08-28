const path = require('path');
const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
    entry: {
        home: './src/home/home.js',
        login: './src/login/login.js',
        register: './src/register/register.js'
    },
    module: {
        rules: [
            {
                loader: 'vue-loader',
                test: /\.vue$/
            },
            {
                loader: 'babel-loader',
                test: /\.js$/
            },
            {
                use: [ 
                    'style-loader',
                    'css-loader',
                    'sass-loader'
                ],
                test: /\.scss$/
            }
        ]
    },
    output: {
        filename: 'js/[name].js',
        path: path.resolve(__dirname, 'build')
    },
    plugins: [
        new VueLoaderPlugin()
    ]
};