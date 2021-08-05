# BibleLM


-------------------


## inference(or generate) 
```python
!pip install git+https://github.com/leehosu01/BibleLM.git
from BibleLM import inference

inference('<|endoftext|>Lookup', 5) # model file split and non-split format both are supported. 
#["Lookup to the LORD, and behold his glory: arise from thy slumber; he shall be exalted. Selah Balaam is the saviour of Israel by God's hand unto the destruction that is before him for evermore in all places where they have forsaken thee this day because of their transgressions: who hath cut off a people out thereof? yea even Jacob alone, saith David my servant! go down to her also, I pray you with tears. So said Je",
# 'Lookup, O LORD; lift up thine eyes upon my soul. And the LORD lifted him up with his hand over their heads above all that they saw by night: and he looked on them in those days. Now therefore now what shall I do? shall this man also go away from me? so will it be well for thee, if thou wilt make thy servant a king to stand before Israel. If I have sinned against God through ignorance of these things not doing, then',
# "Lookup to heaven and unto the Lamb: for he shall come down from heaven with great power; yea, even with a shout of fire: then shall all those who are in darkness know that I am God. And again another saying is found concerning him (as also was prophesied by Jeremiah according as it were at the first): For if we say this thing secretly against our will without any conscience toward any man's life whatsoever before God or man himself aforetime being fulfilled, why should not",
# 'Lookup, O LORD: for thou knowest what shall come upon thee. Therefore take thy vengeance upon them that oppress me; and purge the evil from among you all by death on every side of Jerusalem round about this city into Edom to be a snare unto you, saith our God Almighty in his wondrous power concerning Jerusalem throughout your generations until the very end thereof? If ye abide in the land which I sware toward Abraham my father, then will I declare it before thee',
# 'Lookup, and see what thou hast done; for I know that thou art the LORD. And he said unto me again after this manner: Sit down, go in to thine husband also of whom we have spoken above concerning thee by us both now with all authority from heaven toward him (and thus it is written) God hath sent me two new moons upon thy head like a crown thereof.) So the people kept silence. Then was there no more war between Israelite kings any longer among']
```

-------------------

## training model 
```python

!pip install git+https://github.com/leehosu01/BibleLM.git
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

