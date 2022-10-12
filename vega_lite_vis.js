var vg_1 = "map/prop_map.vg.json";
vegaEmbed("#bean_origin_map", vg_1).then(function(result) {
// Access the Vega view instance
// (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var vg_2 = "horizontal-bar-chart/lollipop_chart.vg.json";
vegaEmbed("#horizontal_bar_chart", vg_2).then(function(result) {
// Access the Vega view instance
// (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var vg_3 = "bar-chart/bar_chart.vg.json";
vegaEmbed("#bar_chart", vg_3).then(function(result) {
// Access the Vega view instance
// (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var vg_4 = "scatter-plot/cocoa_rating_chart.vg.json";
vegaEmbed("#scatter_plot", vg_4).then(function(result) {
// Access the Vega view instance
// (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

