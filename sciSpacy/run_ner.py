#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 05:49:33 2020

@author: MAGESHWARAN
"""

import spacy

model = spacy.load("en_core_sci_sm")

text = 'A patient was prescribed Magnesium hydroxide 400mg/5ml suspension PO of total 30ml bid for the next 5 days.'
doc = model(text)

print([(ent.text, ent.label_) for ent in doc.ents])
