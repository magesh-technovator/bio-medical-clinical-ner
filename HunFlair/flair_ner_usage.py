#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:12:40 2020

@author: MAGESHWARAN
"""

# -----------------Template for using hunflair for BioMedical NER--------------
from flair.data import Sentence
from flair.models import MultiTagger
from flair.tokenization import SciSpacyTokenizer

# make a sentence and tokenize with SciSpaCy
sentence = Sentence("Behavioral abnormalities in the Fmr1 KO2 Mouse Model of Fragile X Syndrome",
                    use_tokenizer=SciSpacyTokenizer())

# load biomedical tagger
tagger = MultiTagger.load("hunflair")

# inference
tagger.predict(sentence)

# print sentence with predicted tags
print(sentence.to_tagged_string())


# Entities may have multiple words, here's an easy way to get each annotated span
for disease in sentence.get_spans("hunflair-disease"):
    print(disease)

# Can be converted to dictionary, to get additional information
print(sentence.to_dict("hunflair-disease"))

# =============================================================================
# Above examples are for diseases, similarly you can get cell-lines, genes, species, and chemical entites
# hunflair-cellline: cell lines
# hunflair-chemical: chemicals
# hunflair-gene: genes and proteins
# hunflair-species: species
# exmaple: print(sentence.to_dict("hunflair-species"))
# =============================================================================

# To get all entites at once,
for entity in sentence.get_spans():
    print(entity)