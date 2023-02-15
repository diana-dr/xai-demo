<template>
  <div class="container">
  <div class="list">
    <h1>User Ranking</h1>
    <draggable :list="itemList" ghost-class="ghost" @end="onEnd" @change="onChange">
      <transition-group>
        <div class="sortable" v-for="element in itemList" :key="element.rank" @click="onclick(element)">
          <span class="rank" :class="{active: element.rank === isActive}" :style="{'background': element.color}"><b> {{ element.rank }} </b></span>
          <strong class="item" :class="{active: element.rank === isActive}" :style="{'background': element.color}"> {{ element.name }} </strong>
        </div>
      </transition-group>
    </draggable>
    <button @click="submit()" id="button"><b>Submit Ranking</b></button>

  </div>

    <div style="display:none" id="rankList">
      <div class="list">
        <h1>3rd Party Ranking</h1>
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
      <div id='plots' class="explanation">
        <div class="text">
          <h3>Explanation</h3>
          We have ranked these songs based on:
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
          </ul>
          <h3>Global Explanation</h3>
          <h3>Item Level Explanation</h3>
        </div>
        <div id='myDiv'>
        </div>
        <div id='myDiv2'>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>

import { stringify } from 'qs';
import {defineComponent} from 'vue'
import {VueDraggableNext} from 'vue-draggable-next'
import {getRanking, postRanking, getPreference} from '../api/api'
import { f1 } from "../plot_functions/plot.js";
import { f2 } from "../plot_functions/plot.js";

// function getthird_rankRanking() {
//   let names = ["Tom", "Sandra", "Bob", "Tim", "Nina"];
//   names = names.sort(() => Math.random() - 0.5);
//   return names.map((x, i) => ({rank:i+1, name:x}));
// }

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
    }
  },
  methods: {
    loadRanking() {
      // backend interative functions
      getRanking().then(response => {
        this.itemList = [...response.data];
        this.third_rank = structuredClone(this.itemList);
        // console.log(this.third_rank);
      })
    },
    load3rdRanking() {
        return [...this.itemList];
    },
    submitRankings() {
        postRanking(this.itemList, this.third_rank).then(response => {
          console.log(stringify(this.itemList === this.third_rank));
          console.log(response.data);
        })
    },
    getUserPref() {
        getPreference().then(response => {
          console.log(response.data)
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
      f1(this.itemList[item.rank - 1], this.third_rank[item.rank - 1]);
      f2(this.itemList[item.rank - 1], this.third_rank[item.rank - 1]);
    },
    submit: function() {
      document.getElementById('rankList').style.display = "inline-block";

      document.getElementById('button').style.background ="transparent";
      document.getElementById('button').style.color ="transparent";


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

.list, .draggable {
  display: inline-block;
  // width: 15%;
}

.container {
  min-width: max-content;
}

strong {
  //display: inline-block;
  font-size: 14px;
}

.sortable {
  // width: 40%;
  margin-bottom: 15px;

  span {
    font-size: 14px;
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
    margin-left: 50px;
}

#button {
  padding: 10px 24px;
  margin-top: 20px;

  &:hover {
    background-color: rgb(0, 183, 255);
    color: rgb(231, 231, 231);
  }
}

.rankrow {
  /*margin-top: 1em;*/
  //margin-bottom: 6px;
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

#plots {
  margin-top: -50px;
}

.active {
  /*border: 1px solid #0E0E0EF9;*/
  /* font-size: larger; */
  outline: 2px solid #0E0E0EF9;
}

.explanation {
  display: inline-block;
  margin-left: 50px;
  // width: 50%;
  // margin-left: 100px;
  // margin-top: 200px;
}

ul {
  //padding: 10px;
  margin-left: -20px;
  list-style-type: none;
}

li {
  //display: inline;
  //margin: 0 10px;
}

a {
  color: #42b983;
}

.text {
  // margin-top: -200px;
}

</style>
