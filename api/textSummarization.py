import torch
import json 
import time
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

def abstractSummarize(text):
    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    device = torch.device('cpu')

    preprocess_text = text.strip().replace("\n","")
    t5_prepared_Text = "summarize: "+preprocess_text

    tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)


    # summmarize 
    summary_ids = model.generate(tokenized_text,
                                        num_beams=4,
                                        no_repeat_ngram_size=2,
                                        min_length=30,
                                        max_length=100,
                                        early_stopping=True)

    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    print ("\n\nSummarized text: \n",output)

    # Summarized output from above ::::::::::
    # the us has over 637,000 confirmed Covid-19 cases and over 30,826 deaths. 
    # president Donald Trump predicts some states will reopen the country in april, he said. 
    # "we'll be the comeback kids, all of us," the president says.


def extractSummarize(text):
    # Object of automatic summarization.
    auto_abstractor = AutoAbstractor()
    # Set tokenizer.
    auto_abstractor.tokenizable_doc = SimpleTokenizer()
    # Set delimiter for making a list of sentence.
    auto_abstractor.delimiter_list = [".", "\n"]
    # Object of abstracting and filtering document.
    abstractable_doc = TopNRankAbstractor()
    # Summarize document.
    result_dict = auto_abstractor.summarize(text, abstractable_doc)

    # Output result.
    print(len(result_dict["summarize_result"]))
    limit = int((len(result_dict["summarize_result"]))/3)
    i = 1
    for sentence in result_dict["summarize_result"]:
        print(sentence)
        if i >= limit: 
            break
        #i += 1

def main():
    text ="""
    Now then, the great period of Greek philosophy is approximately 385, which is roughly the date of Plato’s first dialogue, to 323. This is the death of Aristotle. And here, because of the difficulties in answering the question what, here the question became how, in the sense of how do you know? If you answer, what, you give certain scientific information and then a person will say, well how do you know that? So the subject matter is epistemology and the question is how do you know the knowledge and act you’ve pointed out. The emphasis is on knowledge.
Now after the death of Aristotle the next development began about the year 300 B. C. and it continued until A. D. 529. A very long period of time, I won’t say a completely unimportant period of time but the importance is diluted by the number of years and these people were interested a little in science and some epistemology and I don’t want you to get the idea that those things were forgotten but the chief interest was in ethics and you might say, “well what should we do about?” And that is the history of Greek philosophy in three parts. 529 is the year in which Justinian closed the schools of philosophy in the East. Of course, the East had become moribund and the West had been conquered by the invading barbarians, and civilization was extinguished for about 1,000 years. Now that’s a little outline.
Now for the early period of Greek philosophy say up through Heraclitus, I would like to mention five things to summarize them and I hope you noticed them as you were going through but we’ll take this minute to sort of get started. They were interested in finding the one stuff out of which the universe was made. They thought it would be irrational for the universe to consist of 94 or 152 elements or some other definite number. Can you in the next minute and a half or 30 seconds figure out a reason why the universe should consist of precisely 94 or 16 or 132 elements? You see there is no reason that can justify one such number rather than another. And hence, they thought that if the universe were rational as they assumed it was, it would have to be constituted of one stuff. They didn’t agree on the stuff but they agreed on the fact that it was one. And that of course is the important point, not just what they _____.
The second of these five point is that this one stuff is everlasting. It was never created, it would never be destroyed it is the eternal substance. In a moment, I’ll give you some reasons for this. But let’s go through the five points first.
The third point is that in contrast with the universe as a whole the cosmos is limited. Now the word cosmos is a word that is known by all ladies for another. One of the most important words of the English language is derived from the word cosmos, what is it? Cosmetics. Having come from a wedding ceremony what is uppermost in your mind? It’s the word cosmetics. Can any of your guess why there is a connection between cosmos and cosmetics? Oh its not so hard as all that. Cosmos and cosmetics. Well, the opposite of cosmos I suppose is what the young ladies would describe before they use their cosmetics. Chaos.
"""

    #print("Reference text:" + text)

    print("Using extractive approach")
    start1 = time.time()
    extractSummarize(text)
    end1 = time.time()
    print("Runtime:" + str(end1 - start1))

    print("Using abstractive approach")
    start2 = time.time()
    abstractSummarize(text)
    end2 = time.time()
    print("Runtime:" + str(end2 - start2))

main()