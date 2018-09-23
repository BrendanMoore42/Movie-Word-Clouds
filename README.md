## Subtitle Word Clouds
Creates a Word Cloud from a Subtitle .srt file.

### Requirements & Packages
* Works in both OSX and Windows
* Python 3.6+
* Pandas, Numpy, WordCloud, Matplotlib
* Photoshop/Gimp (optional)

### Scope
Subtitle Cloud creates an image based off of word frequencies in the script. Subtitles are stored in .srt format, and contain a good approximation of overall dialogue. Srt files can be acquired from www.yifysubtitles.com/movie/. The script will output a .png of the word cloud based off of the jpg used and a cleaned .txt file of the dialogue without timestamps. 

### Example #1: The Dark Knight, 2008
![batman](https://i.imgur.com/z0hsXTa.jpg)

### Parameters
Clouds can be customized to add stopwords, change colors, apply contours, alter background colour, adjust figure size, change output filetypes and more. Some srt files will include auditory cues like 'laughing', or 'gasps', and can be removed by adding them to the example stopwords list in get_words() fn. Image masks to outline the clouds are best in JPEG format, larger than 1024x768, black and white. 

### Example #2: James Bond - Goldfinger, 1964
#### Set-up
(Optional) Create virtual environment and install dependencies using pip.

* Create or find black and white image to use as mask:
<img src="https://i.imgur.com/QmfXrCk.png" alt="Bond_pre" width="250">

* Download subtitles: www.yifysubtitles.com/movie/james-bond-goldfinger-1964
* Put both srt and jpg in same folder as txt_to_cloud.py.

#### Running the script
In terminal, go to target directory, activate VM or simply run:

    $ python txt_to_cloud.py goldfinger.srt jamesbond.jpg
    
If error, change encoding as last argument: 
    
    $ python txt_to_cloud.py goldfinger.srt jamesbond.jpg cp1252

#### Pre-Process:
<img src="https://i.imgur.com/iCtVxxp.png" alt="Bond_pre" width="500">

#### Post-Process:
Try playing around with settings to find the best fit for your image/script. Use photoshop to fine-tune details, add wrappers, and change colours.

### Goldfinger, 1964
<img src="https://i.imgur.com/Xg1iVVl.jpg" alt="Bond_pre" width="500">

### More Examples:

### Hamlet, 1990
<img src="https://i.imgur.com/AXf2Nem.jpg" alt="Hamlet" width="500">

### Beauty and the Beast, 2017
<img src="https://i.imgur.com/Dq5Cisa.jpg" alt="Beauty_and_beast" width="500">

Help and additional credit - @Nadimyounes & @ndunn219
