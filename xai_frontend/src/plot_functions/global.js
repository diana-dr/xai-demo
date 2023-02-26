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
    try {
        df.drop({columns: ["id", "artist", "song", "duration_ms", "explicit", "year", "mode", "genre", "name", "rank", "color"], inplace: true});
      } catch (error) {
        df.drop({columns: ["id", "artist", "song", "duration_ms", "explicit", "year", "mode", "genre", "name", "rank"], inplace: true});
      }
    // Scale the data using MinMaxScaler
    const scaler = new dfd.MinMaxScaler();
    scaler.fit(df);
    let X = scaler.transform(df);

    let colors = ['#FAD6A5',
    '#F0B775',
    '#F1E1C9',
    '#8A7F66',
    '#C0C3A3',
    '#8BB8A8',
    '#A7D2C1',
    '#E7EAD2',
    '#F2B2A8',
    '#F9CDAD',
    '#F3D3BD',
    '#FCE5CD']
    // let colors = ['#DE3163', '#6495ED', '#FFC300', '#FF5733', '#DAF7A6', '#C70039', '#00A5E3', '#8B00FF', '#7CFC00', '#FF1493', '#00BFFF', '#F0E68C', '#A0522D'];

    let data = [];
    for (let rank = 0; rank < 10; rank++) {
        let trace = {
            x: X.columns,
            y: X.data,
            name: names[rank],
            marker: {
            color: colors[rank],
            opacity: 1,
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

    X.plot("simi").bar({
        layout: {
            title: "<b>Global Features</b>",
            xaxis: {
              title: "Songs"
            },
            yaxis: {
              title: "Value"
            },
            colorway: colors,
            barmode: 'stack',
        }
    })

}


  