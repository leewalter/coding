# sample python code to use as Prometheus client
# ref - https://github.com/prometheus/client_python

from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.

    i = 0
    while True:
       i += 1
       print("Sample python client code to test Prometheus library, counter is ", i )
       # process_request(random.random())
       process_request(random.uniform(0,3))

'''
Sample python client code to test Prometheus library, counter is  1
Sample python client code to test Prometheus library, counter is  2
Sample python client code to test Prometheus library, counter is  3
Sample python client code to test Prometheus library, counter is  4
Sample python client code to test Prometheus library, counter is  5
Sample python client code to test Prometheus library, counter is  6
.....

then http://localhost:8000/
# HELP python_gc_collected_objects Objects collected during gc
# TYPE python_gc_collected_objects histogram
# HELP python_gc_uncollectable_objects Uncollectable object found during GC
# TYPE python_gc_uncollectable_objects histogram
# HELP python_gc_duration_seconds Time spent in garbage collection
# TYPE python_gc_duration_seconds histogram
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="7",patchlevel="0",version="3.7.0"} 1.0
# HELP request_processing_seconds Time spent processing request
# TYPE request_processing_seconds summary
request_processing_seconds_count 9.0 <------counter 
request_processing_seconds_sum 16.841596455
# TYPE request_processing_seconds_created gauge
request_processing_seconds_created 1.549348740074782e+09

'''
