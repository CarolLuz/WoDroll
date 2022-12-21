import random

def rolling_dice(message):

    def changeling(number, size, diff):
        dice_toss = [random.randint(1,size) for x in range(number)]
        sum_success = len([x for x in dice_toss if x >= diff])
        sum_ones = len([x for x in dice_toss if x == 1])
        number_success = sum_success - sum_ones

        if number_success >= 0:
            return f'{number_success} successes. \nDice: {dice_toss}'
        if number_success < 0:
            return f'Critical failure. Sorry. \nDice: {dice_toss}'
    
    def vampire(number, size, diff):
        dice_toss = [random.randint(1,size) for x in range(number)]
        sum_success = len([x for x in dice_toss if x >= diff and x != 10])
        sum_tens = len([x for x in dice_toss if x == 10])
        sum_ones = len([x for x in dice_toss if x == 1])
     
        number_success = sum_success - sum_ones
        number_success = number_success + sum_tens

        if number_success >= 0:
            return f'{number_success} successes. \nDice: {dice_toss}'
        if number_success < 0:
            return f'Critical failure. Sorry. \nDice: {dice_toss}'
    

    if 'roll' in message.lower():
        p_message = message.lower().split()
        diff = p_message[2]
        roll = p_message[0]
        number_dice = int(p_message[1].split('d', 1)[0])
        size_dice = int(p_message[1].split('d', 1)[1])
        if roll == '#rollc':
            changeling(number_dice, size_dice, diff)
        elif roll == '#rollv':
            vampire(number_dice, size_dice, diff)
        else:
            return 'Try again'
