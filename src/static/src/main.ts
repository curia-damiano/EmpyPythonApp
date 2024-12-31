document.addEventListener("DOMContentLoaded", () => {
	const message = "Hello, World from TypeScript!";
	console.log(message);
	document.body.innerHTML += `<p class='item'>${message}</p>`;
});
