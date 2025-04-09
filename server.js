// Import the Express module, which helps us build a web server

// Create an instance of an Express app

// Define the port number where the server will listen for requests

// Use Express's built-in middleware to parse incoming JSON data in request bodies

// Create a temporary array to store posts in memory (this simulates a database)

// Set up a route to handle POST requests made to "/posts"
// This route will receive data from the client and save it as a new post
// Example: Save the post to a data store
// Create a new post object with a unique id and the received title and content
// Add the new post to the posts array
// Respond with a 201 status code (Created) and send back the new post as JSON
app.post("/posts", (req, res) => {});

// Start the server and have it listen on the specified port
// Log a message to let us know the server is running
app.listen(port, () => {});
