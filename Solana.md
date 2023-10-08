## Solana
I chose to analyze scam-related activities associated with Solana due to its growing prominence and widespread adoption within the cryptocurrency ecosystem. As one of the fastest and most scalable blockchains, Solana has garnered significant attention from investors, developers, and the crypto community at large. This increased visibility has made Solana a potential target for fraudulent schemes, Ponzi schemes, and other malicious activities. 

#### Entity type: Blockchain

#### Associated scams

###### 2022-08-04

_Hackers attacked the Solana crypto ecosystem with a previously unknown exploit and compromised over 8,000 wallets, at least so far. Most of the victims seem to be mobile wallet users. Solana is a blockchain that supports builders creating crypto apps and has SOL as its cryptocurrency. OtterSec, a company specialized in blockchain audits, initially posted on Twitter that over 5,000 wallets had been drained in just a few hours, but that number has changed since. They also added that their owners signed the transactions, suggesting that the victims' private keys had been compromised somehow._ 
_Some of the victims include Phantom, Slope and TrustWallet. Several Solana accounts have amassed more than $5 million worth of various tokens, but the system already flagged them as part of a possible hack._
_Solana deals with hot wallets, which are always connected online, allowing their owners to make or receive payments quickly. Unfortunately, this also raises some security issues. It's unclear how the hack took place, how many people were affected, and whether the victims could retrieve the money._

###### 2022-10-13

_Solana network suffers another $100M scam at Mango Markets. A decentralized blockchain Solana has suffered several exploits over two months. While the rest of the market was busy trading digital assets, the Solana network was experiencing a scam through its Phantom wallet._
_As per reports, the hacker initially funded one 5mm USDC for assurance around 6:19 PM ET. After that, he offered 483 million MNGO units in the Mango Markets. After this, the offender funded a different account with 5M USDC collateral around 6:24 PM ET to purchase the same 483 million MNGO perpetual contracts worth $0.03._
_Around about 6.26 PM ET, the attacker began to manipulate the Mango spot market price, making it $0.91 and the 483 million MNGO’s worth $423 M. A credit amount of $116 million was immediately received by the scammer, leaving Mango’s fund with a balance of -116.7 million, which drained the liquidity._


## Approach
Using a Python script, I collected a total 1266 articles from Google News that mention Solana either in its title or text for the period from September 1st to October 3rd 20223. Then using data manupulation techniques, I marked every article to be scam-related or not. An article is classified as a scam-related if it contains any of the following words:
```scam_keywords = ["scam", "fraud", "bankman-fried", "cyberattack", "attack", "unauthorized", "phishing", "hacker", "fraudulent", "ponzi", "deception", "swindle", "hoax", "con", "challenges", "death", "lawsuit", "dangerous", "uncertainty",  "freeze", "controversial", "risk", "exploit", "compromise", "victim", "fake"]```


## Graphs

#### Bar-chart showing the number of Scam-related mentions relative to General mentions of Solana in Google News articles for the period from September 1st to October 3rd. Total number of articles - 1266
![Staked Bar-chart](https://github.com/alibek-git/crypto-scams-challenge/blob/main/media/solana-mentions-graph.png)

#### Pie-Chart below illustrates that with regards to Solana, 4.4%, or 56 out of 1266 articles, can be classified as scam-related.
![Pie-chart](https://github.com/alibek-git/crypto-scams-challenge/blob/main/media/solana-mentions-pie-chart.png)

#### Word-cloud to visually represent the most frequently occurring words or phrases in the titles of 1266 articles.
![Word Cloud](https://github.com/alibek-git/crypto-scams-challenge/blob/main/media/solana-mentions-word-cloud.png)
