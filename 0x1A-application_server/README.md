# Application server
This task involved deployment of the AirBnB clone project. I was tasked with configuring Nginx on my server provided by ALX to serve a WSGI(Web Server Gateway Interface)Flask app running through Gunicorn. 

# What is Gunicorn?
Gunicorn (Green Unicorn) is a type of application server. Gunicorn is a popular WSGI (Web Server Gateway Interface) server for running Python web applications. It is designed to serve as a middle layer between the web server (like Nginx or Apache) and the Flask or Django application, handling the execution of the Python code and managing incoming HTTP requests.

# Why Gunicorn?
+ WSGI Compatibility: Gunicorn is WSGI-compliant, meaning it adheres to the WSGI standard for communication between web servers and Python web applications.

+ Multi-Worker Model: Gunicorn uses a multi-worker model, where multiple worker processes handle incoming requests simultaneously. This allows for improved performance and concurrency.

+ Ease of Use: Gunicorn is known for its simplicity and ease of use. It can be easily integrated with popular web frameworks like Flask and Django.

+ Load Balancing: Gunicorn supports basic load balancing by spawning multiple worker processes. This helps distribute incoming requests across the workers, improving the application's ability to handle concurrent connections.

+ Integration with Nginx or Other Web Servers: Gunicorn is often used in conjunction with web servers like Nginx or Apache. The web server handles tasks like static file serving, SSL termination, and load balancing, while Gunicorn focuses on executing the Python application code.

+ Production-Ready: Gunicorn is suitable for use in production environments and is commonly chosen for deploying Python web applications.

In a typical deployment setup, Nginx or another web server acts as a reverse proxy, forwarding requests to Gunicorn, which in turn handles the execution of the Python web application. This combination provides a robust and scalable architecture for serving Python web applications.