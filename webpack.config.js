module.exports = {
    entry: "./scripts/index.jsx",
    output: {
        path: __dirname,
        filename: "./static/script.js"
    },
    module: {
        rules: [
            { test: /\.css$/, loader: "styles!css" },
            {
                test: /\.(js|jsx)$/,
                exclude: /(node_modules)/,
                loader: 'babel-loader',
                options: {
                     presets: [
                        '@babel/preset-react',
                        [
                            '@babel/preset-env',
                            {
                              targets: {
                                esmodules: false
                              }
                            }
                        ]
                    ]
                }
            }
        ]
    },
    resolve: {
    extensions: ['.js', '.jsx'],
  }
};