# pychart.py

![](https://i.imgur.com/t34nH8d.png)

A simple bar graph generator that I've made specifically to prove that YouTube commenter was correct, and that a whole bunch of people in the replies are absolutely factually wrong and/or dumb. I obtained the data to support this objectively based and true opinion from the [TechPowerUp GPU Spec Database](https://www.techpowerup.com/gpu-specs/?mfgr=NVIDIA&mobile=No&workstation=No&igp=No&sort=released "TechPowerUp GPU Spec Database"), filtering for Nvidia GPUs, then using the filter text "TX 70" to see only the 70 Series cards. The 70 series was chosen because they're generally seen to be the high-mid range of GPUs, and because fuck you that's why. This gave me this rough data, which I then added price data to. Source: the internet.
<br>


### The Data
| **Product Name**                                                                       | **Released**   | **Memory**              |
| -------------------------------------------------------------------------------------- | -------------- | ----------------------- |
| [GeForce GTX 470](https://www.techpowerup.com/gpu-specs/geforce-gtx-470.c267)          | Mar 26th, 2010 | 1280 MB, GDDR5, 320 bit |
| [GeForce GTX 570](https://www.techpowerup.com/gpu-specs/geforce-gtx-570.c269)          | Dec 7th, 2010  | 1280 MB, GDDR5, 320 bit |
| [GeForce GTX 670](https://www.techpowerup.com/gpu-specs/geforce-gtx-670.c362)          | May 10th, 2012 | 2 GB, GDDR5, 256 bit    |
| [GeForce GTX 770](https://www.techpowerup.com/gpu-specs/geforce-gtx-770.c1856)         | May 30th, 2013 | 2 GB, GDDR5, 256 bit    |
| [GeForce GTX 770M](https://www.techpowerup.com/gpu-specs/geforce-gtx-770m.c2129)       | May 30th, 2013 | 3 GB, GDDR5, 192 bit    |
| [GeForce GTX 870M](https://www.techpowerup.com/gpu-specs/geforce-gtx-870m.c2535)       | Mar 12th, 2014 | 3 GB, GDDR5, 192 bit    |
| [GeForce GTX 970](https://www.techpowerup.com/gpu-specs/geforce-gtx-970.c2620)         | Sep 19th, 2014 | 4 GB, GDDR5, 256 bit    |
| [GeForce GTX 1070](https://www.techpowerup.com/gpu-specs/geforce-gtx-1070.c2840)       | Jun 10th, 2016 | 8 GB, GDDR5, 256 bit    |
| [GeForce GTX 1070 Ti](https://www.techpowerup.com/gpu-specs/geforce-gtx-1070-ti.c3010) | Nov 2nd, 2017  | 8 GB, GDDR5, 256 bit    |
| [GeForce RTX 2070](https://www.techpowerup.com/gpu-specs/geforce-rtx-2070.c3252)       | Oct 17th, 2018 | 8 GB, GDDR6, 256 bit    |
| [GeForce RTX 3070](https://www.techpowerup.com/gpu-specs/geforce-rtx-3070.c3674)       | Sep 1st, 2020  | 8 GB, GDDR6, 256 bit    |
| [GeForce RTX 3070 Ti](https://www.techpowerup.com/gpu-specs/geforce-rtx-3070-ti.c3675) | May 31st, 2021 | 8 GB, GDDR6X, 256 bit   |
| [GeForce RTX 4070](https://www.techpowerup.com/gpu-specs/geforce-rtx-4070.c3924)       | Apr 13th, 2023 | 12 GB, GDDR6X, 192 bit  |

------------

<br>
### Results
<p>
> 'A really stupid opinion'
> Most of those replies (2023, Colourised)


![](https://i.imgur.com/mkseWtb.png)

From 2010’s GTX 470 to 2016’s GTX 1070 we went from 1.2GB to 8GB of VRAM. From 2016’s GTX 1070 to 2023’s RTX 4070 we went from 8GB to 12GB of VRAM. 

So let’s compare how much VRAM allocations changed over the last 7 Years, compared to the 6 Years before that. 

2016-2023: 150%
2010-2016: 666%

Yikes. 

What about the price over that same period?

2016-2023: 158%
2010-2016: 115%

I'm not happy with how clear the chart generated is at accurately displaying the correct level of disdain I feel for people who think the opposite is true, nor does it show the increase over time - this is my first time with the TK library so I'm proof of concepting the entire thing first, making it pretty second. 
