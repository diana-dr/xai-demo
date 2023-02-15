import Plotly from 'plotly.js-dist';

export function f2(item, third_party) {
    // var trace2 = {
    //     x: [item.popularity, item.popularity, item.popularity],
    //     y: [item.speechiness, item.instrumentalness, item.liveness],
    //     mode: 'lines+markers',
    //     type: 'scatter',
    //     name: item.name
    // };
    
    // var trace3 = {
    //   x: [third_party.popularity, third_party.popularity, third_party.popularity],
    //   y: [third_party.speechiness, third_party.instrumentalness, third_party.liveness],
    //     mode: 'lines+markers',
    //     type: 'scatter',
    //     name: third_party.name
    // };

        var trace1 = {
      x: [item.popularity, third_party.popularity],
      y: [item.speechiness, third_party.speechiness],
        mode: 'lines+markers',
        type: 'scatter',
        name: 'Speechiness'
    };

    var trace2 = {
      x: [item.popularity, third_party.popularity],
      y: [item.liveness, third_party.liveness],
        mode: 'lines+markers',
        type: 'scatter',
        name: 'Liveness'
    };

    var trace3 = {
      x: [item.popularity, third_party.popularity],
      y: [item.instrumentalness, third_party.instrumentalness],
        mode: 'lines+markers',
        type: 'scatter',
        name: 'Instrumentalness'
    };
    
    var data = [trace1, trace2, trace3];
    var layout = {
        xaxis: {
          autorange: true,
          // range: [60, 100],
          title: 'Popularity' 
        },
        yaxis: {
          autorange: true,
          // range: [0, 1],
          title: ' '
        },
        plot_bgcolor: 'rgb(255, 255, 255)',
        paper_bgcolor: 'rgb(255, 255, 255)',
        colorway: ["#DE3163", "#6495ED", '#FF7F50'],
    }

    Plotly.newPlot('myDiv2', data, layout)
}

// sns.regplot(x=df["popularity"], y=df["speechiness"], label='speechiness')
// sns.regplot(x=df["popularity"], y=df["instrumentalness"], label='instrumentalness')
// sns.regplot(x=df["popularity"], y=df["liveness"], label='liveness')

export function f1(item, third_party) {

      var trace1 = {
    x: [item.popularity, third_party.popularity],
    y: [item.energy, third_party.energy],
      mode: 'lines+markers',
      type: 'scatter',
      name: 'Energy'
  };

  var trace2 = {
    x: [item.popularity, third_party.popularity],
    y: [item.danceability, third_party.danceability],
      mode: 'lines+markers',
      type: 'scatter',
      name: 'Danceability'
  };

  var trace3 = {
    x: [item.popularity, third_party.popularity],
    y: [item.valence, third_party.valence],
      mode: 'lines+markers',
      type: 'scatter',
      name: 'Valence'
  };

  var trace4 = {
    x: [item.popularity, third_party.popularity],
    y: [item.speechiness, third_party.speechiness],
      mode: 'lines+markers',
      type: 'scatter',
      name: 'Speechiness'
  };

  var trace5 = {
    x: [item.popularity, third_party.popularity],
    y: [item.liveness, third_party.liveness],
      mode: 'lines+markers',
      type: 'scatter',
      name: 'Liveness'
  };

  var trace6 = {
    x: [item.popularity, third_party.popularity],
    y: [item.instrumentalness, third_party.instrumentalness],
      mode: 'lines+markers',
      type: 'scatter',
      name: 'Instrumentalness'
  };

  var trace7 = {
    x: [item.popularity, third_party.popularity],
    y: [item.acousticness, third_party.acousticness],
      mode: 'lines+markers',
      type: 'scatter',
      name: 'Acousticness'
  };
  
  var data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7];
  var layout = {
    title: "Features in Correlation to Popluarity",
      xaxis: {
        autorange: true,
        // range: [60, 100],
        title: 'Popularity' 
      },
      yaxis: {
        autorange: true,
        // range: [0, 1],
        title: ' '
      },
      plot_bgcolor: 'rgb(255, 255, 255)',
      paper_bgcolor: 'rgb(255, 255, 255)',
      colorway: ["#DE3163", "#6495ED", '#FF7F50', '#F4A460', "#C2B280", "#7D7D7D", "#ADD8E6"],
    }

  Plotly.newPlot('myDiv', data, layout)
}

// export function f2(item, third_party) {


//   lotly.newPlot('myDiv2', data, layout)
// }

export function item_similarity3(song1, song2) {
// Calculate the difference between the values of each feature
const features = ['energy', 'danceability', 'speechiness', 'instrumentalness', 'liveness', 'valence', 'acousticness']
const diffs = [];
for (let i = 0; i < features.length; i++) {
  const diff = song1[features[i]] - song2[features[i]];
  diffs.push({
    name: features[i],
    x: 0,
    y: diff,
    size: Math.abs(diff),
  });
}

// Create the data for the bubble plot
const data = [{
  x: diffs.map(d => d.name),
  y: diffs.map(d => d.y),
  text: diffs.map(d => d.name),
  type: "scatter",
  mode: 'markers',
  marker: {
    size: 20,
    sizemode: 'area',
    color: '#DE3163'
  }
}];

// Create the layout for the bubble plot
const layout = {
  title: 'Feature Difference',
  xaxis: {
    title: ''
  },
  yaxis: {
    title: 'Value'
  }
};

// Create the bubble plot
  Plotly.newPlot('myDiv3', data, layout);
}

export function f3(item, third_party) {
  // ['energy', 'danceability', 'speechiness', 'instrumentalness', 'liveness', 'valence', 'acousticness']
  // Define the data for the chart
  const name1 = item.song
  const name2 = third_party.song

var trace1 = {
  // x: [name1, name2],
  x: ['Energy', 'Danceability', 'Speechiness', 'Instrumentalness', 'Liveness', 'Valence', 'Acousticness'],
  y: [item.energy, item.danceability, item.speechiness, item.instrumentalness, item.liveness, item.valence, item.acousticness],
    type: 'bar',
    name: name1
};

var trace2 = {
  x: ['Energy', 'Danceability', 'Speechiness', 'Instrumentalness', 'Liveness', 'Valence', 'Acousticness'],
  y: [third_party.energy, third_party.danceability, third_party.speechiness, third_party.instrumentalness, 
    third_party.liveness, third_party.valence, third_party.acousticness],
    type: 'bar',
    name: name2
};

// var trace3 = {
//   x: [name1, name2],
//   y: [item.valence, third_party.valence],
//     type: 'bar',
//     name: 'Valence'
// };

// var trace4 = {
//   x: [name1, name2],
//   y: [item.speechiness, third_party.speechiness],
//     type: 'bar',
//     name: 'Speechiness'
// };

// var trace5 = {
//   x: [name1, name2],
//   y: [item.liveness, third_party.liveness],
//     type: 'bar',
//     name: 'Liveness'
// };

// var trace6 = {
//   x: [name1, name2],
//   y: [item.instrumentalness, third_party.instrumentalness],
//     type: 'bar',
//     name: 'Instrumentalness'
// };

// var trace7 = {
//   x: [name1, name2],
//   y: [item.acousticness, third_party.acousticness],
//     type: 'bar',
//     name: 'Acousticness'
// };

var data = [trace1, trace2]; //, trace3, trace4, trace5, trace6, trace7];

// Define the layout for the chart
const layout = {
  title: "Feature Comparison",
  xaxis: {
    title: "Songs"
  },
  yaxis: {
    title: "Value"
  },
  barmode: "group",
  plot_bgcolor: 'rgb(255, 255, 255)',
  paper_bgcolor: 'rgb(255, 255, 255)',
  colorway: ['#F4A460', "#C2B280"]//, '#FF7F50', '#F4A460', "#C2B280", "#7D7D7D", "#ADD8E6"],
};

// Create the chart
Plotly.newPlot("myDiv2", data, layout);

}