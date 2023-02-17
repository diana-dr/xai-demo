<template>
  <div class="container">
    <div class="list">
    <div class="list1">
    <h2>User Ranking</h2>
    <draggable :list="itemList" ghost-class="ghost" @end="onEnd" @change="onChange">
      <transition-group>
        <div class="sortable" v-for="element in itemList" :key="element.rank" @click="onclick(element)">
          <span class="rank" :class="{active: element.rank === isActive}" :style="{'background': element.color}"><b> {{ element.rank }} </b></span>
          <strong class="item" :class="{active: element.rank === isActive}" :style="{'background': element.color}"> {{ element.name }} </strong>
        </div>
      </transition-group>
    </draggable>
  </div>
  </div>

    <div class="list" v-if="showRank" id="rankList">
      <div class="list2">
        <h2>3rd Party Ranking</h2>
        <div v-for="item in third_rank" :key="item">
        <ul>
            <li @click="onclick(item)">
              <strong>
                <div class="rank" :class="{active: item.rank === isActive}" :style="{'background': item.color}">{{item.rank}}</div>
                <div class="item" :class="{active: item.rank === isActive}" :style="{'background': item.color}">{{item.name}}</div>
              </strong>
            </li>
        </ul>
        </div>
        <button style="background:transparent; border:none; color:transparent;" id="redoButton"><b>Redo Ranking</b></button>
        </div>

      <!-- <div class="list">
        <div v-for="item in third_rank" :key="item">
        <ul>
            <li>
              <div class="explanation" :class="{explanation: item.rank === isActive}" v-if="item.rank !== isActive"> ...</div>
              <div class="item" :class="{active: item.rank === isActive}" v-if="item.rank === isActive"> Explanation for {{item.rank}}</div>
            </li>
        </ul>
        </div>
        <button style="background:transparent; border:none; color:transparent;"></button>
      </div> -->
      <div class="explanation">
        <h2>Explanation</h2>
        <div v-if="showShap"><h3>Global Explanation</h3></div>
        <div class="icon-container">
        <img src="../../question_mark.png" alt="Icon" class="question_img">
        <span class="text">
          <p style="margin-left: 20px"> We have ranked these songs based on: </p>
          <ul>
            <pre><span>
            <li><b>Popularity.        </b> The higher the value the more popular the song is.</li>
            <li><b>Danceability.      </b> The higher the value, the easier it is to dance to the song.</li>
            <li><b>Key.               </b> The key the track is in.</li>
            <li><b>Loudness (dB).     </b> The higher the value, the louder the song.</li>
            <li><b>Mode.              </b> Indicates the modality (major or minor) of a track.</li>
            <li><b>Speechiness.       </b> The higher the value the more spoken word the song contains.</li>
            <li><b>Acousticness.      </b> The higher the value the more acoustic the song is.</li>
            <li><b>Instrumentalness.  </b> The number of vocals in a song.</li>
            <li><b>Liveness.          </b> The higher the value, the more likely the song is a live recording.</li>
            <li><b>Valence.           </b> The higher the value, the more positive mood for the song.</li>
            <li><b>Tempo.             </b> The overall estimated tempo of a track in beats per minute (BPM).</li>
            <li><b>Duration.          </b> Duration of the song (ms).</li>
            <li><b>Time signature.    </b>No. of beats are in each bar (or measure).</li>
          </span></pre>
          </ul></span>
      </div>
      <div class='plots'>
      <div id="loading">
      <img src="../../loading.gif" alt="Loading..." id="loading_img">
      </div>
      <div v-if="showShap" id="shap_image"><img src="../../../shap_graph.svg"/></div>
      <div id="simi" v-if="showShap" style="width: 350%"></div>
      <!-- <div id="bubble_test"></div> -->
      <!-- <div id="bubble_df"></div>
      <div id="df_line"></div>
      <div id="df_violin"></div>
      <div id="df_scatter"></div> -->
  <div v-if="showShap"><h3>Item Level Explanation</h3></div>
        <!-- <div class="text">
          <h2>Global Explanation</h2>
          <h2>Item Level Explanation</h2>
        </div> -->

        <div id='myDiv2'>
        </div>
        <div id='myDiv3'>
        </div>
        <div id='myDiv'>
        </div>
        </div>
      </div>
    </div>
  </div>
  <button @click="submit()" id="button"><b>Submit Ranking</b></button>
</template>

<script>

// import { stringify } from 'qs';
import {defineComponent} from 'vue'
import {VueDraggableNext} from 'vue-draggable-next'
import {getRanking, postRanking, getPreference} from '../api/api'
import { f1 } from "../plot_functions/plot.js";
import { f3 } from "../plot_functions/plot.js";
import { item_similarity3 } from "../plot_functions/plot.js";
import { barplot } from "../plot_functions/global.js";
// import {bubble} from '../plot_functions/global'

// function getthird_rankRanking() {
//   let names = ["Tom", "Sandra", "Bob", "Tim", "Nina"];
//   names = names.sort(() => Math.random() - 0.5);
//   return names.map((x, i) => ({rank:i+1, name:x}));
// }

const dfd = require("danfojs")

export default defineComponent({
  name: "UserRanking",
  components: {
    draggable: VueDraggableNext,
    // CompareRanking
  },
  data() {
    return {
      enabled: true,
      // itemList: [
      //   {rank: 1, name: "Tom"},
      //   {rank: 2, name: "Sandra"},
      //   {rank: 3, name: "Bob"},
      //   {rank: 4, name: "Tim"},
      //   {rank: 5, name: "Nina"},
      // ],
      itemList: null,
      dragging: false,
      third_rank: null, //{rank: name}
      color: {red: '#DE424AFF', yellow: '#FEE191', green: '#B0DBA4', blue:"rgba(19, 117, 255, 0.985)"},
      isActive: '',
      ThirdRanking: this.loadRanking(),
      showShap: false,
      showRank: false,
      showPlot: false
    }
  },
  methods: {
    // Plots
    test() {
      this.items2 = new dfd.DataFrame(this.third_rank);
      this.temp = [...this.third_rank]
      this.items1 = new dfd.DataFrame(this.temp.sort(() => Math.random() - 0.5));
      // console.log(this.items1, this.items2)
      
      let scaler = new dfd.MinMaxScaler()
      
      this.items1.drop({columns: ["id", "artist", "song", "duration_ms", "explicit", "year", "mode","genre","name","rank", "color"], inplace: true});
      this.items2.drop({columns: ["id", "artist", "song", "duration_ms", "explicit", "year", "mode","genre","name","rank", "color"], inplace: true});
      // this.diff = this.items1.sub(this.items2)
      // scaler.fit(this.diff)
      // this.diff = scaler.transform(this.diff)
      // this.diff.plot("diff").bar()
      
      this.simi = this.items1.copy()
      
      this.simi=this.simi.drop({index: [0]})
      this.items1=this.items1.drop({index: [9]})
      this.simi=this.simi.sub(this.items1)//.abs()
      console.log(this.simi)
      scaler.fit(this.simi)
      this.simi = scaler.transform(this.simi)
      
      // for (let i = 1; i < this.items1.shape[0]; i++) {
      //   const row0 = this.items1.loc({rows: [i-1]});
      //   const row1 = this.items1.loc({rows: [i]});
      //   console.log(row0.columns)
      //   this.simi.append([row0.sub(row1).values], [i-1])
      // }
      // console.log(this.simi)
      this.simi.plot("simi").bar()
      // this.simi.plot("simi").box()
      // this.simi.plot("df_line").line()
      // this.simi.plot("df_violin").violin()
      // this.simi.plot("df_scatter").scatter({
      //           // config: { x: "Age", y: "Fare" }
      //         })



    },

    loadRanking() {
      // backend interative functions
      getRanking().then(response => {
        this.itemList = [...response.data];
        this.third_rank = structuredClone(this.itemList);
        console.log(this.third_rank);
      })
    },
    load3rdRanking() {
        return [...this.itemList];
    },
    
    submitRankings() {
        postRanking(this.itemList, this.third_rank).then(response => {
          // console.log(stringify(this.itemList === this.third_rank));
          // console.log(response);
          this.feature_importance = response.data.feature_importance;
          this.item_explanations = response.data.item_explanations;
          // console.log(this.feature_importance)
          // console.log(this.item_explanations)
        })        
        setTimeout(() => document.getElementById('loading').style.display = 'none', 25000);
        setTimeout(() => this.showShap = true, 25000);
        // setTimeout(() => {var elem = document.createElement("img");
        //                   elem.className = "shapClass";
        //                   elem.src = "../../../shap_graph.svg"; 
        //                   document.getElementById("shap_image").appendChild(elem);}, 25000);
        setTimeout(() => barplot(this.third_rank), 25000);
        // setTimeout(() => {
        //   // Load the HTML file using AJAX or fetch
        //   fetch('bar.html')
        //   .then(response => response.text())
        //   .then(html => {
        //   document.querySelector('#simi').innerHTML = html;
        //   });
        //   }, 20000);
    },

    getUserPref() {
        getPreference().then(response => {
          console.log(response.data)
          this.shap_image = [...response.data]
        })
    },

    // frontend functions

    onChange: function() {
      this.itemList = [...this.itemList].map((item, index) => {
        const newSort = index + 1;
        // also add in a new property called has changed if you want to style them / send an api call
        item.hasChanged = item.rank !== newSort;
        if (item.hasChanged) {
          item.rank = newSort;
        }
        return item;
      });
    },

    log(event) {
      console.log(event)
    },

    onEnd: function(event) {
      console.log(event)
    },

    onclick(item) {
      this.isActive = this.isActive === item.rank ? 0 : item.rank;
      f3(this.itemList[item.rank - 1], this.third_rank[item.rank - 1]);
      item_similarity3(this.itemList[item.rank - 1], this.third_rank[item.rank - 1]);
      f1(this.itemList[item.rank - 1], this.third_rank[item.rank - 1]);
      // f2(this.itemList[item.rank - 1], this.third_rank[item.rank - 1]);
    },

    submit: function() {

      document.getElementById('button').style.background ="transparent";
      document.getElementById('button').style.color ="transparent";
      this.showRank = true;

      // sort by name
      this.itemList.sort((a, b) => a.name.localeCompare(b.name));
      this.third_rank.sort((a, b) => a.name.localeCompare(b.name));

      // Same rank: Green, near: yellow, close:white, far: red
      for (let i = 0; i < this.itemList.length; i++) {
        if(Math.abs(this.itemList[i].rank - this.third_rank[i].rank) > this.itemList.length * 0.5) {
          this.itemList[i].color = this.color['red'];
          this.third_rank[i].color = this.color['red'];
        }
        if(Math.abs(this.itemList[i].rank - this.third_rank[i].rank) <= this.itemList.length * 0.2) {
          this.itemList[i].color = this.color['yellow'];
          this.third_rank[i].color = this.color['yellow'];
        }
        if(this.itemList[i].rank === this.third_rank[i].rank) {
          this.itemList[i].color = this.color['green'];
          this.third_rank[i].color = this.color['green'];
        }
      }
      // sort by rank
      this.itemList.sort((a, b) => a.rank - b.rank);
      this.third_rank.sort((a, b) => a.rank - b.rank);
      // send to backend
      this.submitRankings();
    }
  },
})
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.container {
  display: flex;
  flex-wrap: wrap;
}

.list {
  margin: 10px;
  margin-top: -110px;
  margin-left: -100px;
}

.list2, .list1 {
  float: left;
  flex-basis: 20%;
}

.explanation {
  float: right;
  flex-basis: 30%;
  margin: 10px;
  margin-top: 0px;
  // margin-left: -100px;
}

.list, .draggable {
  display: inline-block;
  // width: 15%;
}

.container {
  min-width: max-content;
}

strong {
  //display: inline-block;
  font-size: 12px;
}

.sortable {
  // width: 40%;
  margin-bottom: 15px;

  span {
    font-size: 12px;
  }
}

.list .sortable-drag {
  opacity: 0;
}

.flip-list-move {
  transition: transform 0.5s;
}
.ghost {
  border-left: 6px solid rgb(0, 183, 255);
  box-shadow: 10px 10px 5px -1px rgba(0,0,0,0.14);
  opacity: .7;

  &::before {
    content: " ";
    position: absolute;
    width: 20px;
    height: 20px;
    margin-left: -50px;
  }
}

pre {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 12px;
  // margin: 0.5em 0;
  white-space: pre-line;
  // overflow: auto;
  // padding: 0;
  // margin: 0;
}

button {
  font-size: 16px;
  transition-duration: 0.4s;
  color: rgb(231, 231, 231);
  background-color: gray;
  border: none;
  border-radius: 3px;
}

#rankList {
    margin-left: 10px;
}

#button {
  padding: 10px 24px;
  margin-top: 20px;

  &:hover {
    background-color: rgb(0, 183, 255);
    color: rgb(231, 231, 231);
  }
}


.rank {
  display: inline;
  width: 10px;
  margin-right: 10px;
  /*border: 1px solid black;*/
  // width: 30%;
  background: rgb(231, 231, 231);
  padding: 1em;
  cursor: move;
  border-radius: 3px;
}

.item {
  display: inline-block;
  width: 20em;
  padding: 1em;
  /*border: 1px solid black;*/
  border-radius: 4px;
  background: rgb(231, 231, 231);
}

.active {
  /*border: 1px solid #0E0E0EF9;*/
  /* font-size: larger; */
  outline: 2px solid #0E0E0EF9;
}

.explanation {
  display: inline-block;
  margin-left: 30px;
  // width: 50%;
  // margin-left: 100px;
  // margin-top: 200px;
}

.plots {
  position: absolute;
  z-index: -1;
}

ul {
  //padding: 10px;
  margin-left: -20px;
  list-style-type: none;
}

a {
  color: #42b983;
}

.icon-container {
  position: absolute;
  top: 40px;
  right: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.icon-container img {
  height: 30px;
}

.icon-container .text {
  top: 30px;
  // right: -50px;
  background-color: #333;
  color: #fff;
  padding: 5px;
  border-radius: 5px;
}

.text {
  position: relative;
  top: 20px;
  // right: calc(100% + 10px);
  background-color: #fff;
  padding: 10px;
  width: 200px;
  box-shadow: 0px 2px 5px rgba(0,0,0,0.2);
  display: none;
  width: 900%;
}

.icon:hover + .text {
  display: block;
}

.icon-container:hover .text {
  display: block;
  
}
.shapClass {
  margin-left: 30px;
  max-width: 90%;
  height: auto;
}

#loading_img {
  max-width: 20%;
  height: auto;
}

</style>