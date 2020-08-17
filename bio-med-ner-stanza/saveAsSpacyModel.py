#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:23:34 2020

@author: MAGESHWARAN
"""

import stanza
from spacy_stanza import StanzaLanguage

models = {"craft": [('anatem', "ANATOMY"),
                  ('bc5cdr',"CHEMICAL>DISEASE"), ('bc4chemd', "CHEMICAL"),
                  ('bionlp13cg', "AMINO_ACID>ANATOMICAL_SYSTEM>CANCER>CELL>CELLULAR_COMPONENT>DEVELOPING_ANATOMICAL_STRUCTURE>GENE_OR_GENE_PRODUCT>IMMATERIAL_ANATOMICAL_ENTITY>MULTI-TISSUE_STRUCTURE>ORGAN>ORGANISM>ORGANISM_SUBDIVISION>ORGANISM_SUBSTANCE>PATHOLOGICAL_FORMATION>SIMPLE_CHEMICAL>TISSUE"),
                  ('jnlpba', "PROTEIN>DNA>RNA>CELL_LINE>CELL_TYPE"),
                  ('linnaeus', "SPECIES"),
                  ('ncbi_disease', "DISEASE"),
                  ('s800', "SPECIES")
                  ],
          "mimic": [("i2b2", "PROBLEM>TEST>TREATMENT"),
                       ("radiology", "ANATOMY>OBSERVATION>ANATOMY_MODIFIER>OBSERVATION_MODIFIER>UNCERTAINTY")]
          }

for ud in models.keys():
    for model in models[ud]:
        stanzaModel = stanza.Pipeline(lang="en", # package=ud,
                                   processors={"tokenize": "spacy",
                                               "ner": model[0]})
        
        nerModel = StanzaLanguage(stanzaModel)
        nerModel.to_disk("model/" + model[0])
     