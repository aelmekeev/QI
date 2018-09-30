# QI Guest List

This project contains back-end and front-end code of the guest list of BBC's [Quite Interesting](http://www.bbc.co.uk/qi/).
With this tool you can:

* see list of participants of all QE tv episodes
* find out list of episodes where particular person was on the show including:
  * links to the recordings of the show &mdash; mostly from [VK group "Quite Interesting"](http://vk.com/quiteinteresting)) with Russian/English subtitles;
  * air date of each show (available in a tooltip);
  * is this person win the show or not.

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

Input data is `data.csv` from data directory. Output is `data.js` which will be added into data directory. Copy it to frontend part once you make sure that it's in a good state.

Note: `generate_data.py` uses `vk_api` library. Use below command to install it:

```
pip install vk_api
```

### Front-end

The result is deployed on: [https://qi-guest-list.herokuapp.com/](https://qi-guest-list.herokuapp.com/).