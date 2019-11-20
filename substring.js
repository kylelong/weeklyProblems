String.prototype.mySubstring = function(a, b = null){

    s = "";
    if(b == null){
        for(var i = a; i < this.length; i++){
            s += this.charAt(i);
        }
    } else{
        for(var i = a; i < b; i++){
            s += this.charAt(i);
        }
    }
    return s;
}
console.log("hello world!".mySubstring(1,5)); //ello
console.log("hello world!".mySubstring(6)); //world!
