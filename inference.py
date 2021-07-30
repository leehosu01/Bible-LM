
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:18:30 2021

@author: map
"""
from config import *

def inference(sentence):
    import transformers

    model = transformers.TFGPT2LMHeadModel.from_pretrained(models_path, from_pt=True)
    tokenizer = transformers.GPT2Tokenizer.from_pretrained("gpt2")

    input_ids = tokenizer.encode(sentence, return_tensors='tf')

    generated_text_samples = model.generate(
        input_ids, 
        max_length=max_length,  
        num_return_sequences=5,
        no_repeat_ngram_size=2,
        repetition_penalty=1.5,
        top_p=0.925,
        temperature=.85,
        do_sample=True,
        top_k=125,
        early_stopping=True
    )

    #Print output for each sequence generated above
    for i, beam_case in enumerate(generated_text_samples):
      print("{}: {}".format(i,tokenizer.decode(beam_case, skip_special_tokens=True)))
      #print("{}: {}".format(i,tokenizer.decode(beam_case, True, True,)))
      #print("{}: {}".format(i,tokenizer.decode(beam_case, False, True)))
      #print("{}: {}".format(i,tokenizer.decode(beam_case, True, False)))
      #print("{}: {}".format(i,tokenizer.decode(beam_case, False, False)))
      print("")
#inference("And ")