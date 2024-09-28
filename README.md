This is the source code for the second analysis of quasar time dilation.
The licence is MIT.

You need to compile the binary with `make`. This depends on
DNest4. Then you need to run process.py to convert the CSV file to the
appropriate plain text format for the C++ code.

```
python process.py > data.txt
```

Then you can run the sampling using `./main -t 8 -s 0` for 8 threads
and with an RNG seed of zero.
This will reproduce the "main model" results from the paper.
