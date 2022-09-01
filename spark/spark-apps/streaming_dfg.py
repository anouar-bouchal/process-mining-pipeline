from pm4py.streaming.stream.live_event_stream import LiveEventStream
from pm4py.streaming.algo.discovery.dfg import algorithm as dfg_discovery


live_event_stream = LiveEventStream()
streaming_dfg = dfg_discovery.apply()
live_event_stream.register(streaming_dfg)
live_event_stream.start()

# Append and process events or traces
for event in events:
    live_event_stream.append(event)
# live_event_stream.stop()

dfg, activities, sa, ea = streaming_dfg.get()