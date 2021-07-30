# BibleLM



## training and make ziped model 
```python
!git clone https://github.com/leehosu01/BibleLM.git
!mv BibleLM/* ./

import setup
import training

training.training()

import config
!zip -r -1 {config.models_path}.zip {config.models_path}/
```

-------------------


## training and inference(or generate) 
```python
!git clone https://github.com/leehosu01/BibleLM.git
!mv BibleLM/* ./

import setup
import training, inference

training.training()

inference.inference("Look")
#['Look on the right hand of his own right hands, and ye shall be saved; I will not fall upon them:',
# 'Look for the LORD: look up unto him, that he may prosper: and I will deliver thee.',
# 'Look as an upright heart, and will not sin: but the wickedness of his mouth shall he deliver.',
# 'Look, they have taken our counsel before the LORD to set up an ambush for us.',
# 'Look, I will not cause any man to die in this city; but he shall live for ever.']
```
