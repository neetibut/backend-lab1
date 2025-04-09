// Import the Express module and create an instance of it

const express = require('express');
const app = express();

//Define the port number
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Declare a simple array called “posts” to temporarily store posts
let posts = [];

// Route to handle POST requests to create a new post
app.post('/posts', (req, res) => {
    const { title, content } = req.body;

    // Example: Save the post to a data store
    const newPost = {
        id: posts.length + 1,
        title: title,
        content: content
    };

    posts.push(newPost);

    res.status(201).json(newPost); // Respond with the saved post
});

// Start the server
app.listen(port, () => {
    console.log('Server running at http://localhost:3000');
});
