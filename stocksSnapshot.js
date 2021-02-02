
/** 
 * You are given a snapshot of a queue of stocks that have changing 
 * prices coming in from a stream. Remove the outdated stocks from the queue.
 * $ snapshot = [
  { sym: ‘GME’, cost: 280 },
  { sym: ‘PYPL’, cost: 234 },
  { sym: ‘AMZN’, cost: 3206 },
  { sym: ‘AMZN’, cost: 3213 },
  { sym: ‘GME’, cost: 325 }
]
$ stockQueue(snapshot)
$ [{ sym: ‘PYPL’, cost: 234 },
   { sym: ‘AMZN’, cost: 3213 },
   { sym: ‘GME’, cost: 325 }]
 */
let snapshot = [
    { sym: "GME", cost: 280 },
    { sym: "PYPL", cost: 234 },
    { sym: "AMZN", cost: 3206 },
    { sym: "AMZN", cost: 3213 },
    { sym: "GME", cost: 325 }
  ];
function stockQueue(snapshot){
    let stocks = {};
    snapshot.forEach(function(stock){
        stocks[stock.sym] = stock;
    });
    return stocks;
}
console.log(stockQueue(snapshot));
