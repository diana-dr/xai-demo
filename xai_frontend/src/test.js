function getDummyRanking() {
  var names = ["Tom", "Sandra", "Bob", "Tim", "Nina"];
  names = names.sort(() => Math.random() - 0.5);
  indexes = names.indexOf(names)
  return Object.assign({}, names)
}
obj = getDummyRanking()

function RankingAgree(r1, r2, key) {
    return r1[key] === r2[key]
}

function intersection(o1, o2) {
    return Object.keys(o1).filter({}.hasOwnProperty.bind(o2));
}

function Swap(obj) {
    const ret = {};
    Object.keys(obj).forEach(key => {
      ret[obj[key]] = key;
    });
    return ret;
  }

o = Swap(obj)


function union(o1, o2) {
    let u = new Set(Object.keys(o1));
    for (const key of Object.keys(o2)) {
      u.add(key);
    }
    return u;
  }
  

var names = ["Tom", "Sandra", "Bob", "Tim", "Nina"];
names = names.sort(() => Math.random() - 0.5);
rank = names.map((x, i) => ({rank:i+1, name:x}))
select_name = rank.map(x => (({name}) => ({name}))(x).name)
console.log(...select_name)

console.log(...rank.sort((a, b) => a.name.localeCompare(b.name)));

console.log(rank.length)


// getRanking()