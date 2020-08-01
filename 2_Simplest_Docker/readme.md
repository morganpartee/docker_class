# Let's pack this thing up!  

We'll put this app in a dockerfile.

Docker will package this app, install the packages we need (if we need them), and run the flask app.

We can even make this more production ready with GUnicorn if we want!

Check out the `dockerfile` in this dir to see! Note there is no extension, that is normal.

Remember `docker hub`? There are prebuilt python containers that we'll leverage. We'll just declare `from python:3.7.8-alpine3.11` to show that we're using python 3.7, and this particular distro uses alpine linux. More info here: `https://hub.docker.com/_/python`

In the dockerfile, we'll copy the app to the host. See the `copy` command.

`RUN pip install flask` installs the flask library, which we need to make this work.

`EXPOSE` tells docker to let other people access port 80 here- The standard port for HTTP.

`ENTRYPOINT` is where the container 'enters', or starts the part that we care about. That will contain the python command to start the app!

So... what next? We build it, we run it! And give it a meaninful name. Try:
`docker build --tag important_app .`
That period means to build everything in the directory.
Try:
`docker run important_app -p 80:80` to run this thing!
Visit localhost to see if it worked.
