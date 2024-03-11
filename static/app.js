document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.star').forEach(star => {
      star.addEventListener('click', function() {
        const taskId = this.dataset.taskId;
        let isImportant = this.dataset.important === 'true';
  
        // Toggle the star appearance
        this.style.color = isImportant ? 'black' : 'yellow';
        this.dataset.important = !isImportant;
  
        // Send a fetch request to update importance
        fetch(`/update_important/${taskId}`, {      // fetch is used to send a request to the server
          method: 'POST',                           // POST request to update the importance of the task
          headers: {                                // Headers are used to specify the type of content being sent
            'Content-Type': 'application/json',     // JSON content type
          },                                        // The body of the request is the data that is being sent
          body: JSON.stringify({ important: !isImportant })  // The data is sent in JSON format
        })                                  // The response from the server is then converted to JSON format
        .then(response => response.json())  // The JSON data is then logged to the console
        .then(data => {                     // If there is an error, it is logged to the console
          console.log('Success:', data);    // If the request is successful, the data is logged to the console
        })
        .catch((error) => {  // If there is an error, it is logged to the console
          console.error('Error:', error); 
        });
      });
    });
  });
  