# Generative Art

## Abstract

This repo is a collection of Generative Art scripts.

## Simplex Noise ([Code](/Noise))

[Open Simplex noise](https://github.com/lmas/opensimplex) provides random, but smooth noise in up to 4 dimensions. We can create perfectly looping randomness without directional artifacts (appearance of stopping and reversing) by traversing a 4D hyper-circle.

![SimplexArrows](/Noise/Show/arrows2D.gif)

![SimplexLavaLamp](/Noise/Show/lamp.gif)

High resolution sampling is powered by [this](https://github.com/ktritz/opensimplex) optimized version using jit compilation via [Numba](https://numba.pydata.org/).

## Circle Packing ([Code](/CirclePacking/pack.py))

To densely pack circles, this algorithm stores a grid of points. At each point a the minimum distance to another circle is stored. When plotting a circle, the canvas grid is updated at each point that is closer to the current circle than what is already stored at that point.

After some random seed iterations, other circles are added the maximum distance stored in the canvas grid with the maximum allotted radius.

![Circle Packing](/CirclePacking/Show/pack.png)

## Pixel Sorting ([Code](/PixelSorting/pixelSort.py))

Randomly select a 'seed' pixel on each row. Increase the sorting range to the left and right so long as the left and right pixels are within a prescribed tolerance of the seed pixel, then sort the selection.

![Pixel Sorting Gif](/PixelSorting/Show/SelectSort.png)

## Pixel Clustering ([Code](/PixelClustering/cluster.py))

This method is inspired by Sherrie Levine's piece titled [Meltdown](https://www.moma.org/collection/works/65711).

Randomly select 12 'palette' pixels from an image. Select another larger set of 'training' pixels. Match each pixel in the training set with a pixel in the palette by closest Manhattan distance. Nudge the palette pixel a small step towards each paired pixel.

![Pixel Clustering Image](/PixelClustering/Show/PixelClustering.png)

The maximum pair distance converges when this process is repeated over many iterations.

![Cluster Convergence](/PixelClustering/Show/ClusterConvergence.png)

After some more learning, [K means clustering](https://en.wikipedia.org/wiki/K-means_clustering) is a faster alternative to this method. Instead of nudging each point a small distance, just set each point to the mean of all matching points. It converges much faster.

## Recursively Generated Tree ([Code](RecursiveTree/RecursiveTree.py))

![Recursive Tree](/RecursiveTree/Show/RecursiveTree.gif)
