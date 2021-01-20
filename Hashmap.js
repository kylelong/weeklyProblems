/** 
Design a hashmap without using any built-in libraries. You should include the following functions:

put(key, value): Insert a (key, value) pair into the hashmap. If the value already exists, update the value.

get(key): Returns the value to which key is mapped, or -1 if this map contains nothing for key.

remove(key): Remove the mapping for the value in key if it exists.
 */
 
 class Hashmap{
     constructor(dict = {}){
         this.dict = dict;
     }
     put(key, value){
        this.dict[key] = value;
     }
     get(key){
        return key in this.dict ? this.dict[key]:-1;
     }
 }
 let map = new Hashmap();
 map.put("year", 2021);
 map.put("month", "january");
 map.put("number", 123);
 console.log(map.get("number"));//123
 map.put("number", 21); //update existing key
 console.log(map.get("number"));//21
 console.log(map.get("year")); //2021
 console.log(map.get("month")); //january
 console.log(map.get(1)); //-1
