import Plotly from 'plotly.js-dist-min'

const dfd = require("danfojs")

// will plot bubble plot in a div given its ID
export const bubble = (div_id) => {
    var trace1 = {
        x: [1, 2, 3, 4],
        y: [10, 11, 12, 13],
        text: ['A<br>size: 40', 'B<br>size: 60', 'C<br>size: 80', 'D<br>size: 100'],
        mode: 'markers',
        marker: {
        color: ['rgb(93, 164, 214)', 'rgb(255, 144, 14)',  'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
        size: [40, 60, 80, 100]
        }
    };
    
    var data = [trace1];
    
    var layout = {
        title: 'Bubble Chart Hover Text',
        showlegend: false,
        height: 600,
        width: 600
    };
    
    Plotly.newPlot(div_id, data, layout);
}

export const barplot = (songs) => {
    // Assuming that songs is an array of objects containing the song data
    let df = new dfd.DataFrame(songs);
    let names = df['song'].values;
    df.drop({columns: ["id", "artist", "song", "duration_ms", "explicit", "year", "mode", "genre", "name", "rank"], inplace: true});
    // Scale the data using MinMaxScaler
    const scaler = new dfd.MinMaxScaler();
    scaler.fit(df);
    const X = scaler.transform(df);

    let colors = ['rgba(255, 174, 255, 0.5)', 'rgba(255, 255, 128, 0.5)', 'rgba(128, 255, 200, 0.5)',              
    'rgba(199, 174, 255, 0.5)', 'rgba(39, 140, 255, 0.5)', 'rgba(255, 122, 133, 0.5)', 'rgba(55, 174, 99, 0.5)',              
    'rgba(140, 100, 255, 0.5)', 'rgba(80, 150, 74, 0.5)', 'rgba(255, 255, 255, 0.5)', 'rgba(255, 174, 0, 0.5)'];

    let data = [];
    for (let rank = 0; rank < 10; rank++) {
        let trace = {
            x: X.columns,
            y: X[rank],
            name: names[rank],
            marker: {
            color: colors[rank],
            opacity: 0.1,
            line: {
                color: 'rgb(0,0,0)',
                width: 1.5
            }
            },
            type: 'bar',
            orientation: 'v'
        };
        data.push(trace);
    }

    let layout = {
    barmode: 'overlay',
    legend: {
        orientation: 'h',
        x: 0,
        y: 1.2,
        yanchor: 'bottom'
      }
    };

    let config = {
    responsive: true
    };

    Plotly.newPlot('simi', data, layout, config);

}


  