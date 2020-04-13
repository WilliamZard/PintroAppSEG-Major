# Timeline API

## Access

Cloud Console: [https://console.cloud.google.com/functions/details/europe-west2/generate_timeline?project=bluej-pintro-project&tab=general](https://console.cloud.google.com/functions/details/europe-west2/generate_timeline?project=bluej-pintro-project&tab=general)

## Deployment

1. Open a command line session
2. Enter the `SEG-Major-BlueJ/backend/timeline` directory
3. Run `gcloud functions deploy generate_timeline --runtime python37 --trigger-http --allow-unauthenticated --region=europe-west2`

    This command creates a GCP function that executes the [`main.py`](http://main.py) script,  is triggered via HTTP requests, and can receive public requests. All requests are then authenticated when the function interacts with the Graph API, ensuring no unauthorized access to the rest of our sysem.

## Development

As with the Graph API app, we follow a TDD approach to developing the Timeline API. Unlike the Graph API, we use unittest as our `ython testing framework, and mock connections to the rest of our system. These tests are solely for testing the algorithm and response of the Cloud Function.

If you have not already, build the Docker image for running tests:

1. Open a command line session
2. Enter the `SEG-Major-BlueJ/backend/timeline` directory
3. Run `docker build -f test.Dockerfile -t timeline:test .`

    This will build a Docker image using the test.Dockerfile in the directory. The image will be called timeline, with the test tag.

To develop the algorithm with a TDD approach:

1. Write unit tests in `SEG-Major-BlueJ/backend/timeline/test.py`
2. Make sure you are in `SEG-Major-BlueJ/backend/timeline` directory
3. Run the unit tests using ```docker run --rm -it -v `pwd`:/timeline/ timeline:test```
4. View the output of your tests, update your source code accordingly, and continue the TDD cycle