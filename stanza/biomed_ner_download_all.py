#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 20:31:38 2020

@author: MAGESHWARAN
"""

import stanza

# Universal dependencies
# For BIO there are 2 packages craft and genia
# But only craft follows new tokenization
uds = {"bio": "craft", "clinical": "mimic"}

for ud in uds.values():
    stanza.download(lang="en", package=ud)

# BIO NER packages
# key: corpus, value: package name, supported entities in comments
bioNer = {"AnatEM": "anatem", # ANATOMY
          "BC5CDR": "bc5cdr", # CHEMICAL, DISEASE
          "BC4CHEMD": "bc4chemd", # CHEMICAL
          "BioNLP13CG": "bionlp13cg", # AMINO_ACID, ANATOMICAL_SYSTEM, CANCER, CELL, CELLULAR_COMPONENT, DEVELOPING_ANATOMICAL_STRUCTURE, GENE_OR_GENE_PRODUCT, IMMATERIAL_ANATOMICAL_ENTITY, MULTI-TISSUE_STRUCTURE, ORGAN, ORGANISM, ORGANISM_SUBDIVISION, ORGANISM_SUBSTANCE, PATHOLOGICAL_FORMATION, SIMPLE_CHEMICAL, TISSUE
          "JNLPBA": "jnlpba", # PROTEIN, DNA, RNA, CELL_LINE, CELL_TYPE
          "Linnaeus": "linnaeus", # SPECIES
          "NCBI-Disease": "ncbi_disease", # DISEASE
          "S800": "s800" # SPECIES
          }

for ner in bioNer.values():
    stanza.download(lang="en", package=uds["bio"], processors={"ner": ner})

  
# Clinical NER Packages
# key: corpus, value: package name, supported entities in comments
clinicalNer = {"i2b2-2010": "i2b2", # PROBLEM, TEST, TREATMENT
          "Radiology": "radiology" # ANATOMY, OBSERVATION, ANATOMY_MODIFIER, OBSERVATION_MODIFIER, UNCERTAINTY
          }


for ner in clinicalNer.values():
    stanza.download(lang="en", package=uds["clinical"], processors={"ner": ner})
