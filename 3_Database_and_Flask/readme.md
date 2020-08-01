# Database and Flask
So we've covered some fundamentals already- We've launched a database, we've made our first toy Flask project, let's put some legos together.

When building a stack of more than one container, we'll want to use `docker-compose`, which can handle multi-container deployments, specified by Yaml files, which are mostly human readable!

We'll make some tweaks to the 1_Simplest app we made, to store our user's submissions, so we have historical records of what they want predicted. This could help us retrain the model, or just extract insights about our userbase.

Check out docker-compose.yml, we'll walk through it like by line. The documentation is fantastic, and can be found here:
https://docs.docker.com/compose/

See the similarities between docker-compose.yml and the command from the 0th lesson? We map ports, map volumes, and pass in environmental variables about the same way.

We can start our stack with the command `docker-compose up`. By default, it displays logs on screen. We can hide this by adding the -d (for detached, just like in lesson 0).

After it's all started, visit `localhost`, we should have the app running! Once we make some submissions, we can pull those records out in the included notebook, to see that it's functioning.

Take a look at the Flask app now, and what changed. Not a huge difference, right? The dockerfile was changed slightly, we're now building the app from the 1_Simplest directory.

Note that in the app we can say, `mysql` for the server address within a stack, but need `localhost` as our server location from our computer. Docker translates those hostnames for containers, but not for us. Still- Handy!
