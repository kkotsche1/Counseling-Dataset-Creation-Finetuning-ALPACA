# Counseling-Transcript-Dataset-Creation-LLaMA
Scraping and data processing creating a dataset of approximately 25k client/therapist interaction turns for training of LLaMA and derivative models

Training code is included in Model_Training.ipynb and was run in Google Colab using a regular GPU and extended system RAM. This was sufficient for the 7B parameter model. Trianing of a 13B model would require premium GPUs with associated higher costs. 

In order to use this code you need to download the AnnoMI dataset which can be found at: https://github.com/uccollab/AnnoMI

#How to Use

The dataset used for training is included in the github repository at /json_files/global_therapy_list.json
The model can be trained from the Model_Training.ipynb file. In order to train adjust the filepaths within
the notebook to point to the included training dataset. 

#Disclaimer

This code and the model created through it are intended for research purposes only. As this is a LORA finetuning of Stanford's ALPACA model that uses Meta LLaMA weights and OpenAI generated data for finetuning this is not intended for commercial purposes. Any and all use should only be for research or personal entertainment purposes. 
