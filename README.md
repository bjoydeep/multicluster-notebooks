# multicluster-notebooks
Collection of notebooks for multicluster analytics

### Current Examples

1. Analysis of Alerts from multiple clusters.
1. Detecting if one Policy/Signal is triggered by another Policy/Signal.
1. Sample SLO/SLI for Kube API Server behaviour on a single cluster

### In Works

1. Detecting big changes in slope of time series data.
1. Detecting if multiple time series data - that should behave the same way - deviate from their expected behaviour. For example, it is expected that services operating in multiple clusters that are supposed to be loaded the same way deviate from one another.


It is no coincidence that all of these notebooks deal with time series that. All of the infrastructure metrics are time series data. Also forecasting work has not yet been done - not that it is too hard to do - because the metrics in the current data set that we are exploring will not yield anything meaningul if projected into the future. 


