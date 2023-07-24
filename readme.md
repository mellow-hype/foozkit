# foozkit - a homebrew modular fuzzing kit

project for learning to write custom fuzzers. 

modules are the fuzzers themselves. a single module should take care of initializing everything needed for a particular fuzz target.
it will be able to collect all of the necessary information to begin a fuzz worker loop.
