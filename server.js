// Import the Express module, which helps us build a web server

const express = require("express");
// Create an instance of an Express app
const app = express();

// Define the port number where the server will listen for requests
const port = 3000;

// Use Express's built-in middleware to parse incoming JSON data in request bodies
app.use(express.json());

// Create a temporary array to store posts in memory (this simulates a database)
let posts = [];

// Set up a route to handle POST requests made to "/posts"
// This route will receive data from the client and save it as a new post
// Example: Save the post to a data store
// Create a new post object with a unique id and the received title and content
// Add the new post to the posts array
// Respond with a 201 status code (Created) and send back the new post as JSON
app.post("/posts", (req, res) => {
  const { title, content } = req.body;

  const newPost = {
    id: posts.length + 1,
    title: title,
    content: content,
  };

  posts.push(newPost);

  res.status(201).json(newPost);
});

// Start the server and have it listen on the specified port
// Log a message to let us know the server is running
app.listen(port, () => {
  console.log("Server running at http://localhost:3000");
});
