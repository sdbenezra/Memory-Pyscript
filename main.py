from js import document

has_flipped_card = False
lockboard = False
first_card = None
first_card_id = None
second_card = None
second_card_id = None


def flip_card(event):
    global has_flipped_card, lockboard
    global first_card, first_card_id
    global second_card, second_card_id

    print("FLIP_CARD")
    if lockboard:
        return
    card = event.currentTarget
    card.classList.add('flip')
    print(f'Classlist: {card.classList}')
    print(f'Data-framework: {card.dataset.framework}')
    print(f'Id: {card.id}')
    evaluate(event)


def evaluate(event):
    global has_flipped_card
    global first_card, first_card_id
    global second_card, second_card_id

    print("EVALUATE")
    if not has_flipped_card:
        print(f'Flip card starting value for has_flipped_card: {has_flipped_card}')
        has_flipped_card = True
        first_card = event.currentTarget.dataset.framework
        first_card_id = event.currentTarget.id
        print(f'After has_flipped_card has been changed: {has_flipped_card}')
        print(f'First card: {first_card} - {first_card_id}')
    else:
        second_card_id = event.currentTarget.id
        if first_card_id == second_card_id:
            print(f'You chose the same card, please pick another')
            second_card_id = None
        else:
            second_card = event.currentTarget.dataset.framework
            second_card_id = event.currentTarget.id
            has_flipped_card = False
            print(f'first card type: {first_card}')
            print(f'second card type: {second_card}')
            check_for_match()


def check_for_match():
    global first_card, first_card_id
    global second_card, second_card_id

    print("CHECK_FOR_MATCH")
    if first_card == second_card and first_card_id != second_card_id:
        print("It's a match!")
        disable_cards()
    else:
        print("Not a match")
        unflip_cards()


def disable_cards():
    global first_card_id, second_card_id

    print("DISABLE_CARDS")
    document.getElementById(f"{first_card_id}").removeAttribute('py-click')
    document.getElementById(f"{second_card_id}").removeAttribute('py-click')
    first_card_id = None
    second_card_id = None


def unflip_cards():
    global lockboard
    global first_card, first_card_id
    global second_card, second_card_id
    print("SECOND CLASSLIST ######")
    print(document.getElementById(f"{second_card_id}").classList)
    print("UNFLIP")
    lockboard = True
    document.getElementById(f"{first_card_id}").classList.remove('flip')
    document.getElementById(f"{second_card_id}").classList.remove('flip')
    lockboard = False
    first_card = None
    first_card_id = None
    second_card = None
    second_card_id = None
