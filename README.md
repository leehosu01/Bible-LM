# BibleLM


-------------------


## inference(or generate) 
```python
!pip install git+https://github.com/leehosu01/BibleLM.git
from BibleLM import inference

inference.inference("Look")# split and non-split format both are supported. 
#['Look the earth, and see: the land is as a garment; the fruit thereof shall not rot.',
# 'Look out, and see what they shall do unto us; for if there be a time of temptation, I pray you come ye to the plain.',
# 'Look out, thou king of Israel: for I am against thee, saith the LORD.',
# 'Look, thou son of man: for thus saith the LORD; Thy years shall be in darkness and shadow until I have destroyed thy seed out from before thee.',
# 'Look, I speak unto you as a man that have sinned: but if ye forgive not your enemies their trespasses which they commit against them.']
```

-------------------

## training model 
```python

from BibleLM.config import *
!git clone https://github.com/huggingface/transformers
!cd transformers && git checkout tags/v4.9.1
!pip3 install -r transformers/examples/pytorch/_tests_requirements.txt
from BibleLM import training, inference

!mkdir trained_model
training.training(clear_other_models = True, split_model = True, delete_model_if_split = True, model_path = 'trained_model')
inference.inference('Look', model_path = 'trained_model')
#['Look at my mouth; it is as the voice of a dove.',
# 'Looketh upon all his way to seek after the LORD, and will not turn aside from following him.',
# 'Look, I will write for thee these words, which thou shalt speak: The LORD hath given it to thy servants and thine own handmaid; ye shall not be ashamed of it.',
# 'Look for a good land to dwell in; and let my people dwell therein:',
# 'Look to the end, and there is not life.']
```

