# NLPcore
Stanford NLP Library

pip install pycorenlp

pip install stanza

Stanza is a Python natural language analysis package. It contains tools, which can be used in a pipeline, to convert a string containing human language text into lists of sentences and words, to generate base forms of those words, their parts of speech and morphological features, to give a syntactic structure dependency parse, and to recognize named entities. The toolkit is designed to be parallel among more than 60 languages, using the Universal Dependencies formalism.

Stanza includes a Python interface to the CoreNLP Java package and inherits additonal functionality from there, such as constituency parsing, coreference resolution, and linguistic pattern matching.

Getting Started
We strongly recommend installing Stanza with pip, which is as simple as:

pip install stanza
To see Stanza’s neural pipeline in action, you can launch the Python interactive interpreter, and try the following commands:

>>> import stanza
>>> stanza.download('en') # download English model
>>> nlp = stanza.Pipeline('en') # initialize English neural pipeline
>>> doc = nlp("Barack Obama was born in Hawaii.") # run annotation over a sentence
You should be able to see all the annotations in the example by running the following commands:

>>> print(doc)
>>> print(doc.entities)

For more details on how to use the neural network pipeline, please see our Getting Started Guide and Tutorials.
