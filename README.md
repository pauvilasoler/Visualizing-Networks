# Visualizing-Networks

Just some code for visualizing (multilayered) networks. 

Before delving into it, be aware of some things: 

- The code is really not tidy as I wasn't expecting anyone to take a look at it and so I just made something that was quick xD. To really make it tidy, it should be set up as a function (e.g. def make_plot() or whatever) and then call it with whichever dataset (i.e. "network") you want to make the plot but I was just too lazy and decided to copy paste for each plot hahaha. I will hopefully work on making it more tidy once I have time as I realize we might be needing to make more plots down the line and so more people might be needing this code.

- You will see that it requires some csv files that contain the respective networks. Imporantly, these csv files are adjacency lists that have been cleaned before hand in a separate R-file (dropping non-respondents, etc.). Unfortunately though, I am pretty sure I lost this R-file as I made it very quick and I can't find it anywhere so i'm guessing I didn't actually save it which means that, for now, plots can only be made with the csv files (i.e. "networks") that are saved in the datasets here in this repo. I will also try to remake this "data-processing" code whenever I have time so that we can do it for every other item as well. (If someone feelse like it, you can also do it as it is relatively straighforward)

- The multilayered plots are set up so that the nodes that got more nominations from the non-friendship item are bigger and the ones that got less are smaller. 

- Feel free to play with the visualizations and make them cooler! (It is relatively straightforward to play with them, you can check matplotlib's color list if you want to change colors for example) :) For instance, I didn't figure out how to increase the distance between the bigger nodes and the edges connecting to them with NetworkX and I didn't have time to delve deeper to figure it out xD. That's why sometimes the bigger nodes are touching the edges.

- If you don't understand something or you are having trouble running the code please tell me and I'll help.

- You will see that if you use a "Spring-layout" as it is currently the default the plot setup (i.e. position) will change every time you run the code but if you uncomment the "kamada_kawai_layout" and use that one istead the position will stay the same.
