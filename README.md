# BibleLM



## training and make ziped model 
```python
!git clone https://github.com/leehosu01/BibleLM.git
!mv BibleLM/* ./

import setup
import training

training.training(clear_other_models = True, split_model = False, delete_model_if_split = True)

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

training.training(clear_other_models = True, split_model = False, delete_model_if_split = True)
#training.training(clear_other_models = True, split_model = True, delete_model_if_split = True)# both are possible

inference.inference("Look")
#['Look out, and let them fall down before us.',
# 'Look for the sword in the plains, and the spear at noon: for he hath no mercy on his own head.',
# 'Look upon thy way, O my God; and make thee the crown of my glory.',
# 'Look of my ways; and see, and behold the way which I have set before you:',
# 'Look for me at the brook, and tell me: for I am strong; go in, I will shew you.']
```

-------------------


## inference(or generate) 
```python
!git clone https://github.com/leehosu01/BibleLM.git
!mv BibleLM/* ./

import setup
import inference

inference.inference("Look")# split and non-split format both are supported. 
#['Look the earth, and see: the land is as a garment; the fruit thereof shall not rot.',
# 'Look out, and see what they shall do unto us; for if there be a time of temptation, I pray you come ye to the plain.',
# 'Look out, thou king of Israel: for I am against thee, saith the LORD.',
# 'Look, thou son of man: for thus saith the LORD; Thy years shall be in darkness and shadow until I have destroyed thy seed out from before thee.',
# 'Look, I speak unto you as a man that have sinned: but if ye forgive not your enemies their trespasses which they commit against them.']
```

<!--
```python
!rm -r *
!git clone https://github.com/leehosu01/BibleLM.git
#!curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
#!sudo apt-get install git-lfs
#!cd BibleLM && git lfs pull
!mv BibleLM/* ./


import setup
import training
training.training(clear_other_models = True, split_model = True, delete_model_if_split = True)


import inference
print(inference.inference("Look"))

!rm -r BibleLM
!git clone https://github.com/leehosu01/BibleLM.git
!cp training.py BibleLM/
!cp config.py BibleLM/
!cp inference.py BibleLM/

!git config --global user.email "leehosu01@naver.com"
!git config --global user.name "leehosu01"

!curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
!sudo apt-get install git-lfs
!cd BibleLM/ && git lfs untrack "*.bin"
!cd BibleLM && git add . && git commit -m "add model split after training option"
!cd BibleLM && cp -r ../models_ckpts ./
!cd BibleLM && git add . && git commit -m "split 된 모델추가, BS = 1, epochs = 2"
#!rm BibleLM/.gitattributes
!cd BibleLM && git add . && git commit -m "lfs 안쓰기 때문에 attr 제거"
```
-->
