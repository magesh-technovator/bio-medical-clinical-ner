#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:39:49 2020

@author: MAGESHWARAN
"""

# ---------Template for Fine-tuning HunFlair on specific NER datasets----------

# 1. load your target corpus
from flair.datasets import NCBI_DISEASE
corpus = NCBI_DISEASE()

# 2. load the pre-trained sequence tagger
from flair.models import SequenceTagger
tagger: SequenceTagger = SequenceTagger.load("hunflair-disease")

# 3. initialize trainer
from flair.trainers import ModelTrainer
trainer: ModelTrainer = ModelTrainer(tagger, corpus)

# 4. fine-tune on the target corpus
trainer.train(
    base_path="taggers/hunflair-disease-finetuned-ncbi",
    train_with_dev=False,
    max_epochs=200,
    learning_rate=0.1,
    mini_batch_size=32
)
