## Subtitle Word Clouds
Creates a Word Cloud from a Subtitle .srt file.

### Requirements & Packages
* Works in both OSX and Windows
* Python 3.6+
* Pandas, Numpy, WordCloud, Matplotlib
* Familiarty with Photoshop/Gimp a strong 

### Scope
Text to Cloud converts a subtitle movie file to a word cloud. Subtitles are stored in .srt format, and contain a good approximation of the movie's script. Images must be in jpeg format, preferably black and white. Srt's can be acquired by searching https://www.yifysubtitles.com. The script will additionally output a cleaned .txt file of dialog without .srt timestamps into the same directory.

### Showcase #1: The Dark Knight, 2008
![batman](https://i.imgur.com/z0hsXTa.jpg)

### Use & Parameters
Clouds can be customized to add stopwords, change colors, apply contours, alter background colour, adjust figure size, change output filetypes and more. Some srt files will include auditory cues like 'laughing', or 'gasps', and can be removed by adding them to the example stopwords list in get_words() fn. Image masks to outline the clouds are best in JPEG format, larger than 1024x768, black and white. 

### Example: James Bond - Goldfinger, 1964
#### Set-up
(Optional) Create virtual environment and install dependencies using pip. Recommended. 
* Create or find black and white image to use as mask:
![bondmask](https://i.imgur.com/QmfXrCk.jpg =250x250)
* Download subtitles: www.yifysubtitles.com/movie/james-bond-goldfinger-1964
* Put both srt and jpg in same folder

#### Running the script
Run from command line, example: James Bond - Goldfinger

    $ python txt_to_cloud.py goldfinger.srt jamesbond.jpg
    
If error, change encoding as 4th argument: 
    
    $ python txt_to_cloud.py goldfinger.srt jamesbond.jpg cp1252

#### Pre-Process:
<img src="https://i.imgur.com/iCtVxxp.png" alt="Bond_pre" width="500" height="500">

#### Post-Process:
Try playing around with settings to find the best fit for your image/script. 

### Goldfinger, 1964
<img src="https://i.imgur.com/Xg1iVVl.jpg" alt="Bond_pre" width="500" height="500">

### Hamlet, 1990
<img src="https://i.imgur.com/AXf2Nem.jpg" alt="Hamlet" width="500" height="500">

### Beauty and the Beast, 2017
<img src="https://i.imgur.com/Dq5Cisa.jpg" alt="Beauty_and_beast" width="500">
