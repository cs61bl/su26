---
layout: page
title: "Common Bugs"
nav_order: 6
parent: >-
  Project 3
# grand_parent: Projects
has_children: false
has_toc: false
has_right_toc: true
description: >-
  Project 5 Common Bugs.
released: true
---

## Deadlines

{% capture deadlines %}{% include proj3-deadlines.html %}{% endcapture %}
{{ deadlines | markdownify }}

## Common Bugs

### Overriding Equals

**The Problem**: Two instances of my class are saying they are not equal when they should be. Also, I set the instance of my class to be the key in a HashMap, but I can't find it when I try to access that key.

**The Solution**: Make sure that if you create any classes, override the `.equals()` method AND the `.hashcode()` method. This will guarantee that two instances that are equal will have the same hashcode


## Common UI Bugs

### Invisible Text

Getting text to show up on screen can be somewhat tricky. Several things need to
go right:
- the font color needs to be set to something visible (i.e. white)
- the location of the text needs to be in bounds
- you need to call `StdDraw.show()` after the text is drawn so it shows up
  on screen
- you need to make sure that your text does not get drawn over or cleared right
  after it is drawn (for example, `TERenderer.renderTiles` clears the entire
  screen)

Here's some code that should correctly draw text:
```java
TERenderer ter = new TERenderer();
ter.initialize(80, 40, 0, 0);
StdDraw.setPenColor(Color.WHITE);
StdDraw.text(40, 30, "I like cheese");
StdDraw.show();
```


### Strange Tiles

**The Problem:**

One common glitch is that after implementing other parts of the UI, the tile
characters will suddenly misbehave. Here's a program that demonstrates the problem.

```java
package core;

import edu.princeton.cs.algs4.StdDraw;
import tileengine.TERenderer;
import tileengine.TETile;
import tileengine.Tileset;

import java.awt.*;
import java.util.Arrays;

public class FlowerWorld {
    public static final int WORLD_WIDTH = 80;
    public static final int WORLD_HEIGHT = 40;

    public static void main(String[] args) {
        // create renderer
        TERenderer ter = new TERenderer();
        ter.initialize(WORLD_WIDTH, WORLD_HEIGHT, 0, 0);

        // draw main menu
        StdDraw.setFont(new Font("Monaco", Font.BOLD, 50));
        StdDraw.setPenColor(Color.WHITE);
        StdDraw.text(WORLD_WIDTH * 0.5, WORLD_HEIGHT * 0.75, "Press any key to continue");
        StdDraw.show();
        while (!StdDraw.hasNextKeyTyped()) {
            StdDraw.pause(10);
        }

        // create flower world
        TETile[][] tiles = new TETile[WORLD_WIDTH][WORLD_HEIGHT];
        for (TETile[] ar : tiles) {
            Arrays.fill(ar, Tileset.NOTHING);
        }
        for (int x = WORLD_WIDTH / 4; x < WORLD_WIDTH * 3 / 4; x++) {
            for (int y = WORLD_HEIGHT / 4; y < WORLD_HEIGHT * 3 / 4; y++) {
                tiles[x][y] = Tileset.FLOWER;
            }
        }

        // render frame
        StdDraw.clear(new Color(0, 0, 0));
        ter.drawTiles(tiles);
        StdDraw.show();
        StdDraw.pause(10);
    }
}
```

You'll notice that the flowers no longer look like flowers anymore. This is
because the font size is much too large, so the characters for each tile are
spilling into the other tiles.

**The Solution:**

The problem is that the tiles are being drawn with too large a font size, so
we'll use a method that resets the font size. Call the `resetFont` method in
your TERenderer class:

```java
/** Sets the font to the correct font for drawing tiles */
public void resetFont() {
    Font font = new Font("Monaco", Font.BOLD, TILE_SIZE - 2);
    StdDraw.setFont(font);
}
```

Then, call the method before you draw the tiles:

<table>
    <thead>
        <th>Before</th>
        <th>After</th>
    </thead>
<tr>
<td markdown="block">

```java
// render frame
StdDraw.clear(new Color(0, 0, 0));
ter.drawTiles(tiles);
StdDraw.show();
StdDraw.pause(10);
```
</td>
<td markdown="block">

```java
// render frame
ter.resetFont();
StdDraw.clear(new Color(0, 0, 0));
ter.drawTiles(tiles);
StdDraw.show();
StdDraw.pause(10);
```
</td>
</tr>
</table>

Now, when you run `FlowerWorld` the tiles should be drawn correctly.

### Custom image not rendering

**The Problem:**

If you are creating custom images for your game, then you may run into a bug where your images aren't rendering even after you have created a custom TETile with the correct filepath.

**The Solution:**

Make sure that your images are 16x16 pixels and stored as PNGs.