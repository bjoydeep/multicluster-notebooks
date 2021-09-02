

# Trying out the Web Apps

## Background
If jupyter notebook with all python code is not your style, here is a another way to enjoy the same benefits (well almost!). This takes the logic from the notebooks, and generates a simple low overhead web app using [streamlit](https://streamlit.io/).  A few of the notebooks have been taken and converted into web app. No attempt has been made to beautify the presentation yet - example: Labels, legends etc could be much more improved. And unlike the notebook, which controlled access to the data through the user bearer token, this gives you access to all the data. With a little more work, this can be fixed ofcourse.

## To kick the tyres
1. log into [quay.io](https://quay.io/repository/)
1. log into your Openshift Cluster that is running [Red Hat Advanced Cluster Management (ACM) Hub with Observability](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.3/html/observability/observing-environments-intro#enable-observability) enabled in the command line
1. clone this repo
1. navigate to webapp directory
1. run: `make deploy` 

This will create the following in the ACM hub Cluster:
- a namespace called `analytics` 
- a `route` in the namespace called `analytics`. 

Launch that route-url and have fun.

## If you want to build
1. fork this repo
1. Update the makefile - it points to `quay.io/bjoydeep/`. Point it to your repo.
1. run `make publish`

## To destroy 
To destroy the artifacts created in the Openshift Cluster just delete the `analytics` namespace.






