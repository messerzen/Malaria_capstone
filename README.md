# CNN model for cell images classification

This is the capstone project of "Nanodegree Machine Learning Engineer" course from Udacity. 
The model classification  task is to detect if a cell is infected with malaria parasite or is uninfected based on image attributes.
In this project three CNN models are compared and their performance are compared:
- Model_1: CNN model created from scratch
- Model_2: Model_1 update with more layers and adjusted parameters.
- Pre-trained: model using VGG16 pre-trained model.

The best performance was achieved by model_2.

## Getting started

This project was developed using Google Colaboratory because it allows you to use a GPU for free. 
You are encourage to use google colaboratory in order to reduce time consuming to preprocess data, build and training the model.

### Instructions

There are two options to upload the '*.tar.xz" dataset files in Google Colaboratory Notebook:
- Upload button: 

<img src='https://forums.fast.ai/uploads/default/original/2X/9/9cfacd52a41fac4c9bcf533c6b4e76237caa9e4d.png'/>

- Using Pydrive module - In this case you have to perform the following steps:

1. install pydrive module in google colaboratory notebook using:

`! pip install pydrive`

2. Upload all tar.xz files in a google drive account.

3. Authenticate and create the PyDrive client.

`auth.authenticate_user()`

`gauth = GoogleAuth()`

`gauth.credentials = GoogleCredentials.get_application_default()`

`drive = GoogleDrive(gauth)`


4. Import necessary modules

`import os`

`from pydrive.auth import GoogleAuth`

`from pydrive.drive import GoogleDrive`

`from google.colab import auth`

`from oauth2client.client import GoogleCredentials`

When prompted, click on the link to get authentication to allow Google to access your Drive account. 
You should see a screen with “Google Cloud SDK wants to access your Google Account” at the top. 
After you allow permission, copy the given verification code and paste it in the box in Colab. [Info source](https://towardsdatascience.com/3-ways-to-load-csv-files-into-colab-7c14fcbdcb92)

5. Download the files from google drive

To get the file ID use the sharable link file, e.g.:
`https://drive.google.com/open?id=14DiZ1ZbsfbZaDFqwDDJWKFcb1M0wXvIW`

Copy and paste the file ID in 'id' key

`download = drive.CreateFile({'id': '14DiZ1ZbsfbZaDFqwDDJWKFcb1M0wXvIW'})'`

`download.GetContentFile('test.tar') # Download the file and save with the specific name 'test.tar`
 
 You should create an CreateFile object for each validation, training and test file.

6. Upload & extract .tar files.

`upload = drive.CreateFile({'title': 'test.tar'}) # Title is the same name chosen in GetContentFile object`
`upload.SetContentFile('test.tar')`
`upload.Upload()`

`! mkdir -p content/cell_images # Create a directory to extract the dataset`

Feel free to change the directory name

7. Extract content

`!tar -xvf  test.tar -C content/cell_images`

## Useful links:
[Colab upload tutorial](https://colab.research.google.com/notebooks/io.ipynb#scrollTo=zU5b6dlRwUQk)

[Article 1](https://towardsdatascience.com/3-ways-to-load-csv-files-into-colab-7c14fcbdcb92)

[Forum discussion](https://forums.fast.ai/t/platform-colab/28161/21)

## Author

- **Paulo Henrique Zen Messershmidt** - [LinkedIn](https://www.linkedin.com/in/paulo-henrique-zen-messerschmidt-35581661/)

email: phzm.engmec@gmail.com

## Built with
- [Keras Librabry](https://keras.io/)
- [Google Colaboratory](https://colab.research.google.com) - Virutal Enviroment

## Acknowledgments
-  [U.S. National Library of Medicine (NIH)](https://www.nlm.nih.gov/) for sharing this dataset.

