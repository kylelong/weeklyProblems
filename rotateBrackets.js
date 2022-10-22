const brackets = [ ['(', ')'], ['{', '}'], ['[', ']'] ];
const matches = (open, close) => {
    let arr = brackets.filter(bracket => bracket === open);
    console.log(arr);
}
var isValid = function(s) {
    const open = ['(', '[', '{'];
    let stack = [];
    for(let i = 0; i < s.length; i++){
        let c = s.charAt(i);
        if(open.includes(c)){
            stack.push(c);
        } else{
            if(stack.length != 0){
                matches(stack.pop(), c);
            }
        }
    }
    
};

isValid("()");