#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 05:49:33 2020

@author: MAGESHWARAN
"""

import stanza
import os
from tqdm import tqdm
import pandas as pd

inputPath = r"/home/user/Documents/"
documents = os.listdir(inputPath)

navigateTo = r"text"

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
        nerModel = stanza.Pipeline(lang="en", # package=ud,
                                   processors={"tokenize": "spacy",
                                               "ner": model[0]})
    
        modelResult = []
        print("Model:" + model[0] + "is in progress")
        
        for document in tqdm(documents):
            try:
                if os.path.isdir(os.path.join(inputPath, document, navigateTo)):
                    for file in os.listdir(os.path.join(inputPath, document, navigateTo)):
                        
                        if file.endswith(".txt"):
                            modelLabels = {key: [] for key in model[1].split(">")}
                            modelLabels["other"] = []
                            
                            fp = open(os.path.join(inputPath, document, navigateTo, file))
                            content = fp.read()
                            content = content.replace("\n", " ").replace("\t", " ").replace(".", " ").replace("  ", " ")
                            
                            fp.close()
                            
                            annot = nerModel(content)
                            
                            if len(annot.ents):
                                for ent in annot.entities:
                                    if not modelLabels[ent.type]:
                                        modelLabels[ent.type] = [ent.text]
                                    
                                    else:
                                        modelLabels[ent.type].append(ent.text)

                            modelLabels["Document ID"] = document
                            modelLabels["Page Number"] = file.split(".txt")[0]
                            
                            modelResult.append(modelLabels)
            except FileNotFoundError:
                print(document)
                        
        testData = pd.DataFrame(modelResult, columns = list(modelLabels.keys()))

        testData.to_csv("PredictionReports/" + model[0]+".csv")
