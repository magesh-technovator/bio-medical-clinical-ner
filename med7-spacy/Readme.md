## Med7 NER: [paper](https://arxiv.org/abs/2003.01271) [github](https://github.com/kormilitzin/med7/)

* Training Data: MIMIC-III free-text electronic health records
* Components: tagger, parser, clinical NER(Dosage, drug, duration, form, frequeny, route, strength)

### Details on NER
![Image description](https://github.com/MageshDominator/bio-medical-ner-spacy-stanza/blob/master/med7-spacy/images/med7ner.png)

### Available Models
| --width  | --depth | --embed-rows    |model size (MB) | epochs | URL      |
| --------:| -------:| -------------:  |--------------: |------: |-----:    |
| 96       |      4  |   10000         |      3.8       |    350 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_096_04_350.bin) |
| 128      |      8  |   10000         |      18.3      |    596 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_128_08_596.bin) |
| 256      |      8  |   10000         |      47.6      |    450 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_256_08_450.bin) |
| 256      |      16  |   10000         |     66.1      |    332 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_256_16_332.bin) |
| 300      |      8  |    20000       |       89.6      |    338 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_300_08_338.bin) |

The models were pre-trained on the entire MIMIC-III data, comprising a collection of 2,083,054 documents with the total of 3,129,334,419 words. Models' losses (logarithmically scaled) are presented below:


<img src="https://github.com/MageshDominator/bio-medical-ner-spacy-stanza/blob/master/med7-spacy/images/loss.png" width="350">

The model achieved a lenient (strict) micro-averaged F1 score of 0.957 (0.893) across all seven categories.

### Installation:
```
pip install -U spacy
```

Download models from above link or use this
`pip install https://med7.s3.eu-west-2.amazonaws.com/en_core_med7_lg.tar.gz`

### Usage

```python
import spacy

med7 = spacy.load("en_core_med7_lg")
# med7 = spacy.blank("en").from_disk("model_256_16_332.bin") # model downloaded from above link

# create distinct colours for labels
col_dict = {}
seven_colours = ['#e6194B', '#3cb44b', '#ffe119', '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']
for label, colour in zip(med7.pipe_labels['ner'], seven_colours):
    col_dict[label] = colour

options = {'ents': med7.pipe_labels['ner'], 'colors':col_dict}

text = 'A patient was prescribed Magnesium hydroxide 400mg/5ml suspension PO of total 30ml bid for the next 5 days.'
doc = med7(text)

spacy.displacy.render(doc, style='ent', jupyter=True, options=options)

[(ent.text, ent.label_) for ent in doc.ents]
```
The Med7 model identifies correctly all seven entities in the following example and highlights them in different colours for better visualisation:

![](https://github.com/MageshDominator/bio-medical-ner-spacy-stanza/blob/master/med7-spacy/images/displacy.png)


and the resulting output:

```
[('Magnesium hydroxide', 'DRUG'),
 ('400mg/5ml', 'STRENGTH'),
 ('suspension', 'FORM'),
 ('PO', 'ROUTE'),
 ('30ml', 'DOSAGE'),
 ('bid', 'FREQUENCY'),
 ('for the next 5 days', 'DURATION')]
```

## [med7Ner.py](https://github.com/MageshDominator/bio-medical-ner-spacy-stanza/blob/master/med7-spacy/med7Ner.py)
* It has s template file to run NER using med7 model in spacy
* It has entity linking template to link entities with drug
* Has code to render entity annotation with displacy

## Reference
```
@article{kormilitzin2020med7,
  title={Med7: a transferable clinical natural language processing model for electronic health records},
  author={Kormilitzin, Andrey and Vaci, Nemanja and Liu, Qiang and Nevado-Holgado, Alejo},
  journal={arXiv preprint arXiv:2003.01271},
  year={2020}
}
```
