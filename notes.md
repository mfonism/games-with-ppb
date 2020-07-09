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

Save this (https://pngtree.com/so/construction-production)[construction-production png from pngtree.com] as cart.png in your project folder, and run `main.py` again.

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
