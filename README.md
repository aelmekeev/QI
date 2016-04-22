# QI Guest List

This project contains back-end and front-end code of the guest list of BBC's [Quite Interesting](http://www.bbc.co.uk/qi/).
With this tool you can:

* see list of participants of all QE tv episodes
* find out list of episodes where particular person was on the show including:
  * links to the recordings of the show &mdash; mostly from [VK group "Quite Interesting"](http://vk.com/quiteinteresting)) with Russian subtitles, but also with English subtitles
  * air date of each show is available in a popup

## Usage

There are two parts of this project: back-end and front-end. Back-end is written on Python and front-end is on Javascript. Also there is an `data.csv` file which was created based on information from [Wikipedia](https://en.wikipedia.org/wiki/QI).

### Back-end

Initial set of data is located [here](https://docs.google.com/spreadsheets/d/1FOJ0BsKj5z2ksIugG7oRY_dtE3SM-gZakIGuXTSS2tg/edit?usp=sharing) and was created manually. `data.csv` was exported from this spreadsheet.

The purpose of back-end script `generate_data.py`:

* parse and do basic validation of input csv file
* generate `data.js` file which will be used by front-end part.

In order to do this you just need to simply run backend script like this:

```
python generate_data.py
```

Input data is `data.csv` from data directory. Output is `data.js` which will be added into data directory.

### Front-end

Since for visualization was used [JSFiddle](https://jsfiddle.net/) front-end part consists of html, css and js files that you can just copy-paste to your fiddle. Besides this code you will also need to:

1. enable in JSFiddle interface:
   1. JQuery Framework (2.1.4);
   2. enable JQuery UI library (1.11.4);
2. include as external resource:
   1. `data.js` which you can found in data directory of this project after compliting of back-end process.