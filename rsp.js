const readline = require("readline-sync");
console.log("Welcome to Rock, Paper, Scissors.")
let choice = readline.question("Enter R for Rock, P for Paper, or S for Scissors: ");
let choices = ["Rock", "Paper", "Scissors"];
let index = Math.floor(Math.random() * 3);
console.log("The computer chose: " + choices[index]);
let computer = choices[index].charAt(0);
if(computer == choice){
	console.log("Tie");
}
else if(computer == "R" && choice == "S"){
	console.log("You lost!");

}
else if(computer == "S" && choice == "P"){
	console.log("You lost!");
}
else if(computer == "P" && choice == "R"){
	console.log("You lost!");
}
else{
	console.log("You won!");
}