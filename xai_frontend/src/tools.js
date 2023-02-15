// Swap key values
function Swap(obj) {
    const ret = {};
    Object.keys(obj).forEach(key => {
      ret[obj[key]] = key;
    });
    return ret;
  }
  
  // Common keys of 2 Objects
  function intersection(o1, o2) {
    return Object.keys(o1).filter({}.hasOwnProperty.bind(o2));
  }
  
  // All items
  function union(o1, o2) {
    let u = new Set(Object.keys(o1));
    for (const key of Object.keys(o2)) {
      u.add(key);
    }
    return u;
  }
  