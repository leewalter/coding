from prometheus_client import Histogram
from prometheus_client import start_http_server, Summary
import random
import time

h = Histogram('request_latency_seconds', 'Description of histogram')
h.observe(4.7)    # Observe 4.7 (seconds in this case)

@h.time()
def f():
  pass

with h.time():
  pass

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.

    while True:
        h.observe(random.uniform(0,5))

'''
http://localhost:8000/

# HELP python_gc_collected_objects Objects collected during gc
# TYPE python_gc_collected_objects histogram
# HELP python_gc_uncollectable_objects Uncollectable object found during GC
# TYPE python_gc_uncollectable_objects histogram
# HELP python_gc_duration_seconds Time spent in garbage collection
# TYPE python_gc_duration_seconds histogram
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="7",patchlevel="0",version="3.7.0"} 1.0
# HELP request_latency_seconds Description of histogram
# TYPE request_latency_seconds histogram
request_latency_seconds_bucket{le="0.005"} 32001.0
request_latency_seconds_bucket{le="0.01"} 63749.0
request_latency_seconds_bucket{le="0.025"} 159652.0
request_latency_seconds_bucket{le="0.05"} 319993.0
request_latency_seconds_bucket{le="0.075"} 480149.0
request_latency_seconds_bucket{le="0.1"} 640626.0
request_latency_seconds_bucket{le="0.25"} 1.603277e+06
request_latency_seconds_bucket{le="0.5"} 3.208363e+06
request_latency_seconds_bucket{le="0.75"} 4.812899e+06
request_latency_seconds_bucket{le="1.0"} 6.417821e+06
request_latency_seconds_bucket{le="2.5"} 1.6053888e+07
request_latency_seconds_bucket{le="5.0"} 3.2115897e+07
request_latency_seconds_bucket{le="7.5"} 3.2115897e+07
request_latency_seconds_bucket{le="10.0"} 3.2115897e+07
request_latency_seconds_bucket{le="+Inf"} 3.2115897e+07
request_latency_seconds_count 3.2115897e+07
request_latency_seconds_sum 8.030116580928595e+07
# TYPE request_latency_seconds_created gauge
request_latency_seconds_created 1.549349734980678e+09
'''
