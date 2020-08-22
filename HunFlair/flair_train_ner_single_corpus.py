#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:54:41 2020

@author: MAGESHWARAN
"""

# ----Template for Training HunFlair on specific NER datasets from scratch-----

from flair.datasets import NCBI_DISEASE

# 1. get the corpus
corpus = NCBI_DISEASE()
print(corpus)

# 2. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type="ner")

# 3. initialize embeddings
from flair.embeddings import WordEmbeddings, FlairEmbeddings, StackedEmbeddings

embedding_types = [

    # word embeddings trained on PubMed and PMC
    WordEmbeddings("pubmed"),

    # flair embeddings trained on PubMed and PMC
    FlairEmbeddings("pubmed-forward"),
    FlairEmbeddings("pubmed-backward"),
]


embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

# 4. initialize sequence tagger
from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger(
    hidden_size=256,
    embeddings=embeddings,
    tag_dictionary=tag_dictionary,
    tag_type="ner",
    use_crf=True,
    locked_dropout=0.5
)

# 5. initialize trainer
from flair.trainers import ModelTrainer

trainer: ModelTrainer = ModelTrainer(tagger, corpus)

trainer.train(
    base_path="taggers/ncbi-disease",
    train_with_dev=False,
    max_epochs=200,
    learning_rate=0.1,
    mini_batch_size=32
)