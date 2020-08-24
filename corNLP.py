# Download Stanford NLP Library at https://stanfordnlp.github.io/CoreNLP/download.html
# Navigate to your stanford NLP path and run this :- java -mx6g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 50000

from pycorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://localhost:9000')

text = "This movie was actually neither that funny, nor super witty. The movie was meh. I liked watching that movie. If I had a choice, I would not watch that movie again."

results = nlp.annotate(text,properties={
        'annotators':'sentiment, ner, pos',
        'outputFormat': 'json',
        'timeout': 50000,
        })

for s in results["sentences"]:
    print("{} : {}".format(" ".join(t["word"] for t in s["tokens"]),s["sentiment"]))