#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 05:49:33 2020

@author: MAGESHWARAN
"""

import spacy

# med7 = spacy.load("en_core_med7_lg")
med7 = spacy.blank("en").from_disk("model_256_16_332.bin")

# create distinct colours for labels
# =============================================================================
# col_dict = {}
# seven_colours = ['#e6194B', '#3cb44b', '#ffe119', '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']
# for label, colour in zip(med7.pipe_labels['ner'], seven_colours):
#     col_dict[label] = colour
# 
# options = {'ents': med7.pipe_labels['ner'], 'colors':col_dict}
# 
# =============================================================================
text = 'A patient was prescribed Magnesium hydroxide 400mg/5ml suspension PO of total 30ml bid for the next 5 days.'
doc = med7(text)

# spacy.displacy.render(doc, style='ent', jupyter=True, options=options)

# print([(ent.text, ent.label_) for ent in doc.ents])


def filter_spans(spans):
    # Filter a sequence of spans so they don't contain overlaps
    # For spaCy 2.1.4+: this function is available as spacy.util.filter_spans()
    get_sort_key = lambda span: (span.end - span.start, -span.start)
    sorted_spans = sorted(spans, key=get_sort_key, reverse=True)
    result = []
    seen_tokens = set()
    for span in sorted_spans:
        # Check for end - 1 here because boundaries are inclusive
        if span.start not in seen_tokens and span.end - 1 not in seen_tokens:
            result.append(span)
        seen_tokens.update(range(span.start, span.end))
    result = sorted(result, key=lambda span: span.start)
    return result


def extract_drug_relations(doc):
    # Merge entities and noun chunks into one token
    spans = list(doc.ents) + list(doc.noun_chunks)
    spans = filter_spans(spans)
    with doc.retokenize() as retokenizer:
        for span in spans:
            retokenizer.merge(span)

    relations = []
    for drug in filter(lambda w: w.ent_type_ == "DRUG", doc):
        print(drug.dep_)
        if drug.dep_ in ("attr", "dobj"):
            print(list(drug.head.lefts))
            subject = [w for w in drug.head.lefts]
            dummy = [w for w in drug.head.rights]
            print(dummy)
            if subject:
                subject = subject[0]
                relations.append((subject, drug))
        elif drug.dep_ == "pobj" and drug.head.dep_ == "prep":
            relations.append((drug.head.head, drug))
    return relations


relations = extract_drug_relations(doc)
for r1, r2 in relations:
    print("{:<10}\t{}\t{}".format(r1.text, r2.ent_type_, r2.text))


for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])

# spacy.displacy.render(doc, style='dep', jupyter=False)

