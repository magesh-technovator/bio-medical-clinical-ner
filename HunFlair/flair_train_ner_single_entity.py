#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 12:00:36 2020

@author: MAGESHWARAN
"""

# ---Template for Training HunFlair on specific Entity from multiple corpura---

from flair.datasets import HUNER_CELL_LINE

# Import and use corpura accordingly,
# chemicals: HUNER_CHEMICALS
# diseases: HUNER_DISEASE
# genes/proteins: HUNER_GENE
# Species: HUNER_SPECIES


# 1. get all corpora for a specific entity type
from flair.models import SequenceTagger
corpus = HUNER_CELL_LINE()

# 2. initialize embeddings
from flair.embeddings import WordEmbeddings, FlairEmbeddings, StackedEmbeddings
embedding_types = [
    WordEmbeddings("pubmed"),
    FlairEmbeddings("pubmed-forward"),
    FlairEmbeddings("pubmed-backward"),

]

embeddings = StackedEmbeddings(embeddings=embedding_types)

# 3. initialize sequence tagger
tag_dictionary = corpus.make_tag_dictionary(tag_type="ner")

tagger = SequenceTagger(
    hidden_size=256,
    embeddings=embeddings,
    tag_dictionary=tag_dictionary,
    tag_type="ner",
    use_crf=True,
    locked_dropout=0.5
)

# 4. train the model
from flair.trainers import ModelTrainer
trainer = ModelTrainer(tagger, corpus)

trainer.train(
    base_path="taggers/hunflair-cell-line", 
    train_with_dev=False, 
    max_epochs=200,
    learning_rate=0.1, 
    mini_batch_size=32
)