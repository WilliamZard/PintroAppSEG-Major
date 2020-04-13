# Graph API

## Access

Cloud Endpoints Dashboard: [https://console.cloud.google.com/endpoints/api/bluej-pintro-project.appspot.com/overview?project=bluej-pintro-project&duration=PT1H](https://console.cloud.google.com/endpoints/api/bluej-pintro-project.appspot.com/overview?project=bluej-pintro-project&duration=PT1H)

View the "Deployments History" section to see the current and past deployments.

## Deploying

To deploy the Graph API Cloud Endpoints service:

1. Open a command line session
2. Enter the `SEG-Major-BlueJ/backend/graph` directory
3. Run `gcloud endpoints services deploy openapi-appengine.yaml`

## Developing

The entire Cloud Endpoint service is defined in the `openapi-appengine.yaml` file.

To develop this service, make changes to that configuration file. Currently there is no dedicated testing environment for this configuration. However, when deploying the endpoints service, the YAML file is validated and any syntax or semantic errors are caught.