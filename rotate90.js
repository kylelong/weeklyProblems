//Given an n x n array, rotate it 90 degrees without making a new array.
/* 
$ rotate90([[1,2,3],[4,5,6],[7,8,9]])
$ [[7,4,1],[8,5,2],[9,6,3]]
*/
let rotate90 = function(matrix) {
    let top = 0;
    let bottom = matrix.length - 1;
    while(top <= bottom){
        let tmp = matrix[top];
        matrix[top] = matrix[bottom];
        matrix[bottom] = tmp;
        top++;
        bottom--;
    }
    for(let i = 0; i < matrix.length; i++){
        for(let j = i + 1; j < matrix[0].length; j++){
            let tmp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = tmp;
        }
    }
    return matrix;
};
console.log(rotate90([[1,2,3],[4,5,6],[7,8,9]])); //[[7,4,1],[8,5,2],[9,6,3]]
console.log(rotate90([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])); //[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
