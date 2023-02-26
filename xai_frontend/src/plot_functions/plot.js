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

  Plotly.newPlot('myDiv', data, layout);
}

// export function f2(item, third_party) {

//   lotly.newPlot('myDiv2', data, layout)
// }

export function item_similarity3(song1, song2) {

// Calculate the difference between the values of each feature
const features = ['energy', 'danceability', 'speechiness', 'instrumentalness', 'liveness', 'valence', 'acousticness', 'loudness', 'key', 'popularity']
const diffs = [];
for (let i = 0; i < features.length; i++) {
  const diff = song1[features[i]] - song2[features[i]];
  diffs.push({
    name: features[i],
    x: 0,
    y: Math.abs(diff),
    size: Math.abs(diff),
  });
}

  const sizes = diffs.map(d => d.size);

  // Normalize the sizes between a specified minimum and maximum value
  const minSize = 20;
  const maxSize = 50;
  const normalizedSizes = sizes.map(size => (size - Math.min(...sizes)) / (Math.max(...sizes) - Math.min(...sizes)) * (maxSize - minSize) + minSize);


// Create the data for the bubble plot
const data = [{
  x: diffs.map(d => d.name),
  y: diffs.map(d => d.y),
  text: diffs.map(d => d.name),
  type: "scatter",
  mode: 'markers',
  marker: {
    size: normalizedSizes,
    sizemode: 'diameter',
    color: '#F67280'
  }
}];

// Create the layout for the bubble plot
const layout = {
  title: '<b>Feature Differences</b>',
  xaxis: {
    title: 'Features'
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
  title: "<b>Bar Plot of Feature Comparison</b>",
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

export function f4(item, third_party) {
  // const colors = ['#DE3163', '#6495ED', '#FFC300', '#FF5733', '#DAF7A6', '#C70039', '#00A5E3', '#8B00FF', '#7CFC00', '#FF1493', '#00BFFF', '#F0E68C', '#A0522D'];
  const labels = ["danceability", "mode", "speechiness", 
  "acousticness", "instrumentalness", "liveness", "valence", "duration", "timeSignature"];

  let x = [item.danceability, item.mode, item.speechiness, 
    item.acousticness, item.instrumentalness, item.liveness, item.valence, item.duration, item.timeSignature]
  let y = [third_party.danceability, third_party.mode, 
    third_party.speechiness, third_party.acousticness, third_party.instrumentalness, third_party.liveness, 
    third_party.valence, third_party.duration, third_party.timeSignature]

    const mrks = [];
    for (let i = 0; i < labels.length; i++) {
      mrks.push({
        name: labels[i],
        x: x[i],
        y: y[i],
      });
    }

  const data = [{  
    x: mrks.map(d => d.x),
    y: mrks.map(d => d.y),
    mode: 'markers',
    type: 'scatter',
    name: mrks.map(d => d.name),
    text: labels,
    marker: {
      // color: ['#DE3163', 'rgba(0, 0, 255, 0.8)'],
      color: '#C06C84',
      size: 20,
    },
  }];
    
  const layout = {
    title: "<b>Scatter Plot of Audio Features</b>",
    xaxis: {title: item.song},
    yaxis: {title: third_party.song},
    legend: {
      orientation: 'h',
      y: -0.2,
      // itemclick: false,
      // itemdoubleclick: false
    }
  };
  
  Plotly.newPlot('myDiv4', data, layout);
  
}

export function f5(song1, song2) {
  const trace1 = {
    x: ['danceability', 'energy', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence'],
    y: [song1.danceability, song1.energy, song1.speechiness, song1.acousticness, song1.instrumentalness, song1.liveness, song1.valence],
    mode: 'markers',
    type: 'scatter',
    name: song1.song,
    marker: {
      color: 'rgba(65, 105, 225, 0.5)',
      size: 25
    }
  };
  
  const trace2 = {
    x: ['danceability', 'energy', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence'],
    y: [song2.danceability, song2.energy, song2.speechiness, song2.acousticness, song2.instrumentalness, song2.liveness, song2.valence],
    mode: 'markers',
    type: 'scatter',
    name: song2.song,
    marker: {
      color: 'rgba(255, 127, 80, 0.5)',
      size: 25
    }
  };
  
  const data = [trace1, trace2];
  
  const layout = {
    title: '<b>Scatter Plot of Feature Comparison</b>',
    xaxis: {
      title: 'Features'
    },
    yaxis: {
      title: 'Values'
    }
  };    
    

// Create the plot
Plotly.newPlot('myDiv5', data, layout);

}

export function f6(song1, song2) {
  var trace1 = {
    type: 'scatterpolar',
    r: [song1.duration_ms, song1.explicit, song1.year, song1.popularity, song1.danceability, song1.energy, song1.loudness, song1.mode, song1.speechiness, song1.acousticness, song1.instrumentalness, song1.liveness, song1.valence, song1.tempo],
    theta: ['duration_ms', 'explicit', 'year', 'popularity', 'danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'],
    fill: 'toself',
    name: song1.song,
    marker: {
      color: 'rgba(143, 151, 121, 0.5)',
      line: {
        color: 'rgba(143, 151, 121, 1)',
        width: 2
      }
    }
  };
  
  var trace2 = {
    type: 'scatterpolar',
    r: [song2.duration_ms, song2.explicit, song2.year, song2.popularity, song2.danceability, song2.energy, song2.loudness, song2.mode, song2.speechiness, song2.acousticness, song2.instrumentalness, song2.liveness, song2.valence, song2.tempo],
    theta: ['duration_ms', 'explicit', 'year', 'popularity', 'danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'],
    fill: 'toself',
    name: song2.song,
    marker: {
      color: 'rgba(255, 160, 122, 0.5)',
      line: {
        color: 'rgba(255, 160, 122, 1)',
        width: 2
      }
    }
  };
  
  var data = [trace1, trace2];
  
  var layout = {
    polar: {
      radialaxis: {
        visible: true,
        range: [0, 1]
      }
    },
    showlegend: true,
    title: '<b>Radar Chart of Audio Features</b>'
  };
  
  Plotly.newPlot('myDiv6', data, layout);
  
}