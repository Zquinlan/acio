---
layout: single

header:
  overlay_color: "#5e616c"
  overlay_image: /assets/images/tutorial.jpg
excerpt: >
  AcIo BETA tutorial <br /><br /><br /><br />

classes: wide 
sidebar:
  nav: "content" 

---
If you would like to help beta test AcIo, please email [Zach](mailto:zquinlan@gmail.com) to recieve the application executables. 
<br /><br />
If you are running AcIo on windows you will have to download [Git for windows](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) if you have not previously done so. You will also have to setup your login credentials differently from the below instructions for osxkeychain. 

## Tutorial:
### Before starting verify that you have a Readme already in your repository. This will be used to build your landing page with AcIO. In future updates you will have the option to not use a readme if you prefer.

- Open Terminal (or Command Line if using Windows)
- Change directory to your local repository

```bash
cd ~/path/to/your/repository
```

- Verify git is installed. If it is not you can follow the instructins from [Github](https://docs.github.com/en/github/getting-started-with-github/caching-your-github-credentials-in-git) directly.
- Once you have verified that you have git installed and setup the osxkeychain make a new gh-pages branch in your repository.

```bash
git checkout -B gh-pages
```
- Now we can swtich over to AcIo (but do NOT close the terminal instance)! Right click Acio_gui.app and select open. A pop-up will tell you it is from an unknown source; click open.
- Fill in your Website title and name
- Click select directory and find the local repository which you want to make the website from.
- Select Minimal as the theme (more options will be avialable soon) and select a skin color theme for the minimal-mistakes jekyll theme.
- Paste your DOI into the box

### Recommended additions:
- Add photos: 
*Logo* will be the upper left portion next to the title of your website.
*Author* Picture of you!
*Splash image* This is the image which will be the main image going across the landing page
*photo album* An album of photos which you want to be displayed from your research!

<br />
- Social Media:
Add whatever social media handles you want to be included with the website

<br /><br />
### Click Acio Website to build the framework of your website! 
This could take a bit depending on internet speed but usually will not take longer than 1 minute. Once it completes another window will pop up and say "Framework Created!"

- Back in your old terminal window commit the changes and push to github.
```bash
git add -A
git commit -a -m 'AcIo Website frameork created'
git push
```
- Go to your github repository on your web browser and now on the right side of the screen you should see "Github-pages" under the environments side view. You can click that and then click "view deployment" on the following page! 

