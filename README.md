# BERT are you sensible? Evaluating common-sense reasoning in pre-trained language models
This repository contains the dataset and all code related to the MSc project.

- The preprocess.py script reads in the original dataset, applies the steps detailed in the report, and outputs the processed dataset.
- The taska-finetune-notebook fine-tunes the bert base model on subtask A.
- The taskb-finetune-notebook fine-tunes the bert base model on subtask B.
- The taska-evaluate-notebook loads the fine-tuned model for subtask A from hugging face and reproduces the results mentioned in the report.
- The taskb-evaluate-notebook loads the fine-tuned model for subtask B from hugging face and reproduces the results mentioned in the report.


The finetuned models for both subtask A and subtask B are available publicly at the Hugging Face model hub and the results can easily be reproduced using them.
https://huggingface.co/JazibEijaz/bert-base-uncased-finetuned-semeval2020-task4a
https://huggingface.co/JazibEijaz/bert-base-uncased-finetuned-semeval2020-task4b
