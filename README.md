# She Plus Plus London 2017

Our team project for the mentored hack.

## Hackathon Team Name Generator

Here’s a link to our [twitter bot](https://twitter.com/ShePlusPlusTeam)

### Why?

We had trouble picking a team name, so we decided to build a twitter to to do it for us. Simple!

### What?

We picked the structure we wanted for our team names - settling on a three part format:  
a positive adjective + a noun related to programming or computers + a collective noun for the teams or groups. 

```
Magnificent Python League
Courageous Fragmentation Wizards
Whimsical Algorithm Guild
Legendary Emoji Posse
Dazzling Hexadecimal Heroes
```


Next, came planning the text for our tweets that we would be able to drop the random words into. We wanted our bot to be able to write two kinds of tweets. Firstly, in response to people who tweet it asking for a team name:

```
“You should call your team Determined Cache Bunch @example”
```
We also wanted it to be able to tweet out semi-regularly on its own:

```
“Adventurous Algorithm Gang! Much creative. Such wow.”
“New team name: Co-operative Bandwidth Alliance”
```
… 

### How?
First, we saved the adjectives, computer nouns and team nouns as separate files, and wrote a method that would shuffle each of these lists individually and return a random word. We also wrote a method called 'normalise' that would guarantee that the first letter of each returned word would be upper case.

Then, we added a ##timer to our script that would tweet the sequence, so a suggestion would be posted every 10 minutes. 
We also built a ##listener program for the @ reply function. 

## Built With

* Python2.7
* Twitter API

## Authors

* **Alex Millward** - *mentor*
* **Gabriella Gal**
* **Em Donnelly**

## Acknowledgments


* **She Codes London** - *all the organisers who made it happen* - [She Plus Plus](http://www.sheplusplus.london/)
* **Monzo** - *our wonderful hosts* - [Monzo](https://monzo.com/about/)
