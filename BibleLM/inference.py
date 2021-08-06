
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:18:30 2021

@author: map
"""
from BibleLM.config import *
import transformers

tokenizer = transformers.GPT2Tokenizer.from_pretrained("gpt2")
def inference(sentence, return_case = 5, model_path = models_path):

    try: model = transformers.GPT2LMHeadModel.from_pretrained(model_path)
    except:
        try:
            simple_cmd_command(f"cat {model_path}/pytorch_model.bin.split_* > {model_path}/pytorch_model.bin")
            model = transformers.GPT2LMHeadModel.from_pretrained(model_path)
        except Exception as e:
            raise RuntimeError(str(e))
            #raise RuntimeError(f'Fail to open model. Check {model_path}/ is correctly exist.')

    input_ids = tokenizer.encode('<|endoftext|>' + sentence, return_tensors='pt')

    generated_text_samples = model.generate(
        input_ids, 
        max_length=max_length,  
        num_return_sequences=return_case,
        no_repeat_ngram_size=2,
        repetition_penalty=1.5,
        top_p=0.925,
        temperature=.85,
        do_sample=True,
        top_k=125,
        early_stopping=True
    )
    return [tokenizer.decode(beam_case, skip_special_tokens=True) for beam_case in generated_text_samples]
    #Print output for each sequence generated above
    for i, beam_case in enumerate(generated_text_samples):
      print("{}: {}".format(i,tokenizer.decode(beam_case, skip_special_tokens=True)))
      #print("{}: {}".format(i,tokenizer.decode(beam_case, True, True,)))
      #print("{}: {}".format(i,tokenizer.decode(beam_case, False, True)))
      #print("{}: {}".format(i,tokenizer.decode(beam_case, True, False)))
      #print("{}: {}".format(i,tokenizer.decode(beam_case, False, False)))
      print("")
#inference("And ")
