# RedHat OpenShift image with Newrelic's Python agent

This is a test repository to demonstrate an Openshift image with the New Relic Python agent
Instructions for building and running:

**NOTE - this Docker container requires two things:**

1. An ISV / partner account with Red Hat as you need to run the container on a RHEL7 host
2. An account / license key from Newrelic - https://newrelic.com/signup

After getting the above, then proceed with the below
1. Install a RHEL7 host
2. Install Docker on that host
3. Download/clone this git repo
4. Go to https://www.newrelic.com and obtain a license key (xxxxx).
5. Build the Docker image `docker build -t newrelic-admin-rhel73/python-agent .`
6. Once the image is built, launch the container:
* `docker run -e NEW_RELIC_LICENSE_KEY=xxxxx -e NEW_RELIC_APP_NAME=hello-openshift newrelic-admin-rhel73/python-agent`
7. This will launch the container and print 5 test messages and send metrics for those to your NewRelic account

# How it works
The included `Dockerfile` sets the `newrelic-admin run-program` command as an entrypoint. This guarantees that all commands will run with `newrelic-admin run-program` prepended, even if a customer overrides the command.
For example, `docker run openshift-demo echo "hello world"` will actually run the command `newrelic-admin run-program echo hello world`.

The following environment variables are set by default:
```
NEW_RELIC_LOG=stderr
NEW_RELIC_LOG_LEVEL=info
NEW_RELIC_ENABLED=true
```

In addition, the newrelic python package is installed and an example program is copied into the image and set to run by default.

# Usage
The `NEW_RELIC_LICENSE_KEY` env variable is required to be set in order to report data to New Relic.
The `NEW_RELIC_APP_NAME` env variable is also required to set up reporting to a particular application in New Relic.

```bash
# Build the image
docker build -t newrelic-admin-rhel73/python-agent .

# Run the image with the NEW_RELIC_LICENSE_KEY variable set
docker run -e NEW_RELIC_LICENSE_KEY=xxxxx -e NEW_RELIC_APP_NAME=hello-openshift newrelic-admin-rhel73/python-agent
```
