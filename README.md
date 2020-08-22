## Bio-medical and Clinical NER: spacy, stanza, sciSpacy, HunFlair(flair)

This repository contains various templates / utilities to run bio-medical and clinical ner using spacy, sciSpacy, stanza and flair.

## Dependencies
```
pip install -r requirements.txt
```

## Usage: Refer to framework specific documentation(Readme.md)
1. [stanza](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/stanza) -State Of The Art (Tokenizer, Tagger, Parser, NER)
2. [med7NER](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/med7-spacy) -Tagger, Parser, 7 Clinical NER(Dosage, drug, duration, form, frequeny, route, strength)
3. [sciSpacy](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/sciSpacy) -NER, Abbrevation detector and Entity linker
4. [HunFlair](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/HunFlair) -Bio-medical NER based on flair framework, achieves SOTA(comparison without fine-tuning), Easy framework for biomedical fine-tuning, training and pre-training
