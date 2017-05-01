
# Polish Case Trainer

This is a simple CLI program to allow a learner of the Polish Language to practice case declension. Those people who have attempted to learn Polish as a non-native speaker will be aware just how complex the case system is.

The premise is that the brain is better at learning via repeated guessing and correction. I was inspired by the way in which Chicken Sexing is taught, as described by [this article](http://www.businessinsider.com/the-incredible-intuition-of-professional-chicken-sexers-2012-3).

The traditional way of learning these things (memorising a table of endings, and stem-modification rules) leads to fractured speech as the brain has to pause talking while it applies the rules. The trial and correction approach forces the brain to learn the skill unconsciously and intuitively, much like a native speaker's innate knowledge of the language. The goal is to teach you the patterns that govern what a given case-form for is for an arbitrary word. This program is *not* about teaching vocabulary.

## Installation Instructions:

Firstly, clone this repository:

```bash
git clone https://github.com/tombusby/PolishCaseTrainer
```

Then navigate into the `PolishCaseTrainer` directory (`cd PolishCaseTrainer`).

You may want to install this program in a virtual environment rather than to your system Python installation. If so you should initialise that and active it now.

Install the dependencies as follows (pip will require root if installing to system Python env):

```bash
pip install -r requirements.txt
```

After this, we simply need to use Python's setup.py features to install the module (again will require root if not in virtualenv):

```bash
python setup.py install
```

If you want to develop this app, instead install with:

```bash
python setup.py develop
```

Once this is completed you'll have access to the `polish_case_trainer` script that can be run from the command line at any time. It will be on the PATH so you don't need to be in a specific directory to run it.

## Usage Instructions:

You'll be presented with a random noun (and its gender) plus a random adjective. Translation is not provided. You are then presented with a case and grammatical number (e.g. Plural Genitive) and prompted to provide the correct declined forms.

If you succeed you are congratulated, if you fail you are given the correct answer. The program then moves on to another random adjective/noun pair and requests another case.

It's best to accept that you will get most of them wrong to begin with. Keep playing and your rate of correct choices will increase. When you're getting a near-100% correct response rate, you have successfully internalised the root-change and ending-change patterns.

## Sample Output:

![Sample output](https://raw.githubusercontent.com/tombusby/PolishCaseTrainer/master/readme-files/terminal.png)

## To Do:

* Prevent "Singular Nominative" from being requested
* Create game mode that allows for practising irregular, common-word case forms such as pronouns
* Create a mode for practising verb endings
* Create a mode which is the reverse of the existing one: Provides the noun (+ gender) and a declined adjective/noun form. It then requests that you specify what case it is.

## Misc

If you're interested in how I acquired the list of correct noun/adjective forms, this python scrapy repository might be interesting to you:

[https://github.com/tombusby/polish-case-scraping](https://github.com/tombusby/polish-case-scraping)
