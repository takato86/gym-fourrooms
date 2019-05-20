
## Get Started
```
git clone https://github.com/takato86/gym-fourrooms.git
cd gym-fourrooms
pip install -e .
```

After install, you can check the behaivor with the following code.

```
import gym
import gym_fourrooms

env = gym.make('Fourrooms-v0')
env.reset()
env.render()
env.step(0)
env.render()
```

## Env List
|name|version|description|
|---|---|---|
|Fiverooms|v0||
|Fourrooms|v0||
|Threerooms|v0||
