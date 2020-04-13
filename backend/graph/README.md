# Graph API App

## Access

App Engine Dashboard: [https://console.cloud.google.com/appengine?project=bluej-pintro-project&serviceId=default&duration=PT1H](https://console.cloud.google.com/appengine?project=bluej-pintro-project&serviceId=default&duration=PT1H)

## Deployment

1. Open a command line session,
2. Enter the `SEG-Major-BlueJ/backend/graph` directory
3. Run `gcloud app deploy --stop-previous-version`
4. When prompted to approve the deployment, enter yes.

Running this command will make the GCP SDK look for the file named `app.yaml`, which specifies our app engine configuration. This will in turn look for the production Dockerfile, named `Dockerfile` which will be used to deploy and execute the application.

## Development

Development of this micro-service employs a Test Driven Development(TDD) approach. Generally speaking, this will be the flow you follow:

If you have not already, build the Docker image used for running tests:

1. Make sure Docker is running on your machine
2. Enter the `SEG-Major-BlueJ/backend/graph` directory
3. Run `docker build -f test.Dockerfile -t graph_api:test .`

    This builds a Docker image based on the test.Dockerfile file, called graph_api, and tagged with the tag "test".

Then, write and run the tests:

1. Write unit tests in the `SEG-Major-BlueJ/backend/graph/graph_api/tests` directory, adhering to the test structure seen in the rest of the test files, and adhering to [pytest standards](https://docs.pytest.org/en/latest/goodpractices.html).
2. To run all the tests, enter this command ```docker run --rm -it -v `pwd`:/graph_api/ graph_api:test```

    This will create and run a Docker container that is mounted to your current working directory. In this case, that means you can make changes to your source code and rerun the tests in that Docker container without have to rebuild it, speeding up development significantly.

3. To run specific groups of tests, append to the above command `-m <TEST_MARK>` where TEST_MARK is the pytest identifier you've chosen for that test class.

    For example, all tests for calling GET on our /users/<user_email> endpoint are contained in the TestGet class in test_users.py. You will notice that this class is decorated with `@pytest.mark.GET_user`, so its mark is GET_user. To run just those tests, enter:

    ```docker run --rm -it -v `pwd`:/graph_api/ graph_api:test -m GET_user```

4. View the output of your tests, update your source code accordingly, and continue the TDD cycle

You can alternatively, and should you want to perform manual testing, do the following:

1. Build another Docker image:
    1. Make sure Docker is running on your machine
    2. Open a command line session
    3. Enter the `SEG-Major-BlueJ/backend/graph` directory
    4. Run `docker build -f dev.Dockerfile -t graph_api:dev .`

        This builds a Docker image based on the dev.Dockerfile file, called graph_api, and tagged with the tag "dev"

2. Run the Docker image using ```docker run --rm -it -v `pwd`:/graph_api/ -p 8080:8080 graph_api:dev```

    This will create and run a Docker container that is mounted to your current working directory. Meaning that any changes you make to your code are reflected in real time in the Docker container and the application it is running. Additionally, the `-p` argument means that the container is listening on its port 8080, which is currently being mapped to the host machine's(your computer) port 8080.

3. Now you can freely edit your code, see those changes reflected in the application, and make requests to [http://0.0.0.0:8080/](http://0.0.0.0:8080/)

    You will notice that if you open the above link in your browser, you will see a Swagger API Spec. You can explore the spec in your browser, and make requests to those endpoints  using the "Try it out" button on the right. However, we would recommend using a more powerful API tool such as [Postman](https://www.postman.com/).
