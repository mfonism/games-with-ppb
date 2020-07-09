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
