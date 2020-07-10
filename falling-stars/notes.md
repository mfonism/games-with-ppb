# For starters...

* Create a sprite (a cart)
* Each time the window is repainted, cart should be at point (0, 0) -- the centre of the window
* Instantiate a cart and add it to the current scene
* Run script

```
$ python falling-stars/main.py
```

## How about that warning?

```
$ python falling-stars/main.py
UserWarning: Using SDL2 binaries from pysdl2-dll 2.0.10
WARNING:ppb.assetlib:File not found: 'cart.png'
```

Let's focus on the second warning:
* Says it can't find a cart.png file. Let's give it one, and see what it does with it.

------

Save this [construction-production png from pngtree-dot-com](https://pngtree.com/so/construction-production) as cart.png in your project folder, and run `main.py` again.

Yaaaay!

Works like a charm.

------

# Let's get a movin'

We want to move in a certain direction with a certain speed. So, we need speed and direction.

* Set initial speed to 0
* Set initial direction to a zero vector

* When a direction key (left or right) is pressed, give it a non-zero speed, and set its direction appropriately
* `on_update` will handle the positioning on window repaint

When you run the script, the cart starts stationary on the window. Set it into motion with your direction keys.

Notice that you only need to press once for it to move in that direction.

Also notice that there's no way to bring it to a stop.

------

# Solving the Halting Problem

Well, a different kind of halting problem than [the one computer scientists have been grappling with for ages](https://en.wikipedia.org/wiki/Halting_problem#:~:text=In%20computability%20theory%2C%20the%20halting,or%20continue%20to%20run%20forever.)

We want to halt the motion whenever the space bar is pressed, and this is what we'll do on that key press:
* Set the speed to zero
* Set the direction to a zero vector

Now, pressing the space bar brings halts the cart. Awesome!

------

# Scaling Up

Our cart is too small. Let's resize it.

Excellent.

------

How about we position the cart on a horizontal plane very close to the bottom of the window? At the moment, it is too vertically centred.

------

# Respecting Boundaries

We don't want our cart leaving the viewport on either side. We have to set boundaries and make sure it respects them.

We'll need to know the coordinates of the far-right and far-left sides of our sprite, so we can detect when they collide with the far-right and far-left sides of the viewport.

Let's upgrade our sprite to a rectangle sprite for that.

* Let the Cart class inherit from the RectangleSprite class
* Clear the size of the cart and set a height instead -- the width will be automatically calculated
* On each update, check for collision with the sides of the viewport, and set direction so that cart bounces back

------

# A Star is Born

* Create a Star class which inherits from Sprite class
* It will be moving from top to bottom, so position it at the top of the viewport, and give it a downwards direction vector
* On each repainting of the window, the star should move downwards

------

## Aside

We don't really need to use init() in the Cart class. Like in the Star class, we can set all those things as class variables.

Then we make sure we instantiate carts without arguments so that the defaults hold.

------

# Re: A Star is Born

Did you notice we got a coloured placeholder square as the visual representation of our sprite.

If you run the script again and look at the terminal, you'll see a warning like one we've seen before:

```
...

WARNING:ppb.assetlib:File not found: 'star.png'
```

Let's give it a star.png file so it can do its thing.

------

Save this [star-clipart png from pngtree-dot-com](https://pngtree.com/so/star-clipart) as star.png in your project folder, and run `main.py` again.

Go celebrate yourself!

------

# In or Out -- Brace Up for This

Now we're going to detect when the star gets into the cart.

* If the bottom of the star is above the top of the cart, then it should keep falling
* Other wise, we have to check whether any part of the star overlaps a part of the cart
  + If it does, then the star is in the cart

For now, when we determine that the star is in the cart, we remove it from the scene.

If it has fallen outside the cart, we move it to a position at the top right corner of the scene.

------

If you play with it at this state long enough, you'll observe that sometimes you could swear your star has gone into the cart, but the game says otherwise.

I'll confess, that totally took me unaware. Almost drove me nuts.

The thing is, our images (cart.png and star.png) are larger than the actual size of the sprites they represent. And we didn't bother to resize them to fit the dimensions of our sprites. Matter of fact, we didn't even bother to set dimensions to our sprites!

Phew...

We had just one job!

------

# All of the Dimensions

In order to appreciate the problem at hand, rename your png files to something other than cart.png and star.png so that the game engine doesn't use them to represent the sprites.

I renamed mine **cart_.png** and **star_.png** so I can easily revert them.

When you run the game now, you'll notice the images are gone. All you can see are coloured squares.

And they are much smaller than the images made you think they were.

------

Let's be explicit about the dimensions of our cart and star, shall we!

* Make both sprite classes inherit from `RectangleSprite` (instead of `Sprite`) so we can set rectangular dimensions on them
* Set class variables `height` and `width` on each sprite class
  + Make the cart 2 units high and 6 units wide
  + Make the star 1 unit high and 1 unit wide (what shape is that, though?)

------

# House Keeping

The cart is as high as it is wide -- a square!

So we don't really need to inherit from `RectangleSprite`. `Sprite` will do.

And then, we don't need to set both height and width. Setting one will automatically set the other (because, square!)

And while we're at it, let's clean up the code for updating the star.

* Update the position of the star using its speed, its direction and the time elapsed since previous update
* Get a hold of the cart
* Check whether the star is in the cart:
  + If the bottom of the star has not fallen below the top of the cart, then it should keep falling
  + Otherwise halt the star for a moment
    * If the center of the star is within the space between the far-left and far-rights of the cart, then the star is in the cart

Recall that for now we're removing the star from the scene if it falls into the cart, and taking it to the top right corner of the viewport otherwise.

------

# Bring Back my PNGs

Well, you heard the girl.

Hurry, restore the original names of the png files for the cart and star.

Play the game.

------