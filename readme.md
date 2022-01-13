

## model

modules are the fuzzers themselves. a single module should take care of initializing everything needed for a particular fuzz target.
it will be able to collect all of the necessary information to begin a fuzz worker loop.

modules make use of plugins.o


Fuzzers represent a fuzzer for a particular Target type
    Fuzzers run Generators to generate FuzzInputs
        FuzzInputs are passed through a Connector
            Connectors define an interface for a Fuzzer use to pass FuzzInputs to FuzzTargets
                FuzzTargets represent the final target being fuzzed and expose a generic interface that describes how the target should receive 


```
Fuzzer():
    -Generator -> FuzzInputs
```