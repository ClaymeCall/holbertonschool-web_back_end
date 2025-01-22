// Use the process module for to allow interaction with console
const process = require('process');

// Prompt the user to input text
process.stdout.write("Welcome to Holberton School, what is your name?\n");

// Get user input
process.stdin.on('readable', () => {
	const name = process.stdin.read();
	if (name) {
		process.stdout.write(`Your name is: ${name}`);
	}
});

// Print a message upon closing the input stream
process.stdin.on('end', () => {
	console.log('This important software is now closing');
});
