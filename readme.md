# Practical Docker for Data Science

The idea here isn't to be a definitive intro to docker or devops, just to hand you a few tools to keep in your back pocket. I use Docker daily for testing things locally on my computer, and deploying ML both on-premise and to the cloud. We're going to deploy a quick model trained on the Iris dataset.

The 'Development_Docker' directory is an example of how I often use Docker for development work.

The 'Simplest' directory is a minimal working example of a Flask application, with a simple function as our predictor.

The 'Simplest_Docker' directory is the above, in docker!

The 'Database_and_Flask' dir is a bad example of how you can build multi-container apps work together, using docker compose.

The 'Database_Flask_FastAPI' dir is another (probably bad) example of how to make a distributed app, with a scalable back end. I'll talk through the tool I often use to deploy to kubernetes as well.

Again- No real industry best practices here, just enough knowledge to leverage these tools to make your life easier.  
