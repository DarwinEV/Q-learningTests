import gym
import numpy as np

env = gym.make("MountainCar-v0", render_mode='human')
# every environment must be reset at start
env.reset()

LEARNING_RATE = 0.1
DISCOUNT = 0.95 # measure of how much we value future reward over current
EPISODES = 25000

# its possible that we are in an environment where we won't know these values
# print(env.observation_space.high)
# print(env.observation_space.low)
# print(env.action_space.n)

# we want to make 20 buckets from the range of low to high
DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE
# print(discrete_os_win_size)
# q-table: a table storing all the possible combinations of actions that can be taken based on a certain position
# the actions will change as the model gets rewarded and learns what works
q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))

def get_discrete_state(state):
    # print(state)
    discrete_state = (state - env.observation_space.low) / discrete_os_win_size
    return tuple(discrete_state.astype(np.int32))

discrete_state = get_discrete_state(env.reset()[0]) # reset because we want the initial state


done = False
while not done: 
    action = np.argmax(q_table[discrete_state])
    new_state, reward, terminated, truncated, info = env.step(action)
    new_discrete_state = get_discrete_state(new_state)


    if not done:
        # the q value get back propagated down the table
        max_future_q = np.max(q_table[new_discrete_state])
        current_q = q_table[discrete_state + (action, )]

        # the formula for calculating all new q values
        q_new = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
        q_table[discrete_state + (action, )] = q_new # we are updating the q_table based on the new state and reward

    elif new_state[0] >= env.goal_position: # 
        q_table[discrete_state + (action, )] = 0
        # print(discrete_state + (action, ))

    discrete_state = new_discrete_state

env.close()

