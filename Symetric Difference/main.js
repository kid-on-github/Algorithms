function sym(args) {
    let symDiff = []
    let lastItem = -1
  
    for (let arg in arguments){
      for (let i in arguments[arg].sort()){
        i = arguments[arg][i]
        
        if(i == lastItem){}
        
        else if(symDiff.includes(i)){
          let index = symDiff.indexOf(i)
          symDiff.splice(index,1)
        }
        
        else{symDiff.push(i)}
        lastItem = i
      }
      lastItem = -1
    }
 
    return symDiff;
  }
  
  sym([1, 2, 3], [5, 2, 1, 4]);
  