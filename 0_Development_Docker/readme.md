# Docker for Development

This is a dumb example! But it shows the power of docker with little knowledge of the platform. Here, we'll use Docker to stand up a MySQL server, and play with it with a Jupyter notebook. How handy! This takes about a minute to stand up, which is WAY better than the windows install...

Install docker here:
`https://docs.docker.com/docker-for-windows/`

Docker Hub is where people publish these images, that we'll pull down a SQL server from! See here:
`https://hub.docker.com/_/mysql`

`docker_run.bat` shows how I would usually run this container for development purposes. Try it out! It contains this command:
`docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password mysql`
Key parts:
`docker run` - Starts a new container
`-d` - Runs the container "detached", so no logging messages to the console.
`-p 3306:3306` Maps the container port 3306 to localhost 3306, so we can connect to it!
`-e MYSQL_ROOT_PASSWORD=password` gives the container an environmental variable, which MYSQL will read in, to give us a root account password!
`mysql` tells docker we want to run the 'docker' image.

See the notebook for how we can use this server!

### Some Handy Docker Commands:

Once the container is started, we can use the docker command line interface to see what is running, restart or stop containers, and inspect containers. A few really useful commands are:

`docker ps` - Lists what containers are running. Note the container ID! When you want to stop the container, you'll need this.

`docker stop <containerID>` - halts a container. You can put in partial ID's or names here, as long as it isn't ambiguous.

`docker container prune` - Deletes all stopped containers. If we're quickly iterating over containers, we could have a bunch of them taking up space!

`docker image prune` - Same as above, but with images.

`docker exec` - Lets you run commands in a container. Typically I'll use `docker exec -it <containerID> bash` to get to a shell, so I can poke around.

Future work:
Map a volume, so the data persists! If we can't store it in memory, this can help us a lot!
