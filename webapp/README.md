

# Trying out the Web Apps

## Background
If jupyter notebook with all python code is not your style, here is a another way to have almost same benefit. This takes the logic from the notebooks, and generates a simple low overhead web app using [streamlit](https://streamlit.io/).  A few of the notebooks have been taken and converted into web app. No attempt has been made to beautify the presentation yet - example: Labels, legends etc could be much more improved.

## To kick the tyres
1. log into quay.io
1. log into your cluster that is running ACM Hub
1. run: `make deploy` 

This will create a namespace called `analytics` in OCP and create a `route` in the namespace called `analytics`. Launch that route and have fun.

## If you want to build
1. Fork this repo
1. Update the makefile - it points to `quay.io/bjoydeep/`. Point it to your repo.
1. run `make publish`






