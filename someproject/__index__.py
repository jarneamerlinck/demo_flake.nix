# Imports
import speechtotext
from speechtotext.datasets import Dataset
from speechtotext.benchmark.customBenchmarks import *
from speechtotext.benchmark.benchmarks import run_benchmarks, Benchmark
from speechtotext.functions import force_cudnn_initialization
from speechtotext.plot.plotting import Plotting

import speechtotext.metric.customMetrics
force_cudnn_initialization()
print("All loaded in!!!!!!!!!!")
