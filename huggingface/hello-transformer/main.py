from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

#response = classifier("I like Large Language models very much") # This is a positive sentiment
#print(response)

response = classifier("I got irritate standing in line at airport") # This is a negative sentiment
print(response)