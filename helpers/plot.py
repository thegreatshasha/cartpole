import plotly.plotly as p
import datetime
import time
import numpy as np
import json
from plotly.graph_objs import *
import plotly.plotly as py
from plotly.graph_objs import *
import timeit

class Plotter:

    def __init__(self, config):
        self.config = config
        #import pdb; pdb.set_trace()
        # self.plot =  p.iplot([{'x': [], 'y': [], 'type': 'scatter', 'mode': 'lines+markers',
        #             'stream': {'token': self.config['streaming_token'], 'maxpoints': 80}
        #           }],
        #         filename='Time-Series', fileopt='overwrite')
        trace1 = Scatter(
            x=[],
            y=[],
            stream=dict(token=self.config['streaming_token'])
        )
        data = Data([trace1])
        self.plot = py.plot(data)


        #self.url = self.plot.resource
        print "Plotting to: %s" % self.plot
        self.stream = py.Stream(self.config['streaming_token'])
        self.stream.open()

    def write(self, x, y):
        self.stream.write({'x': x, 'y': y})
