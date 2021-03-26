destination_star = 10

current_star = 1
count = 1

for s in range(1, destination_star):
    # print(f'{current_star} requires {count} cards')
    current_star += 1
    count *= 2

print(f'{current_star} star troops require {count} cards')


chance_of_given_rare = 0.05
gold_per_pack = 240_000
cards_per_pack = 30

expected_count_per_pack = chance_of_given_rare * cards_per_pack

number_of_packs = count / expected_count_per_pack
cost = gold_per_pack * number_of_packs
print(f'It will cost {cost}g to purchase the {number_of_packs} packs needed to make a {current_star} star rare unit')
