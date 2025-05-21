import random
# rand_int_num = random.randint(1, 10)
# print(rand_int_num)

# random_num_0_to_1 = random.random() * 10
random_num_0_to_1 = random.uniform(1, 10)
# print(random_num_0_to_1)

random_num_0_heads_1_tails = random.randint(0, 1)
if random_num_0_heads_1_tails == 0:
    print("Heads")
else:
    print("Tails")